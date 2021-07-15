import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix = '$')
count = 0

@client.event
async def on_ready():
	print('Online')

@client.command()
async def ping(ctx):
	await ctx.send(f'**Pong!**: {round(client.latency * 1000)}ms')

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'User {member} has been kicked!')

@kick.error
async def kick_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('You don\'t have permission to do that.')
	else:
		await ctx.send('Something went wrong.')

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason='No reason given'):
	await member.ban(reason=reason)
	await ctx.send(f'User {member} has been banned for: {reason}!')

@ban.error
async def ban_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('You don\'t have permission to do that.')
	else:
		await ctx.send('Something went wrong.')

@client.command()
@has_permissions(ban_members=True)
async def unban(ctx, user : discord.User):
	await ctx.guild.unban(user=user)
	await ctx.send(f'{user} unbanned')

file = open("TOKEN.txt","r")
TOKEN = file.read() # This stores the token in a text file so I do not have to release the token publicly.
file.close()
client.run(TOKEN)
