import discord

witajki = ['hejo','cześć','elo','ahoj','siemanko','hej','witajcie']
zegnajki = ['bayo','nara','naura']

class Client(discord.Client):
    async def on_ready(self):
        print(f'Zalogowano jako {self.user}!')

    async def on_message(self, message):
        # print(f'Wiadomość od {message.author} z kanału {message.channel}: {message.content}')
        if message.author == self.user:
            return 

        if message.content.lower().startswith(tuple(witajki)):
            await message.channel.send(f'Ahoy {message.author}! :3')

        if message.content.lower().startswith(tuple(zegnajki)):
            await message.channel.send(f'Do zobaczenia {message.author}! :heart:')

        if message.content.lower().startswith('hello there'):
            await message.channel.send(f'General Kenobi')

        if message.content.lower().startswith('dobranoc'):
            await message.channel.send(f'Dobrej nocki {message.author}, kolorowych snów! :smiling_face_with_3_hearts:')

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('Zareagowałeś! :heart:')

intents = discord.Intents.default()
intents.message_content = True


client = Client(intents=intents)
client.run('BOT_TOKEN_HERE')