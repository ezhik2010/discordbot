import discord, random
from discord.ext import commands
from logicbot import howyou, coin, howprocent

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} забрел на этот сервер {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def howareyou(ctx):
    dela = howyou()
    await ctx.send(dela)

@bot.command()
async def flipcoin(ctx):
    await ctx.send(coin())

@bot.command()
async def howprocents(ctx):
    await ctx.send(howprocent())
     
bot.run('Токен сюда')
