import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('Ready')
    await client.change_presence(activity=discord.Game(name="bread-bank.jimdosite.com"))

@client.event   
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await channel.send(f"Welcome {member.mention} to the Bread Bank server")
    role = discord.utils.get(member.guild.roles, name="Bread Supporter")
    await member.add_roles(role)
    print('joined')
client.run('')
