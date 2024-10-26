async def resume(ctx):
    voice_client = ctx.voice_client

    if voice_client is None:
        return await ctx.send("No estoy conectado a un canal de voz")

    if voice_client.is_playing():
        return await ctx.send("La canción ya se está reproduciendo")

    if voice_client.is_paused():
        voice_client.resume()
        await ctx.send("Canción reanudada")
    else:
        await ctx.send("No hay ninguna canción pausada")