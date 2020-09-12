import discord
from discord.ext import commands, tasks
import os
import B
import asyncio
import random
import time
import requests
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
coin = ["Heads", "Tails", "Heads", "Tails", "Heads", "Tails", "Heads", "Tails", "HA! The coin fell off the table! No one wins! (or loses....)"]
flip = coin[random.randint(0, 8)]
key=os.getenv('key')
wkey=os.getenv('wkey')
client = discord.Client()
client = commands.Bot(command_prefix = '+')
client.remove_command('help')

async def status_task():
    while True:
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name=" 𝘵𝘩𝘦 𝘤𝘰𝘮𝘮𝘢𝘯𝘥:"))
        await asyncio.sleep(4)
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name=" +help"))
        await asyncio.sleep(6)
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name=" 𝘢 𝘸𝘰𝘳𝘬 𝘪𝘯 𝘱𝘳𝘰𝘨𝘳𝘦𝘴𝘴 🔧"))
        await asyncio.sleep(3)
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name=" 𝘣𝘶𝘵 𝘐 𝘩𝘰𝘱𝘦 𝘺𝘰𝘶"))
        await asyncio.sleep(3)
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name=" 𝘭𝘪𝘬𝘦 𝘪𝘵! 😊🥰"))
        await asyncio.sleep(3)
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name=" 𝘤𝘰𝘥𝘦𝘥 𝘣𝘺:"))
        await asyncio.sleep(3)
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.playing, name=" Mini#1146"))
        await asyncio.sleep(5)

@client.event
async def on_ready():
    print('Logged in as:')
    print("Username:",client.user.name+" #9354")
    print("Client ID:",client.user.id)
    print("Bot Creator: Mini#1146")
    print(current_time)
    print('-----------------------------')
    client.loop.create_task(status_task())

@client.command()
async def parrot(ctx,*, mssg=None):
  if mssg == None:
    embed = discord.Embed(title="🦜 Parrot Blink", color=0xE64885)
    embed.add_field(name="Slight Problem...", value='hmm whattya want me to copy?')
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(title="🦜 Parrot Blink", color=0x489AE6)
    embed.add_field(name="now gimme cracker pls 🍘", value=f'{mssg}')
    await ctx.send(embed=embed)

@client.command()
async def reverse(ctx,*, mssg=None):
  if mssg == None:
    embed = discord.Embed(title="🔄 Reverse that!", color=0xE64885)
    embed.add_field(name="hmmm", value='gimme something to reverse!')
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(title="🔄 Reverse that!", color=0x3258BF)
    embed.add_field(name="Pop poP", value=f'{mssg}'[::-1])
    await ctx.send(embed=embed)

@client.command()
async def dice(ctx):
    await ctx.send(embed=discord.Embed(title="You 🎲 Roll", description=f"You rolled {random.randint(1,6)}!", color=0x3258BF))





@client.command()
async def favsong(ctx):
  fs = [
        'https://open.spotify.com/track/1jjFmyLBPVocWR0bDRtBoE?si=P6NtOLajRVOCqm_bmdPerw',
        'https://open.spotify.com/track/3yOlyBJuViE2YSGn3nVE1K?si=Nr6cLTjMSj2x5bxAwz6DqA',
        'https://open.spotify.com/track/6igsoAR6Co9u7Rq3U7mlOD?si=33WBt4byQF2i9GwRjy4unA',
        'https://open.spotify.com/track/0ct6r3EGTcMLPtrXHDvVjc?si=CbIVis4wQDuz7HYc61p4MQ',
        'https://open.spotify.com/track/6sy3LkhNFjJWlaeSMNwQ62?si=vFbjgjZORqmJ7rp3FH0iPA',
        'https://open.spotify.com/track/3j9o0zUoyGNXkijNSyRyBI',
        'https://open.spotify.com/track/1RKZvaLj3UPhGjZkaIrFm7',
        'https://open.spotify.com/track/3BVgrFWuH01GmCUy9Y2EE8',
        'https://open.spotify.com/track/1qE47wUKG2juJwPoLqg4C9'
    ]
  fs1 = random.choice(fs)
  await ctx.send(fs1)

@client.command()
async def about(ctx):
  embed = discord.Embed(title="All about Blink !!", color=0x7100FF)
  embed.add_field(name="I am Mini's favored creation 😋", value="**Bot Name:** Blink#9354\n**Creator:** Mini#1146\n**Programming Language:** Python 3.8\n**Date Created:** June 14th, 2020 | 19:45PM\n **Purpose:** it's a fun bot, so it doesn't use moderation, and is still in the making, but hopefully  Blink adds a passive, customized feel to any server that it is in!\nIt can do very basic stuff, but if you want more features, DM 'Mini#1146', I'm always open to some nice feedback!(school sucks)")
  await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
  embed = discord.Embed(title="❗ Error ❗", color=0xA90000)
  embed.add_field(name="Uh oh...", value=f'{error}')
  await ctx.send(embed=embed)

