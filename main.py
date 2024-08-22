import os
from dotenv import load_dotenv
from discord import Intents, Message
from discord.ext import commands
from responses.responses import get_responses
from responses.roll import roll

# Load environment variables
load_dotenv()
TOKEN: str = os.getenv('DISCORD_TOKEN')

# Setup
intents: Intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)
bot.add_command(roll)

# COMMANDS
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

# MESSAGE HANDLING
@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user:
        return

    # Check if the message is a command
    if message.content.startswith("$"):
        # Use the bot's process_commands to handle commands
        await bot.process_commands(message)
    else:
        # Handle regular messages
        user_message: str = message.content
        await send_message(message, user_message)

# Run the bot
def main() -> None:
    bot.run(TOKEN)

if __name__ == '__main__':
    main()