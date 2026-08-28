# IMPORTS
from discord.ext import commands
from logger import logger, logging_date

witajki = ['hejo','cześć','elo','ahoj','siemanko','hej','witajcie']
zegnajki = ['bayo','nara','naura','pa pa','do zobaczenia']

class messages(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
            # print(f'Wiadomość od {message.author} z kanału {message.channel}: {message.content}')
            if message.author == self.client.user:
                return 
    
            if message.content.lower().startswith(tuple(witajki)):
                await message.channel.send(f'Ahoy {message.author}! :3')
    
            if message.content.lower().startswith(tuple(zegnajki)):
                await message.channel.send(f'Do zobaczenia {message.author}! :heart:')
    
            if message.content.lower().startswith('hello there'):
                await message.channel.send(f'https://klipy.com/gifs/general-kenobi-general-grievous-4')
    
            if message.content.lower().startswith('dobranoc'):
                await message.channel.send(f'Dobrej nocki {message.author}, kolorowych snów! :smiling_face_with_3_hearts:')
    
        # async def on_reaction_add(self, reaction, user):
        #    await reaction.message.channel.send('Zareagowałeś! :heart:')

async def setup(client):
    await client.add_cog(messages(client))