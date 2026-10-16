import discord, os, requests
from discord import app_commands
from discord.ext import commands
from logger import logger, logging_date

def is_owner():
    async def predicate(interaction: discord.Interaction):
        return interaction.user.id == 256059086070743040
    return app_commands.check(predicate)

def tipi_person_details(id):
    url = "https://tipi.zhp.pl/api/persons/"
    header = {"X-API-KEY": os.getenv("API_TIPI")}
    request = requests.get(url+id,headers=header)
    request = request.json()
    return request

class tipi_api(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="tipi_person",description="Podstawowe informacje o osobie z systemu Tipi")
    @is_owner()
    async def tipiperson(self, interaction: discord.Interaction, id: str):
        response = tipi_person_details(id)
        embed = discord.Embed(title="Informacje z Tipi", description="Dane członka ZHP pobrane z systemu Tipi")
        embed.set_image(url="https://tipi.zhp.pl/javax.faces.resource/ImageStreamer_getPublicImage.jsf;jsessionid=zJLB_WOdR7LFRh0nRoqfYLU8XZugjgPmc8XkLnu_.7e3d7e83586d?ln=omnifaces.graphic&v=1590661987&p=LOGO&p=")
        embed.add_field(name="Imię",value=f"{response['firstName']}")
        embed.add_field(name="Nazwisko",value=f"{response['lastName']}")
        embed.add_field(name="Numer członkowski",value=f"{response['memberId']}")
        embed.add_field(name="Data dołączenia do ZHP",value=f"{response['entryDate']}")
        await interaction.response.send_message(embed=embed)


async def setup(client):
    await client.add_cog(tipi_api(client))