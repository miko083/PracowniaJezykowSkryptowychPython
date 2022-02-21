# Based on https://github.com/RasaHQ/how-to-rasa

from email import message
import json
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionTellMeIfOpen(Action):

     def name(self) -> Text:
         return "action_tell_me_if_open"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        def check_if_open(day,hour):
            open_hour =  opening_hours[day]["open"]
            close_hour = opening_hours[day]["close"]
            if hour > open_hour and hour < close_hour:
                return True
            return False
        
        file_opening_hours = open('data_restaurant/opening_hours.json')
        data_opening_hours = json.load(file_opening_hours)
        opening_hours = data_opening_hours["items"]
        
        day = next(tracker.get_latest_entity_values("day"), None)
        hour = int(next(tracker.get_latest_entity_values("hour"), None))
        
        day = day.capitalize()
        message_to_return = ""
        if day in opening_hours:
            if check_if_open(day,hour):
                message_to_return = "Open on " + day + " at " + str(hour) + ". Feel free to order your food!"
            else:
                message_to_return = "Closed on " + day + " at " + str(hour) + "."
        else:
            message_to_return = "Wrong day, please try again."
        
        dispatcher.utter_message(text=message_to_return)
        return []


class ActionShareMenuList(Action):

     def name(self) -> Text:
         return "action_share_menu_list"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        file_menu = open('data_restaurant/menu.json')
        data_menu = json.load(file_menu)
        menu = data_menu["items"]

        menu_string = "=== === ===\n"

        for item in menu:
            menu_string += "Name: " + item["name"] + "\n"
            menu_string += "Price: " + str(item["price"]) + "\n"
            menu_string += "Estimated preparation time: " + str(item["preparation_time"]) + "\n"
            if menu.index(item) == len(menu) - 1:
                menu_string += "=== === ==="
            else:
                menu_string += "=== === ===\n"
        
        dispatcher.utter_message(text=menu_string)

        return []

# Get order (with "with" and ",")
class ActioOrderFood(Action):
    
    def name(self) -> Text:
         return "action_order_food"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        def convert_list_to_string(my_list):
            return ', '.join(map(str,my_list))
        
        file_menu = open('data_restaurant/menu.json')
        data_menu = json.load(file_menu)
        menu = data_menu["items"]
        
        full_order = next(tracker.get_latest_entity_values("full_order"), None)
        if full_order is None:
            dispatcher.utter_message(text="We don't have this meal. Please try another request.")
            return []
        
        full_order = full_order.replace(" and",",")

        allowed_food = []
        for item in menu:
            allowed_food.append(item["name"])
        
        # Sort food
        message_to_return = ""
        full_order = [item.strip() for item in full_order.split(",")]

        # Divide food into catgories
        final_order = []
        refused_meals = []
        prepare_times = []

        # Check if food exists.
        for food in full_order:
            temp_food = food.replace("without", "with")
            temp_split = temp_food.split("with")
            temp_food_name = temp_split[0].strip().capitalize()
            if temp_food_name in allowed_food:
                final_order.append(food)
                for item in menu:
                    if item["name"] == temp_food_name:
                        prepare_times.append(item["preparation_time"])
            else:
                refused_meals.append(food)

        # Prepare final message.
        if refused_meals:
            message_to_return += "Unfortunately, we don't have everything that you asked for.\n"

        if final_order:
            message_to_return += "We will prepare " +  convert_list_to_string(final_order) + ".\n"
            message_to_return += "Your food will be ready to pick-up in " + str(max(prepare_times) * 60) + " minutes."
        
        dispatcher.utter_message(text=message_to_return)
        
        return []

            





    


    

    


