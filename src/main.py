import os
from discord.ext import tasks, commands
import discord
from dotenv import load_dotenv
import os

load_dotenv()

class MusicBot(commands.Bot):
    # Para cargar los SlashCommands
    async def setup_hook(self):
        for directory in ['./cogs']:
            for filename in os.listdir(directory):
                if filename.endswith('.py') and filename not in ('structure.py', 'buttons_cogs.py'):
                    extension = f'{directory[2:]}.{filename[:-3]}'
                    try:
                        await self.load_extension(extension)
                        print(f'Loaded {extension}')
                    except Exception as e:
                        print(f'Failed to load extension {extension}: {e}')

    @tasks.loop(minutes=5)
    async def check_voice_status(self):
        for ctx in self.guilds:
            voice_client = ctx.voice_client
            if voice_client and not voice_client.is_playing() and not voice_client.is_paused():
                await voice_client.disconnect()

    @check_voice_status.before_loop
    async def before_check_voice_status(self):
        await self.wait_until_ready()


bot = MusicBot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Conectado como: {bot.user}")

if __name__ == "__main__":
    bot.run(os.getenv('TOKEN'))