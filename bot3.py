import discord
from discord.ext import commands

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
async def musor(ctx, *, musor_name):
    if "пластик" in musor_name:
        await ctx.send("Пластик нужно выбрасывать в урну")
    elif "стекл" in musor_name:
        await ctx.send("стекло нужно выбрвсывать в урну")
    elif "бум" in musor_name:
        await ctx.send("бумага нужно сдавать в мукатуры")
    elif "бата" in musor_name:
        await ctx.send("батарека нужно сдавать на переработку")
    
    else:
        await ctx.send("Я не знаю")
      
bot.run("")
