import os
import random
import discord
import asyncio
from dotenv import load_dotenv
from discord import Intents, Message
from discord.ext import commands, tasks
from responses.responses import get_responses

# Load environment variables
load_dotenv()
TOKEN: str = os.getenv('DISCORD_TOKEN')

# Setup
intents: Intents = Intents.default()
intents.message_content = True

#command imports
bot = commands.Bot(command_prefix="$", intents=intents, help_command=None)

from responses.roll import roll #roll
bot.add_command(roll)

from responses.help.custom_help import setup as help_setup #help
help_setup(bot)

from responses.lfg import lfg #lfg
bot.add_command(lfg)

# responses
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Error with intents, message was empty')
        return

    try: 
        response: str = get_responses(user_message)
        if response:
            await message.channel.send(response)

    except Exception as e:
        print(f"Exception in send_message: {e}")

# STARTUP
@bot.event
async def on_ready() -> None:
    print(f'BOUKEN DA BOUKEN')

    #status cycle
    with open('rescources/statuses.txt') as file:
        statuses = [line.rstrip("'") for line in file]
    status.start(statuses)

    

#bot status
@tasks.loop(seconds = 300)
async def status(statuses):
    current_status=random.choice(statuses)
    await bot.change_presence(activity=discord.CustomActivity(name = current_status))


# MESSAGE HANDLING
@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user:
        return
    
    #sleephill
    if message.author.id == 217028904890793984:
        delete = random.randint(0, 100)
        if delete <= 1:
            await message.delete()

    # Check if the message is a command
    if message.content.startswith("$"):
        # Use the bot's process_commands to handle commands
        await bot.process_commands(message)
        
    else:
        # Handle regular messages
        user_message: str = message.content
        await send_message(message, user_message)

#Command error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Sorry that command was not found')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('youre missing something important, try $help')

#Run the bot
def main() -> None:
    bot.run(TOKEN)

if __name__ == '__main__':
    main()