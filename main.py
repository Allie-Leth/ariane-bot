import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from music import MusicCommands

load_dotenv(dotenv_path='.env')
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

# Add music commands to the bot
bot.add_cog(MusicCommands(bot))

@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user}")

# Run the bot
if __name__ == "__main__":
    bot.run("YOUR_DISCORD_BOT_TOKEN")