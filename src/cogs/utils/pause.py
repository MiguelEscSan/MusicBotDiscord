async def pause(ctx):
    voice_client = ctx.voice_client

    if voice_client is None:
        return await ctx.send("No estoy conectado a un canal de voz")

    if voice_client.is_paused():
        return await ctx.send("La canción ya está pausada")

    if voice_client.is_playing():
        voice_client.pause()
        await ctx.send("Canción pausada")
