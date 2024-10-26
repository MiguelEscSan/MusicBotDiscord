async  def connect_to_voice_channel(ctx):

    if ctx.voice_client is not None and ctx.voice_client.is_connected():
        await ctx.send("Ya estoy conectado a un canal de voz")
        return

    voice_channel = ctx.author.voice.channel if ctx.author.voice else None
    if voice_channel is None:
        return await ctx.send("¡Necesitas estar en un canal de voz para usar este comando!")
    
    else:
        await voice_channel.connect()
        await ctx.send(f"Conectado a **{voice_channel}**")