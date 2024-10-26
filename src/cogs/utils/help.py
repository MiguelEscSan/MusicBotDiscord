import discord

async def help(ctx):
    help_message = (
        "¡Hola! Aquí tienes una lista de comandos que puedes usar:\n\n"
        "!join - Conéctate al canal de voz.\n"
        "!leave - Desconéctate del canal de voz.\n"
        "!skip - Salta a la siguiente canción.\n"
        "!pause - Pausa la canción actual.\n"
        "!resume - Reanuda la canción pausada.\n"
        "!play <canción> - Reproduce la canción especificada.\n"
        "!stop - Detiene la reproducción actual.\n"
        "!help - Muestra esta ayuda.\n"
    )
    await ctx.send(help_message)