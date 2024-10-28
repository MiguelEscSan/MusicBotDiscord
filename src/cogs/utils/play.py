import discord
from discord.ext import commands
import yt_dlp
from pytube import YouTube

from src.cogs.structure import queue, play_next, current_song

ydl_options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0'
}

async def play(ctx, search):
    voice_channel = ctx.author.voice.channel if ctx.author.voice else None
    if voice_channel is None:
        return await ctx.send("¡Necesitas estar en un canal de voz para usar este comando!")
    elif ctx.voice_client is None and voice_channel is not None:
        await ctx.author.voice.channel.connect()

    async with ctx.typing():
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            is_url = "https://" in search
            query = search if is_url else f"ytsearch:{search}"
            info = ydl.extract_info(query, download=False)
            # Verifica si es una URL directa o un término de búsqueda con resultados
            if is_url or ('entries' in info and info['entries']):
                video = info if is_url else info['entries'][0]
                url, title = video['url'], video['title']
                queue[ctx.guild.id].append({'url': url, 'title': title})
                await ctx.send(f"Se ha añadido **{title}** a la cola")

                if not ctx.voice_client.is_playing():
                    await play_next(ctx)
            else:
                await ctx.send("No se encontró ningún resultado para tu búsqueda.")
