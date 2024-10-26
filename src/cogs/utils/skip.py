async def skip(ctx):
    voice_client = ctx.voice_client

    if voice_client is None:
        return await ctx.send("No estoy conectado a un canal de voz")

    if not voice_client.is_playing():
        return await ctx.send("No hay ninguna canción reproduciéndose")
    else:
        voice_client.stop()
        await ctx.send("Canción saltada")