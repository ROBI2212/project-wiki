# IMPORTS
import discord, json, random
from discord.ext import commands, tasks
from logger import logger, logging_date

# LOADING ACTIVITIES FROM ACTIVITIES.JSON
def load_activities(json_file):
    with open(json_file, "r",encoding="utf-8") as file:
        activities = json.load(file)
    return random.choice(activities)

class bot_activity(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.random_status.start()

    # CHANGE AVTIVITY PER 6 HOURS
    @tasks.loop(hours=6)
    async def random_status(self):
        new_activity = load_activities('activities.json')
        await self.client.change_presence(activity=discord.Game(new_activity))
        logger.info(f' {logging_date()} | Wiki robi coś nowego: {new_activity} :O')

    @random_status.before_loop
    async def before_random_status(self):
        await self.client.wait_until_ready()
        logger.info(f' {logging_date()} | Zmiana statusu, oczekiwanie na pamięć cache...')

async def setup(client):
    await client.add_cog(bot_activity(client))