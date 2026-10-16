import discord, os, requests
from discord import app_commands
from discord.ext import commands
from logger import logger, logging_date

def is_owner():
    async def predicate(interaction: discord.Interaction):
        return interaction.user.id == 256059086070743040
    return app_commands.check(predicate)

def mikrus_stats():
    url = 'https://api.mikr.us/stats'
    data = {'srv': 'eve258', 'key': os.getenv('API_MIKRUS')}
    response = requests.post(url,data=data)
    data = response.json()
    return data

def mikrus_request(req):
    url = 'https://api.mikr.us/'
    data = {'srv': 'eve258', 'key': os.getenv('API_MIKRUS')}
    match req:
        case 'stats':
            url = url+'stats'
            response = requests.post(url,data=data)
            data = response.json()
        case 'exec':
            url = url+'exec'


class mikrus_api(commands.Cog):

    mikrus = app_commands.Group(name="mikrus",description="Zarządzanie serwerem mikr.us")
    def __init__(self,client):
        self.client = client
        self.mikrus

    # HOSTING STATS (CPU, RAM, DISC)
    @app_commands.command(name="stats",description="Statystyki serwera Mikr.us")
    @is_owner()
    async def stats(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Informacje o hostingu")
        # embed = embed.add_field("")
        response = mikrus_stats()
        await interaction.response.send_message(response["free"])
        # await interaction.response.send_message(embed, ephemeral=True)

    # MIKR.US API MAIN COMMAND
    @app_commands.command(name="mikrus",description="Zapytanie API Mikr.us")
    @is_owner()
    async def mikrus_api(self, interaction: discord.Interaction, cli: discord.SelectOption):
        response = mikrus_api()

    # @mikrus.command(name="exec",description="Wykonaj polecenie na serwerze")

    # @mikrus.command(name="wiki-restart", description="Restart bota")

    # @mikrus.command(name="wiki-rebuild", description="Zbudowanie obrazu bota na nowo")

async def setup(client):
    await client.add_cog(mikrus_api(client))