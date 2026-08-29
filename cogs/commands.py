# IMPORTS
import discord
from discord import app_commands
from discord.ext import commands
from logger import logger, logging_date

class commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    class MessageModal(discord.ui.Modal, title="Wyślij wiadomość"):
        message = discord.ui.TextInput(
            label="Treść wiadomości",
            style=discord.TextStyle.paragraph,
            placeholder="Wpisz tutaj wiadomość",
            required=True,
            max_length=2000
        )
        def __init__(self, channel: discord.TextChannel):
            super().__init__()
            self.channel=channel

        async def on_submit(self, interaction: discord.Interaction):
            try:
                await self.channel.send(self.message.value)
                await interaction.response.send_message(f'Wiadomość została wysłana na {self.channel.mention}.',ephemeral=True)
                logger.info(f' {logging_date()} | Użytkownik {interaction.user} wysłał wiadomość na kanał #{self.channel.name} ({interaction.guild}). Treść: {self.message.value}')
            except discord.Forbidden:
                await interaction.response.send_message(f'Nie posiadam uprawnień do tego kanału :sob:',ephemeral=True)
                logger.info(f' {logging_date()} | Użytkownik {interaction.user} chciał wysłać wiadomość na kanał #{self.channel.name}, ale nie mam tam uprawnień :c')
            except Exception as e:
                await interaction.response.send_message(f'Wystąpił błąd podczas wysyłania wiadomości. Skontaktuj się z administratorem!',ephemeral=True)
                logger.info(f' {logging_date()} | Użytkownik {interaction.user} chciał wysłać wiadomość na kanał #{self.channel.name}, ale napotkał błąd: {e}')

    # COMMANDS
    # PING
    @app_commands.command(name="ping", description="Szybka gra z Wikim :3")
    async def ping(self, interaction: discord.Interaction):
        latency_ms = round(self.client.latency*1000,2)
        await interaction.response.send_message(f'Pong :ping_pong:, {latency_ms} ms')

    # PAPUGA
    @app_commands.command(name="papuga", description="Dzwoni papuga, mówi, że musi się udać")
    async def printer(self, interaction: discord.Interaction, tekst: str):
        await interaction.response.send_message(tekst)

    # SEND_MESSAGE
    @app_commands.command(name="send_message",description="Wyślij wiadomość na wybrany kanał")
    @app_commands.default_permissions(administrator=True)
    async def send_message(self, interaction: discord.Interaction, channel: discord.TextChannel):
            if not interaction.user.guild_permissions.administrator:
                await interaction.response.send_message(f'Nie masz uprawnień do używania tego polecenia',ephemeral=True)
                return
            await interaction.response.send_modal(
                self.MessageModal(channel)
            )

    # CHANGE_STATUS
    @app_commands.command(name="change_status",description="Zmień mój status")
    @app_commands.describe(status="Nowy status bota wyświetlany na Discordzie")
    @app_commands.default_permissions(administrator=True)
    async def change_status(self, interaction: discord.Interaction, status: str):
        await self.client.change_presence(activity=discord.Game(status))
        await interaction.response.send_message(f'Status został zmieniony.',ephemeral=True)
        logger.info(f' {logging_date()} | Użytkownik {interaction.user} zmienił status bota na {status}')


async def setup(client):
    await client.add_cog(commands(client))
