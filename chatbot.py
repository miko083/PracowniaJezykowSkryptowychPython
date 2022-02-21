import discord
import requests
import os

from dotenv import load_dotenv

#Load Discord Bot Token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print("Login: " + str(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    author = message.content.split(" ", 1)[0] 
    cut_message = message.content.split(" ", 1)[1]  
    my_request = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"sender": author, "message": cut_message})
    all_lines = my_request.json()
    final_message = ""
    for line in all_lines:
        final_message += '\n' + line.get('text')
    await message.channel.send(final_message)

client.run(token)