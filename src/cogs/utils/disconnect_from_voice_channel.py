async def disconnect_from_voice_channel(ctx):
    if ctx.voice_client is None:
        return await ctx.send("No estoy conectado a un canal de voz")

    await ctx.voice_client.disconnect()
    await ctx.send("Desconectado del canal de voz")