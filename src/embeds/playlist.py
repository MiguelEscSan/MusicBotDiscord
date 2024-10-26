from tkinter import Button

import discord
from src.cogs.structure import queue, current_song

async def playlist_embed(ctx):
    current_song_file = current_song.get(ctx.guild.id)
    current_song_title = current_song_file['title'] if current_song_file else "No hay cancion actual."

    if not queue[ctx.guild.id]:
        queue_list = "No hay temas en la cola."
    else:
        queue_list = "\n".join(f"{index + 1}. {song['title']}" for index, song in enumerate(queue[ctx.guild.id]))

    playlist_embed = {
        "content": "",
        "tts": False,
        "embeds": [
            {
                "title": "Cancion Actual:",
                "description": current_song_title,
                "color": 4723301,
                "fields": [
                    {
                        "name": "Siguientes canciones:",
                        "value": queue_list,
                        "inline": False
                    }
                ],
                "author": {
                    "name": "Playlist"
                }
            }
        ],
        "components": [],
        "actions": {}
    }

    embed = discord.Embed.from_dict(playlist_embed["embeds"][0])


    await ctx.send(embed=embed)