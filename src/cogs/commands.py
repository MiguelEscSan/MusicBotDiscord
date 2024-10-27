import discord
from discord.ext import commands
from src.cogs.utils.skip import skip
from src.cogs.utils.connect_to_voice_channel import connect_to_voice_channel
from src.cogs.utils.disconnect_from_voice_channel import disconnect_from_voice_channel
from src.cogs.utils.pause import pause
from src.cogs.utils.resume import resume
from src.cogs.utils.play import play
from src.cogs.utils.stop import stop
from src.embeds.playlist import playlist_embed

async def setup(bot):

    @bot.command(name="join")
    async def join_command(ctx):
        await connect_to_voice_channel(ctx)

    @bot.command(name="leave")
    async def leave_command(ctx):
        await disconnect_from_voice_channel(ctx)

    @bot.command(name="skip")
    async def skip_command(ctx):
        await skip(ctx)

    @bot.command(name="pause")
    async def pause_command(ctx):
        await pause(ctx)

    @bot.command(name="resume")
    async def resume_command(ctx):
        await resume(ctx)

    @bot.command(name="play")
    async def play_command(ctx, *, query):
        await play(ctx, query)
        await playlist_embed(ctx)

    @bot.command(name="stop")
    async def stop_command(ctx):
        await stop(ctx)