@client.command()
async def greeting(ctx):
  gr = [
        'I\'m a Blink bot 😜',
        'Ayyyeeee! Thanks for asking! Pretty gud!',
        'Could never have been better than this!',
        'How about you? lol how YOU doin\' today?',
        'Awww 🥰 you are a very nice person',
        'today is gonna be great 🥳',
        'doin\' good',
        'thanks for asking lolololol',
        'hmmmmmm.... yeaaaaa',
        '😆😆 hahahaha yea!',
        '🤭aww you didn\'t have to ask... thanks!',
        'i could use a nap right now...💤',
        'nooo 😖 your too nice!',
        'pretty good, thanks 😘',
        '🥕 CARROT 🥕',
        '🥕 CARROT 🥕'
    ]
  gr1 = random.choice(gr)
  embed = discord.Embed(title="Hello Blink!", color=0xBD9EFF)
  embed.add_field(name="How are you today?", value=gr1)
  await ctx.send(embed=embed)

@client.command()
async def time(ctx):
    embed = discord.Embed(title="⌚ Time in Coordinated Universal Time", color=0x575353)
    embed.add_field(name="Time (UTC):", value=current_time)
    await ctx.send(embed=embed)

@client.command()
async def rate(ctx):
  ra = [
        'You are a very nice member here 😊',
        'This is an exquisite server 👌',
        'I ',
        'How about you? lol how YOU doin\' today?',
        'Awww 🥰 you are a very nice person',
        'today is gonna be great 🥳',
        'doin\' good',
        '😌 feelings of serenity'
    ]
  ra1 = random.choice(ra)
  await ctx.send(ra1)

@client.command()
async def grade(ctx):
  gr = random.randint(1,100)
  if gr < 50:
    embed = discord.Embed(title="📝 You take a test and...", color=0xFF4242)
    embed.add_field(name="YOU FAILED!!", value=gr)
    await ctx.send(embed=embed)
  elif gr < 70 and gr > 51:
    embed = discord.Embed(title="📝 You take a test and...", color=0xFF7542)
    embed.add_field(name="Lol your baaaaddd 🤣", value=gr)
    await ctx.send(embed=embed)
  elif gr < 90 and gr > 71:
    embed = discord.Embed(title="📝 You take a test and...", color=0xFFBD42)
    embed.add_field(name="you did quite average", value=gr)
    await ctx.send(embed=embed)
  elif gr < 99 and gr > 91:
    embed = discord.Embed(title="📝 You take a test and...", color=0x82FF42)
    embed.add_field(name="ayyeee you did sweet!", value=gr)
    await ctx.send(embed=embed)
  elif gr == 100:
    embed = discord.Embed(title="📝 You take a test and...", color=0x9B42FF)
    embed.add_field(name="YOU GOT A HUNDRED!!! 🥳", value=gr)
    await ctx.send(embed=embed)

@client.command()
async def flip(ctx):
  coin = ["Heads", "Tails", "Heads", "Tails", "Heads", "Tails", "Heads", "Tails", "Fish"]
  flip = coin[random.randint(0, 8)]
  await ctx.send("I hope you betted beforehand! 😋")
  await asyncio.sleep(2)
  await ctx.send("Flipping...")
  await asyncio.sleep(3)
  await ctx.send("Okay, the flip is in! The Dollar says:")
  await asyncio.sleep(1)
  await ctx.send(flip)

@client.command()
async def bruh(ctx):
  br = [
        'https://cdn.discordapp.com/attachments/717091288251629598/717827811687137341/me.mp4',
        'https://cdn.discordapp.com/attachments/719239789697826898/721073269129740359/101890153_248962729760113_3464118493226686893_n.mp4',
        'https://cdn.discordapp.com/attachments/719239789697826898/721073207209230336/95563224_2683927415176024_8788060489491534796_n.mp4',
        'https://cdn.discordapp.com/attachments/719239789697826898/721073895364624475/video0.mov',
        'https://cdn.discordapp.com/attachments/719239789697826898/721074158288764948/fat_nigga.mp4',
        'https://media.discordapp.net/attachments/719239789697826898/721083240097644625/image0.png?width=258&height=459'
    ]  
  br1 = random.choice(br)
  embed = discord.Embed(title="🤨 What the...", color=0xFFFB6E)
  embed.add_field(name="Here is some \"bruh\" for you", value=br1)
  await ctx.send(embed=embed)

