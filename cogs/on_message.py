# IMPORTS
import re
from discord.ext import commands
from logger import logger, logging_date

witajki = ['hejo','cześć','elo','ahoj','siemanko','hej','witajcie']
zegnajki = ['bayo','nara','naura','pa pa','do zobaczenia']

class messages(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
            new_message = message.content.lower().strip()
            bot_mention = (re.search(r"\bwiki\b",new_message) is not None or self.client.user in message.mentions) 
            # print(f'Wiadomość od {message.author} z kanału {message.channel}: {message.content}')
            if message.author == self.client.user:
                return 
    
            if new_message.startswith(tuple(witajki)) and bot_mention:
                await message.channel.send(f'Ahoy {message.author}! :3')
    
            if new_message.startswith(tuple(zegnajki)) and bot_mention:
                await message.channel.send(f'Do zobaczenia {message.author}! :heart:')
    
            if new_message.startswith('hello there'):
                await message.channel.send(f'https://klipy.com/gifs/general-kenobi-general-grievous-4')
    
            if new_message.startswith('dobranoc') and bot_mention:
                await message.channel.send(f'Dobrej nocki {message.author}, kolorowych snów! :smiling_face_with_3_hearts:')
    
        # async def on_reaction_add(self, reaction, user):
        #    await reaction.message.channel.send('Zareagowałeś! :heart:')
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.guild.system_channel.send(f'Witaj {member.mention}! :smiling_face_with_3_hearts:')
        logger.info(f' Użytkownik {member.name}, {member.id} dołączył na serwer {member.guild}.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await member.guild.system_channel.send(f'{member.name} nas zostawił :cry:')
        logger.info(f' Użytkownik {member.name} opuścił serwer {member.guild}')

async def setup(client):
    await client.add_cog(messages(client))