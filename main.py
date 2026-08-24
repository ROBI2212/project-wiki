import discord
from discord.ext import commands
from discord import app_commands

witajki = ['hejo','cześć','elo','ahoj','siemanko','hej','witajcie']
zegnajki = ['bayo','nara','naura','pa pa','do zobaczenia']
game = discord.Game('Kopie diaxy')

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Zalogowano jako {self.user}!')
        await client.change_presence(activity=game)

        try:
            synced = await self.tree.sync()
            print(f'Zsynchronizowano {len(synced)} poleceń!')
        except Exception as e:
            print(f'Błąd synchronizacji polecenia: {e}')

    

    async def on_message(self, message):
        # print(f'Wiadomość od {message.author} z kanału {message.channel}: {message.content}')
        if message.author == self.user:
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



intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="/", intents=intents)

class MessageModal(discord.ui.Modal, title="Wyślij wiadomość"):
    message = discord.ui.TextInput(
        label="Treść wiadomości",
        style=discord.TextStyle.paragraph,
        placeholder="Wpisz tutaj wiadomość",
        required=True,
        max_length=4000
    )
    def __init__(self, channel: discord.TextChannel):
        super().__init__()
        self.channel=channel

    async def on_submit(self, interaction: discord.Interaction):
        try:
            await self.channel.send(self.message.value)
            await interaction.response.send_message(f'Wiadomość została wysłana na {self.channel.mention}.',ephemeral=True)
        except discord.Forbidden:
             await interaction.response.send_message(f'Nie posiadam uprawnień do tego kanału :sob:',ephemeral=True)
        except discord.HTTPException:
            await interaction.response.send_message(f'Wystąpił błąd podczas wysyłania wiadomości',ephemeral=True)

@client.tree.command(name="ping", description="Szybka gra z Wikim :3")
async def sayPong(interaction: discord.Interaction):
    await interaction.response.send_message("Pong :ping_pong:")

@client.tree.command(name="papuga", description="Dzwoni papuga, mówi, że musi się udać")
async def printer(interaction: discord.Interaction, tekst: str):
    await interaction.response.send_message(tekst)

@client.tree.command(name="send_message",description="Wyślij wiadomość na wybrany kanał")
@app_commands.default_permissions(administrator=True)
async def send_message(interaction: discord.Interaction, channel: discord.TextChannel):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(f'Nie masz uprawnień do używania tego polecenia',ephemeral=True)
            return
        await interaction.response.send_modal(
            MessageModal(channel)
        )


client.run('BOT_TOKEN_HERE')