@client.command()
async def corny(ctx):
  co = [
        'What is the best day to go to the beach? Sunday, of course!',
        'What bow can\'t be tied? A rainbow!',
        'How does a dog stop a video? By hitting the paws button!',
        'What did one toilet say to the other? You look flushed.',
        'A cement mixer and a prison bus crashed on the highway. Police advise citizens to look out for a group of hardened criminals',
        'It\'s always windy in a sports area. All those fans',
        'What is worse than raining cats and dogs? Hailing taxis!',
        'I used to be addicted to not showering. Luckily, I\'ve been clean for five years.',
        'How does a farmer mend his overalls? With cabbage patches.',
        'What did the big flower say to the little flower? Hi bud!',
        'How many tickles does it take to get an octopus to laugh? Ten tickles.',
        'I couldn\'t figure out why the baseball kept getting bigger. Then it hit me.',
        'Why does Humpty Dumpty love autumn? Because he always has a great fall.',
        'Where do hamburgers take their sweethearts on Valentine\'s Day to dance? The Meat Ball!',
        'What time does a duck wake up? The quack of down.',
        'Some people eat snails. They must not like fast food.',
        'What happens to a frog\'s car when it breaks down?\nIt gets toad away.',
        'What did the duck say when it bought lipstick?\n"Put it on my bill."',
        ' What do you call two monkeys that share an Amazon account?\nPrime mates.',
        'Whew, this is Mini#1146 here, the creator of this bot. You just got saved from seeing a bunch of cringy jokes I stole from some "clean" websites 🤣🤣'
    ]
  co1 = random.choice(co)
  embed = discord.Embed(title="🌽 Corny Jokes", color=0xC9FF92)
  embed.add_field(name="Ahhhh so corny!", value=co1)
  await ctx.send(embed=embed)

@client.command()
async def facts(ctx):
  fa = [
        'Did you know that when ants die, they let off a unique stench only other ants can smell, and they will be attracted to the dead ant, and carry him away?',
        'Did you know that Concorde, that supersonic plane, can burn as much fuel as the average car burns in a month, just by taxi\'ing towards the runway?'
    ]  
  fa1 = random.choice(fa)
  embed = discord.Embed(title="📔Random Facts", color=0xFFB694)
  embed.add_field(name="Here's a random fact 😋", value=fa1)
  await ctx.send(embed=embed)

@client.command()
async def invite(ctx):
  embed = discord.Embed(title="Invite Blink! :partying_face:  ", description="Heyyyy thank you sooo much, for requesting to invite me to your server :smiling_face_with_3_hearts:! It will be a great pleasure of mine to bring that small sprinkle of comedy to your channel, and you won't regret this!:yum:\n [Invite Here!](https://discord.com/api/oauth2/authorize?client_id=710903521284980818&permissions=8&scope=bot)", color=0x8F40FF)
  await ctx.send(embed=embed)

@commands.cooldown(1, 3600, commands.BucketType.user)
@client.command()
async def sushi(ctx):
  sushi = random.randint(100, 300)
  embed = discord.Embed(title="Work for that sushi! 😋", color=0xCF2A40)
  embed.add_field(name="**🍣 Sushi you earned 🍣**", value=sushi)
  await ctx.send(embed=embed)

@client.command()
async def meme(ctx):
    url = 'https://some-random-api.ml/meme'
    result_url = requests.get(url)
    resultjson=result_url.json()
    embed=discord.Embed(title=resultjson['caption'], colour=discord.Colour.purple())
    embed.set_image(url=resultjson['image'])
    embed.set_footer(text=f"Category: {resultjson[ 'category']}")
    await ctx.send(embed=embed)

@client.command()
async def cat(ctx): 
    url = 'https://some-random-api.ml/img/cat'
    result_url = requests.get(url)
    resultjson=result_url.json()
    embed=discord.Embed(title="here is cat", description="cat", 
    colour=discord.Colour.green())
    embed.set_image(url=resultjson['link'])
    embed.set_footer(text=f"a amazing good cat")      
    await ctx.send(embed=embed)

@client.command()
async def dog(ctx): 
    url = 'https://some-random-api.ml/img/dog'
    result_url = requests.get(url)
    resultjson=result_url.json()
    embed=discord.Embed(title="here is dog", description="dog", 
    colour=discord.Colour.green())
    embed.set_image(url=resultjson['link'])
    embed.set_footer(text=f"a amazing good dog")      
    await ctx.send(embed=embed)

@client.command()
async def panda(ctx): 
    url = 'https://some-random-api.ml/img/panda'
    result_url = requests.get(url)
    resultjson=result_url.json()
    embed=discord.Embed(title="here is panda", description="panda", 
    colour=discord.Colour.green())
    embed.set_image(url=resultjson['link'])
    embed.set_footer(text=f"a amazing good panda")     
    await ctx.send(embed=embed)

