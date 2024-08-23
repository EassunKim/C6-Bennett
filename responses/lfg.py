#lfg.py
import re
from discord.ext import commands
from discord.ui import Button, View
import discord

intents = discord.Intents.default()
intents.message_content = True

#creating button
class AddButtons(discord.ui.View):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.list = set()

    @discord.ui.button(label="Let's Play!", style=discord.ButtonStyle.primary, custom_id="lets_play_button_1")
    async def lets_play(self, interaction: discord.Interaction, button: discord.ui.Button):
        user_mention = interaction.user.mention
        if user_mention not in self.list:
            self.list.add(user_mention)
            await self.update_message(interaction)
            await interaction.response.defer()
        else:
            await interaction.response.send_message(content="you're already on the list", ephemeral=True)
        

    @discord.ui.button(label="nvm...", style=discord.ButtonStyle.danger, custom_id="nvm_button_1")
    async def nvm(self, interaction: discord.Interaction, button: discord.ui.Button):
        user_mention = interaction.user.mention
        if user_mention in self.list:
            self.list.remove(user_mention)
            await self.update_message(interaction)
            await interaction.response.defer()
        else:
             await interaction.response.send_message(content="you're already not attending...", ephemeral=True)
            

    async def update_message(self, interaction):
        num_attending = len(self.list)
        ppl_list = "\n".join([f"> {mention}" for mention in self.list])
        # Update the message content with the new number and list
        new_content = f"{self.message.content.split('*Drafted: ')[0]} \n> *Drafted: {num_attending}* \n > \n> **Attendees:**\n{ppl_list}"

        await self.message.edit(content=new_content)

       
@commands.command(name='lfg')
async def lfg(ctx, *, activity: str):
    try:
        #process command
        matches = activity.split('"')
        matches = [matches[1], matches[2]]
        activity = matches[0]
        args = matches[1].split()
        lf = int(args[0])
    except (ValueError, IndexError) as e:
        await ctx.send("unintended usage: try $help lfg")

    lfg_message = f'''
    > # {activity} 
    > ### {ctx.author.mention} is looking for __{lf}__ friends
    > *Drafted: 0* \n > 
    > **Attendees:**
    '''

    message = await ctx.send(lfg_message)
    view = AddButtons(message)
    await message.edit(view=view)
