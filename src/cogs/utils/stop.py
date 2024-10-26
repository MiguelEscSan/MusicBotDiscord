from src.cogs.structure import queue

async def stop(ctx):
    voice_client = ctx.voice_client

    if voice_client is None:
        return await ctx.send("No estoy conectado a un canal de voz")

    if voice_client.is_playing():
        voice_client.stop()
        queue.clear()
        await ctx.send("Canción detenida")
    else:
        await ctx.send("No hay ninguna canción reproduciéndose")