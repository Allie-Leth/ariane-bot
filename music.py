import discord
from discord.ext import commands
import yt_dlp

class MusicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        """Join the voice channel of the user."""
        if not ctx.author.voice:
            await ctx.send("You must be in a voice channel to use this command.")
            return
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        """Leave the current voice channel."""
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("Disconnected from the voice channel.")
        else:
            await ctx.send("I'm not in a voice channel.")

    @commands.command()
    async def play(self, ctx, url):
        """Play audio from a YouTube URL."""
        if not ctx.voice_client:
            await ctx.send("I need to be in a voice channel to play music. Use `!join` first.")
            return

        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                audio_url = info['url']

            # Play the audio
            ctx.voice_client.stop()
            ctx.voice_client.play(discord.FFmpegPCMAudio(source=audio_url),
                                  after=lambda e: print(f"Finished playing: {e}"))
            await ctx.send(f"Now playing: {info['title']}")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
