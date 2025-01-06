import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from music import MusicCommands

# Load environment variables from the .env file
load_dotenv()  # Automatically detects .env in the same directory
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("No DISCORD_TOKEN found in environment or .env file!")

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user}")
    await bot.add_cog(MusicCommands(bot))
# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)

