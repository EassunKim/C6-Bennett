# roll.py
import random
from discord.ext import commands

@commands.command(name='roll')
async def roll(ctx, max:str = None):

    try:
        if max is None:
            max = 100
        else:
            max = int(max)
            if max < 1:
                await ctx.send("Please provide a valid number")
                return
    except ValueError:
        max = 100
    

    # Roll a number between 0 and max (inclusive)
    result = random.randint(0, max)
    n = str(result)
    dubs: bool = all(digit == n[0] for digit in n)
    if dubs == True and len(n) >= 2:
        await ctx.send(f'🎲BOOM!🎲 \n {ctx.author.name} rolled {result}')
    else:
        await ctx.send(f'{ctx.author.name} rolled {result}')