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
        logger.info(f' {logging_date} | {interaction.user.name} każe mi mówić to: "{tekst}" na kanałe {interaction.channel}')

    # USER
    @app_commands.command(name="user", description="Informacje o użytkowniku")
    async def user(self, interaction: discord.Interaction, user: discord.Member | None=None):
        if user == None:
            user = interaction.user
        embed = discord.Embed(title=f"Informacje o {user.display_name}",color=discord.Color.green())

        embed.add_field(name="Na Discordzie od:",value=user.created_at.strftime("%d.%m.%Y"),inline=True)
        embed.add_field(name="Na serwerze od:",value=user.joined_at.strftime("%d.%m.%Y"),inline=True)
        embed.add_field(name="\u200b",value="\u200b",inline=True)

        embed.add_field(name="ID:",value=user.id,inline=True)
        booster = user.premium_since
        if booster == None:
            embed.add_field(name="Booster od:",value="Nie wspiera tego serwera :c",inline=True)
        else:
            embed.add_field(name="Booster od:",value=booster.strftime("%d.%m.%Y"),inline=True)
        embed.add_field(name="\u200b",value="\u200b",inline=True)

        activity = user.activity
        if activity == None:
            embed.add_field(name="Co robi:",value="Opierdala się xD")
        else:
            embed.add_field(name="Co robi:",value=user.activity)
        embed.add_field(name="Tag:",value=user.primary_guild.tag,inline=True)

        embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar)
        embed.set_footer(text="Copyright © 2026 Robert Mazur, Project Wiki v0.2")
        await interaction.response.send_message(embed=embed)

    # INFO
    @app_commands.command(name="info", description="Poznaj informacje o mnie :3")
    async def info(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Informacje o bocie",color=discord.Color.dark_blue())
        embed.add_field(name="Pierwsze uruchomienie",value="23.08.2026")
        embed.add_field(name="Wersja bota",value="0.2")
        embed.add_field(name="\u200b",value="\u200b",inline=True)

        embed.add_field(name="Geneza nazwy bota",value="Kundel o imieniu Wiki należący do babci Roberta")
        embed.set_footer(text="Copyright © 2026 Robert Mazur, Project Wiki v0.2")
        await interaction.response.send_message(embed=embed,ephemeral=True)

    # HELP
    @app_commands.command(name="help", description="Listo dostępnych komend")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Lista dostępnych komend")
        embed.add_field(name="/help",value="Lista dostępnych komend")
        embed.add_field(name="\u200b",value="\u200b",inline=True)

        embed.add_field(name="/user",value="Wyświetlam informacje o wskazanym użytkowniku albo o Tobie")
        embed.add_field(name="/ping",value="Ping-pong, szybka gra z Wikim")
        embed.add_field(name="\u200b",value="\u200b",inline=True)

        embed.add_field(name="/papuga",value="Napiszę to co chcesz")
        embed.add_field(name="/send_message",value="Napiszę to co chcesz na wskazanym przez Ciebie kanale **(admin only)**")
        embed.add_field(name="\u200b",value="\u200b",inline=True)

        embed.add_field(name="/change_status",value="Zmień wykonywaną przeze mnie czynność **(admin only)**")
        embed.set_footer(text="Copyright © 2026 Robert Mazur, Project Wiki v0.2")
        await interaction.response.send_message(embed=embed,ephemeral=True)

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