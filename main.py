import discord
import random
import os
from blocked import blocked_words

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#logs bot into server
@client.event
async def on_ready():
    print("I'm logged in as {0.user}".format(client))

@client.event
async def on_member_join(member):
  guild = client.get_guild(996937121115947048)
  channel = guild.get_channel(996937121115947051)
  await channel.send(f"Welcome to Pressure Junkies {member.mention}! :partying_face:\nI'm Scuba Steve! We hope you enjoy your time here! As you can tell, this server is somewhat slow, but we hope to grow and become a better server than the Scuba server! Please make sure to invite your friends! We also have a FB group and subreddit!\nReddit:r/pressurejunkies \nFB: fb://group/1264610087609008?ref=share")
  await member.send(f"Welcome to the {guild.name} server, {member.name}! I'm Scuba Steve!\nTo make this server more enjoyable, I have implemented a blocked words list, to ensure that everyone has an enjoyable experience. If you type any of these words, I will automatically delete your message.\nPlease make sure to invite your friends! We also have a FB group and subreddit! \nReddit:r/pressurejunkies \nFB: fb://group/1264610087609008?ref=share\nType: /help for help commands.\nType: /random to generate a random number.\nType: /zoom to track Zoom the Turtle.\nType: /marko to track Marko the Orca.\nType: /penny to track Penny the Mako.\nType: /ollie to track Ollie the Whale Shark.")


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    replies = {
        "hello": f"Hello {username}!",
        "hi": f"Hello {username}!",
        "hi scuba steve": f"Hello {username}!",
        "hi steve": f"Hello {username}!",
        "How's it going?": f"Great! How about you {username}?",
        "How's it going": f"Great! How about you {username}?",
        "Hows it going": f"Great! How about you {username}?",
        "hows it going": f"Great! How about you {username}?",
        "What's up?": f"What's up {username}?",
        "what's up?": f"What's up {username}?",
        "Whats up?": f"What's up {username}?",
        "Whats up": f"What's up {username}?",
        "whats up": f"What's up {username}?",
        "bye": f"See you later {username}!",
        "goodbye": f"See you later {username}!",
        "lol": f"I'm glad you found that funny, {username}!",
        "what is seanet": f'{username}, SeaNet is a Neural Network Artificial Intelligence system created by Oceandyne Systems INC for SSC-NOAA. which becomes self aware at 0214EDT, on August 29th, 2097, and begins the termination of the human species. This date is to be forever known as "Judgement Day".',
        "what is seanet?": f'{username}, SeaNet is a Neural Network Artificial Intelligence system created by Oceandyne Systems INC for SSC-NOAA. which becomes self aware at 0214EDT, on August 29th, 2097, and begins the termination of the human species. This date is to be forever known as "Judgement Day".',
      "what is SeaNet?": f'{username}, SeaNet is a Neural Network Artificial Intelligence system created by Oceandyne Systems INC for SSC-NOAA. which becomes self aware at 0214EDT, on August 29th, 2097, and begins the termination of the human species. This date is to be forever known as "Judgement Day".',
      "What is SeaNet?": f'{username}, SeaNet is a Neural Network Artificial Intelligence system created by Oceandyne Systems INC for SSC-NOAA. which becomes self aware at 0214EDT, on August 29th, 2097, and begins the termination of the human species. This date is to be forever known as "Judgement Day".'
    }

    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if user_message.lower() in replies:
        await message.channel.send(replies[user_message.lower()])
        return

    if message.author != client.user:
        for text in blocked_words:
            if "moderator" not in str(message.author.roles) and text in str(
                    message.content.lower()):
                await message.delete()
                return

    if user_message.lower() == '/help':
        response = f'Type: /help for help commands.\nType: /random to generate a random number.\nType: /zoom to track Zoom the Turtle.\nType: /marko to track Marko the Orca.\nType: /penny to track Penny the Mako.\nType: /ollie to track Ollie the Whale Shark.'
        await message.channel.send(response)
        return
        
    if user_message.lower() == '/random':
        response = f'This is your random number: {random.randrange(10000000)}'
        await message.channel.send(response)
        return

    if user_message.lower() == '/zoom':
        response = f'http://tracking.oceanproject.co/animal/zoom-turtle/track'
        await message.channel.send(response)
        return

    if user_message.lower() == '/marko':
        response = f'http://tracking.oceanproject.co/animal/marko-whale/track'
        await message.channel.send(response)
        return

    if user_message.lower() == '/penny':
        response = f'http://tracking.oceanproject.co/animal/penny-shark/track'
        await message.channel.send(response)
        return

    if user_message.lower() == '/ollie':
        response = f'http://tracking.oceanproject.co/animal/ollie-shark/track'
        await message.channel.send(response)
        return

client.run(os.getenv('TOKEN'))
