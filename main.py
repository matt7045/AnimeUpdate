import discord
import json
from CrunchyParser import CrunchyParser
from time import sleep

#Get the configuration from the config file
with open("credentials.config", 'r') as f:
    configuration = json.load(f)
discord_token = configuration['discord_token']

#First, generate a global client we can use to talk to discord
client = discord.Client()
#Lets the console know we've successfully logged in
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#When we receive a message...
@client.event
async def on_message(message):
    #Split the message into it's sections
    message_parts = message.content.lower().split(' ')
    #Check to see if they're talking about Anime
    if ('anime' in message.content.lower()) or ('waifu' in message.content.lower()):
        await message.add_reaction('\U0001f618')
      #If the message is an update command
    if (message_parts[0] == '!weeb'):
        #Get the name of the anime, and the 'lookback' number
        if(len(message_parts)>1):
            lookback_included = False
            lookback = 0
            #If we included more than one thing, there's a possibility
            # that extra thing at the end is the lookback. If it can
            # be decoded as a number, assume it is. 
            if (len(message_parts)>2):
                try:
                    lookback = abs(int(message_parts[-1]))
                    lookback_included = True
                except ValueError:
                    lookback = 0
            if lookback_included:
                anime_name = ' '.join(message_parts[1:-1])
            else:
                anime_name = ' '.join(message_parts[1:])
            #Get the descriptions for the most recent episodes of that anime
            try:
                descriptions = CrunchyParser.getShortDescriptions(anime_name)
                description  = '|| **'+descriptions[lookback]['name']+'**\n\n'+descriptions[lookback]['description']+' ||'
            except ValueError:
                description = "Hrm...I couldn't seem to find "+anime_name+'. Sorry darling \U0001f97a \U0001f606 \U0001f618'
            except IndexError:
                description = "Ohhh that's too big \U0001f974 I can't handle that \U0001f61D"
            await message.channel.send(description)
            print('Sent message...\n'+description+'\n\n')


#Run the client
try:
    client.run(discord_token)
except Exception as e:
    CrunchyParser.cleanup()
    print(e)
finally:
    CrunchyParser.cleanup()
sleep(1)


