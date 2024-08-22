from discord.ext import commands

@commands.command(name='help')
async def custom_help(ctx, command_name=None):
    if command_name is None:
        try:
            with open('responses/help/help.txt', 'r') as file:
                content = file.read()

                await ctx.send(content)

        except FileNotFoundError:
            await print("something has happened to the markdown file for $help")
    else:
        if command_name == 'roll':
            await ctx.send('`$roll <max value (inclusive)>` - rolls a random value in the given range')
        else:
            await ctx.send(f"no information found about the command `{command_name[0:10]}`")

def setup(bot):
    bot.add_command(custom_help)
            