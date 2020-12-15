# chip_v1.py
import discord
from discord.ext import commands
import random
print("Starting bot...")
TOKEN = "XXXX" #make it read text file to get token
#TOKEN = open("secret_token.txt","r").readline()
client = commands.Bot(command_prefix = '.')

#We delete default help command
client.remove_command('help')


#answers with the ms latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')


#Embeded help with list and details of commands
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='.ping', value='Returns bot respond time in milliseconds', inline=False)
    embed.add_field(name='.quote', value='Get inspired by a powerful quote', inline=False)
    await ctx.send(embed=embed)


#Answers with a random quote
@client.command()
async def quote(ctx):
    responses = open('quotes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')

#react to any message that contains 'drama'
@client.event
async def on_message(ctx):
    if 'drama' in ctx.content:
        emoji = '\N{EYES}'
        await ctx.add_reaction(emoji)

print("Bot is ready!")
client.run(TOKEN)