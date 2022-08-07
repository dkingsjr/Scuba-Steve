import discord
import random
import os
from blocked import *

client = discord.Client()

#logs bot into server
@client.event
async def on_ready():
  print("I'm logged in as {0.user}".format(client))

#
@client.event
async def on_message(message):
  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  replies = {
    "hello": f"Hello {username}!", "hi": f"Hello {username}!", 
    "How's it going?": f"Great! How about you {username}?", "How's it going": f"Great! How about you {username}?",
    "Hows it going": f"Great! How about you {username}?", "hows it going": f"Great! How about you {username}?",
    "What's up?": f"What's up {username}?", "what's up?": f"What's up {username}?", 
    "Whats up?": f"What's up {username}?", "Whats up": f"What's up {username}?",
    "whats up": f"What's up {username}?", "bye": f"See you later {username}!", "goodbye": f"See you later {username}!"
}
  
  print(f'{username}: {user_message} ({channel})')

@client.event
async def on_message(message):
  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)

  if message.author == client.user:
    return

  if user_message.lower() in replies:
    await message.channel.send(replies[user_message.lower()])
    return

  if message.author != client.user:
    for text in blocked_words:
      if "moderator" not in str(message.author.roles) and text in str(message.content.lower()):
        await message.delete()
        return

  if user_message.lower() == '-random':
    response = f'This is your random number: {random.randrange(10000000)}'
    await message.channel.send(response)
    return

  if user_message.lower() == '-help':
    response = f'Type -help for help commands.\nType -zoom to track Zoom the Turtle.\nType -marko to track Marko the Orca.\nType -penny to track Penny the Mako.\nType -ollie to track Ollie the Whale Shark.'
    await message.channel.send(response)
    return

  if user_message.lower() == '-zoom':
    response = f'http://tracking.oceanproject.co/animal/zoom-turtle/track'
    await message.channel.send(response)
    return

  if user_message.lower() == '-marko':
    response = f'http://tracking.oceanproject.co/animal/marko-whale/track'
    await message.channel.send(response)
    return

  if user_message.lower() == '-penny':
    response = f'http://tracking.oceanproject.co/animal/penny-shark/track'
    await message.channel.send(response)
    return

  if user_message.lower() == '-ollie':
    response = f'http://tracking.oceanproject.co/animal/ollie-shark/track'
    await message.channel.send(response)
    return

client.run(os.getenv('TOKEN'))