@client.command()
async def fox(ctx): 
    url = 'https://some-random-api.ml/img/fox'
    result_url = requests.get(url)
    resultjson=result_url.json()
    embed=discord.Embed(title="here is fox", description="fox", 
    colour=discord.Colour.green())
    embed.set_image(url=resultjson['link'])
    embed.set_footer(text=f"a amazing good fox")     
    await ctx.send(embed=embed)

@client.command()
async def bird(ctx): 
    url = 'https://some-random-api.ml/img/birb'
    result_url = requests.get(url)
    resultjson=result_url.json()
    embed=discord.Embed(title="here is bird", description="bird", 
    colour=discord.Colour.green())
    embed.set_image(url=resultjson['link'])
    embed.set_footer(text=f"a amazing good bird")     
    await ctx.send(embed=embed)

@client.command()
async def red_panda(ctx): 
    url = 'https://some-random-api.ml/img/red_panda'
    result_url = requests.get(url)
    resultjson=result_url.json()
    embed=discord.Embed(title="here is red panda", description="red panda", 
    colour=discord.Colour.green())
    embed.set_image(url=resultjson['link'])
    embed.set_footer(text=f"a amazing good red panda")
    await ctx.send(embed=embed)

@client.command()
async def koala(ctx): 
     url = 'https://some-random-api.ml/img/koala'
     result_url = requests.get(url)
     resultjson=result_url.json()
     embed=discord.Embed(title="here is koala", description="koala", 
     colour=discord.Colour.green())
     embed.set_image(url=resultjson['link'])
     embed.set_footer(text=f"a amazing good koala")
     await ctx.send(embed=embed)

@client.command()
async def hug(ctx, member : discord.Member): 
     url = 'https://some-random-api.ml/animu/hug'
     result_url = requests.get(url)
     resultjson=result_url.json()
     embed=discord.Embed(title=f"{ctx.author.name} hugs {member.name}", colour=discord.Colour.green())
     embed.set_image(url=resultjson['link'])
     embed.set_footer(text=f"hugs")
     await ctx.send(embed=embed)


@client.command()
async def suggest(ctx, *, args):
    channel = client.get_channel(742371371312742490) #Replace with channel ID where suggestion embed will be sent :)
    embed = discord.Embed(title=f'Suggestion from {ctx.author.name}!', description=f'{args}')
    await channel.send(embed=embed)
    await ctx.send(f'Thanks for your feedback!')

@client.command()
async def help(ctx):
    embed = discord.Embed(title="🥳 Blink is here to have fun! 🥳", description="Choose an option below! This is a bot to have fun with, so... have fun!! 😁🤣", color=0x8F40FF)

    embed.set_footer(text='Blink#9354 | Mini#1146')



    embed.set_image(url='https://media1.tenor.com/images/24b4cf8512e58420d0cdfea3df5a3cce/tenor.gif?itemid=14432583')

    embed.add_field(name="👋Hey Blink! How are you?", value="+greeting")
    
    embed.add_field(name="🦜Parrot!", value="+parrot")

    embed.add_field(name="🔄Reverse Speak", value="+reverse")

    embed.add_field(name='🎲Roll Dice', value='+dice')

    embed.add_field(name="💵Flip a Dollar", value="+flip")

    embed.add_field(name="📝Test Grade", value="+grade")

    embed.add_field(name="🍣Get Sushi", value="+sushi")

    embed.add_field(name="🤨What the...", value="+bruh")

    embed.add_field(name="🌽Corny Jokes", value="+corny")

    embed.add_field(name="📔Random Facts", value="+facts")

    embed.add_field(name="📈Rate Stuff", value="+rate")

    embed.add_field(name="⌚Current Time (UTC)", value="+time")

    embed.add_field(name="🎶Blink's Favorites!", value="+favsong")

    embed.add_field(name="📚About Me!", value="+about")

    embed.add_field(name="📩Invite Me!", value="+invite")
    
    embed.add_field(name="🐱Get a picture of a cat!", value="+cat")

    embed.add_field(name="🐕Get a picture of a dog!", value="+dog")

    embed.add_field(name="🐼Get a picture of a panda!", value="+panda")

    embed.add_field(name="🦊Get a picture of a fox!", value="+fox")

    embed.add_field(name="🐦Get a picture of a bird!", value="+birb")

    embed.add_field(name="🎍Get a picture of a red panda!", value="+red_panda")

    embed.add_field(name="🐨Get a picture of a koala!", value="+koala")                                                   
    embed.add_field(name="🤣Get memes!", value="+meme")     

    embed.add_field(name="❓Suggest something!", value="+suggest")

    embed.add_field(name="❣️hug someone!", value="+hug")


    await ctx.send(embed=embed)


client.run(os.getenv('TOKEN'))
