# IMPORTS
import discord, os, asyncio
from cogs import commands
from dotenv import load_dotenv
from discord.ext import commands
from logger import logger, logging_date

game = discord.Game('BERCIK MNIE PSUJE 😰')
load_dotenv()

# LOADING EXTENDES FILES
async def load_cogs():
    await client.load_extension("cogs.commands")
    await client.load_extension("cogs.on_message")
    await client.load_extension("cogs.bot_activity")
    logger.info(f' Pozostałe pliki wczytane!')

class Client(commands.Bot):
    async def on_ready(self):
        logger.info(f' {logging_date()} | Wiki wstał! Zalogowano jako {self.user}!')
        await client.change_presence(activity=game)

        try:
            synced = await self.tree.sync()
            logger.info(f' {logging_date()} | Zsynchronizowano {len(synced)} poleceń!')
        except Exception as e:
            logger.info(f' {logging_date()} | Błąd synchronizacji polecenia: {e}')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = Client(command_prefix="/", intents=intents)

# LAUNCHING BOT
async def main():
    await load_cogs()
    await client.start(os.getenv("BOT_TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())