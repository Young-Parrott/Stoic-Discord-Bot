import os
import requests
import json

client = discord.Client()

def get_quote():

    # get random stoic quote from api
    response = requests.get("https://stoic-api.herokuapp.com/api/v1/random")

    #convert the response into JSON loads from a string
    json_data = json.loads(response.text)
    
    quote = "\"" +json_data['saying'] + "\"" + "\n\n -" + json_data['author'] + "\n" + json_data['source']
    return quote

# decorator that is used to register an event
@client.event

# on ready is called when the bot is ready to start being used
async def on_ready():
    print('Logging in as {0.user}'.format(client))

# decorator
@client.event

# triggers each time a message is received
# but only when message author is the same as client.user
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)


client.run('YOUR_DISCORD.PY_TOKEN_HERE')

