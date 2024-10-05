import discord, random, os
from discord.ext import commands
from logicbot import howyou, coin, howprocent, get_duck_image_url, get_dog_image_url

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
@bot.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command()
async def ITmem(ctx):
    path = os.path.abspath('ITmeme')
    memes_list = os.listdir('ITmeme')
    meme = random.choice(memes_list)
    meme_path = os.path.join(path,meme)
    print(f'Путь к мему {meme_path}')
    with open(meme_path, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def HISmem(ctx):
    path = os.path.abspath('HISmeme')
    memes_list = os.listdir('HISmeme')
    meme = random.choice(memes_list)
    meme_path = os.path.join(path,meme)
    print(f'Путь к мему {meme_path}')
    with open(meme_path, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def ANYMALmem(ctx):
    path = os.path.abspath('ANYMALmeme')
    memes_list = os.listdir('ANYMALmeme')
    meme = random.choice(memes_list)
    meme_path = os.path.join(path,meme)
    print(f'Путь к мему {meme_path}')
    with open(meme_path, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url) 
     
bot.run('Токен сюда')
