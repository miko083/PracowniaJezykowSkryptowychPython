## Python chatbot

### Features

Project made for 4.5 grade based on [these requirements](https://github.com/codete/oreilly-intelligent-bots/blob/master/Homework.ipynb):
>A chatbot with the trained ability to handle at least 3 ways to phrase those intents.

>Information about opening hours and menu items should be fetched from the configuration file.

>Chatbot needs to process the order and confirm purchased meals, as well as additional requests.

>Chatbot needs to confirm when the meal will be available as a pick-up in the restaurant.

>Integrate it with one of the platforms mentioned in Chabots_Integration notebook.

### Examples:

Greeting:
```
Your input ->  Hi
Hey! How can I help you?
```

Get information about hours:
```
Your input ->  Is this restaurant open on monday at 22?
Closed on Monday at 22.
```

Get information about menu:
```
Your input ->  Could you send me a menu?
=== === ===
Name: Lasagne
Price: 16
Estimated preparation time: 1
=== === ===
Name: Pizza
etc.
```

Make order:
```
Your input ->  I want cake.
We don't have this meal. Please try another request.
```
```
Your input ->  I want hot-dog with jalapeno and pizza without olives
We will prepare hot-dog with jalapeno, pizza without olives.
Your food will be ready to pick-up in 30.0 minutes.
```

```
Your input ->  For me hot-dog with extra dip and burger without tomatoes.
We will prepare hot-dog with extra dip, burger without tomatoes.
Your food will be ready to pick-up in 12.0 minutes.
```

### Requirements

* [Docker](https://www.docker.com/)

### Start in shell

To train:
```
./run_train.sh
```

In seperate terminal windows or in background:
```
./run_actions.sh
./run_rasa_shell.sh
```


### Integration with Discord

Please put your token in the file `.env` in main directory:
```
DISCORD_TOKEN=<your-token>
```

Based on (and more information how to setup and get token is also here) [Rasa-discord-bot repo](https://github.com/Cybercube21/Rasa-discord-bot).


#### Start 
In seperate terminal windows or in background:

```
./run_actions.sh
./run_chatbot.sh
python3 chatbot.py
```

#### To talk with the bot (after added to the channel):
```
@<BOT-NAME> <message>
```

Example:
```
@ChatBotUJ Are you open on sunday at 21 ?
```