import discord
import yt_dlp

queue = []
current_song = {}

async def play_next(ctx):
    if queue:
        url, title = queue.pop(0)
        try:
            source = discord.FFmpegOpusAudio(url, before_options="-reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 -reconnect_delay_max 2")
            ctx.voice_client.play(source, after=lambda _: ctx.voice_client.loop.create_task(play_next(ctx)))
            await ctx.send(f"Reproduciendo **{title}**")
        except Exception as e:
            print("Error al reproducir la fuente:", e)
            await ctx.send("Ocurrió un error al intentar reproducir la canción.")
    else:
        await ctx.send("No hay más canciones en la cola")