import discord
from discord.ext import commands
from src.cogs.utils.pause import pause
from src.cogs.utils.resume import resume
from src.cogs.utils.skip import skip
from src.cogs.utils.stop import stop

class ButtonView(discord.ui.View):

    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx

    @discord.ui.button(emoji='⏸️', style=discord.ButtonStyle.red)
    async def pause(self,  interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await self.ctx.invoke(self.ctx.bot.get_command('pause'))

    @discord.ui.button(emoji='▶️', style=discord.ButtonStyle.green)
    async def resume(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await self.ctx.invoke(self.ctx.bot.get_command('resume'))

    @discord.ui.button(emoji='⏭️', style=discord.ButtonStyle.blurple)
    async def skip(self,  interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await self.ctx.invoke(self.ctx.bot.get_command('skip'))

    @discord.ui.button(emoji='⏹️', style=discord.ButtonStyle.danger)
    async def stop(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await self.ctx.invoke(self.ctx.bot.get_command('stop'))

class ButtonCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="buttons")
    async def show_buttons(self, ctx):
        view = ButtonView(ctx)
        await ctx.send("Controla la música con los botones:", view=view)

async def setup(bot: commands.Bot):
    await bot.add_cog(ButtonCog(bot))