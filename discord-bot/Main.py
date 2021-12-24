import discord
from discord.ext import commands
from webserver import keep_alive
import os


client = commands.Bot (command_prefix = "!")
client = remove_command = ('help')

@client.client
async def on_ready ():
    print ("Bot is currently online!")
    
    
    #help command
    @client.command(pass_context=True)
    async def help(ctx):
        author = ctx.message.author
        
        embed = discord embed(
            colour = discord.color.orange()
        )
        
        embed.set.author (name="Help")
        embed.add_field (name ="!help", value = "HelpCommand", inline = False)
                         
                         await client.send_message(author,embed-embed)
        await client.say ("Message sent to your DMs")
        
        
        keep alive()
        TOKEN = os.environ.get("DISCORD_BOT_SECRET")
        client.run(TOKEN)