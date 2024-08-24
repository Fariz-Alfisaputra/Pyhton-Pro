import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open('images/heart.png', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)   
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def organic(ctx):
    await ctx.send(f'you can start by composing waste, having a healthy diet and eat your meal before it starts moulding')

    
#f = open('text.txt', 'r', encoding='utf-8')
#text = f.read()
#print(text) 
#f.close()

# Dan inilah cara kita dapat menulis ulang keseluruhan file teks
#f = open('text.txt', 'w', encoding='utf-8')
#text = 'New text'
#f.write(text)
#f.close()



    
bot.run("token discord")
