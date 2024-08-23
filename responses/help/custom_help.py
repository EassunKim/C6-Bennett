from discord.ext import commands

@commands.command(name='help')
async def custom_help(ctx, command_name=None):
    if command_name is None:
        try:
            with open('responses/help/help.txt', 'r') as file:
                content = file.read()

                await ctx.send(content)

        except FileNotFoundError:
            await print("something has happened to the text file for $help")
    else:
        if command_name == 'roll':
            await ctx.send('''```roll command information:
                           
    Usage: $roll <max> - rolls a random number between 0 and the given max
        - number must be >= 0
        - any text after <max> is ignored
        - if no number is specified <max> is defaulted to 100

        Example:
        $roll 10000```''')
               
        elif command_name == 'lfg':
            await ctx.send('''```lfg command information:
                           
    Usage: $lfg "<description>" <# of people> <@role> - creates an attendance list for an activity 
        - @ing a role is optional

        Example:
        $lfg "Valorant 10 Mans" 10 @valorant```''')
        else:
            await ctx.send(f"no information found about the command `{command_name[0:10]}`")

def setup(bot):
    bot.add_command(custom_help)
            