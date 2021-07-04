import os
import discord
import embeds
import yaml
import random
import configs
import asyncio
import os
import html5lib
import json
import shutil
import urllib.request
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import string
import challonge
from discord.utils import get

intents = discord.Intents.default()
intents.members = True

PREFIX = configs.PREFIX
TOKEN = 'ODUxOTEyNjI5ODk4MzEzNzM1.YL_Ldg.6tvIBgHtflibESYOrunVPxsjBW4'
client = commands.Bot(command_prefix=PREFIX, intents = intents)
allintents = intents = discord.Intents.all()
SHUURL = 'https://asenshu.com'
taVeEnabled = False
activeDebate = False
chars = string.ascii_letters

with open(r'data.yaml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    if data['taVeEnabled'] == True:
        taVeEnabled = True
        print("TaVe was enabled, keeping it that way.")
    else:
        taVeEnabled = False
        print("TaVe was disabled, keeping it that way.")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.remove_command("help")


@client.command(name='introduction')
async def introduction(ctx):
    await ctx.send("Hey!", embed = embeds.introductionEmbed)

@client.command(name = 'help')
async def help(ctx):
    await ctx.reply(embed = embeds.helpEmbed)

@client.command(pass_context = True)
async def faq(ctx, userinput=None):
    if userinput is None:
        await ctx.reply(embed = embeds.faqEmbed)
    else:
        await ctx.reply(getattr(embeds, userinput.lower()))

@client.listen()
async def on_message(message):
    if taVeEnabled:
        if (message.content).lower() == "he":
            await message.reply(content = "ta ve.", delete_after = 15, mention_author = True)
            print(f"Ja vura {message.author}")
            print(message.content)
        elif (message.content).lower() == "h":
            await message.reply(content = "ta v.", delete_after = 15, mention_author = True)
            print(f"Ja vura {message.author}")
        elif (message.content).lower() == "hë":
            await message.reply(content = "ta vë.", delete_after = 15, mention_author = True)
            print(f"Ja vura {message.author}")
        else:
            pass
    else:
        pass

    if (message.content).lower() == "crop your memes":
        scissorsImg = discord.File('./assets/scissors.png')
        await message.reply("Ja po i jap un nje pale gershere", file = scissorsImg)

    if (message.content).lower() == "asenshu bot na thuaj konkluzionin":
        await message.reply("Konkluzioni eshte qe Ramses esht kokrra simpit.")

    if (message.content).lower() == "o asenshu bot do hentai ky":
        await message.reply(embed = embeds.doHentai)

#    if (message.author.name) == "Berlin":
#        await message.reply("Ka Fol.")
#    elif (message.author.name) == "sindi" and message.content.lower() == "yems":
#        await message.reply("Kopjuse")

    if (message.content).lower() == "bilbilush":
        image = discord.File('./assets/bilbilushi.jpg')
        await message.reply("look at this ||ugly|| cutie", file = image)

    if (message.channel.id == configs.debatChannel) and (message.author.name != "Asenshu Bot") and (message.content.startswith("Opinion: ")):
        await message.add_reaction(emoji = '⬆️')
        await message.pin


@client.command('pussy')
async def pussy(ctx):
    await ctx.reply('I kemi vec te vizatuara po hidhi nje sy njehere: https://hasenshu.com')

@client.command('dick')
async def dick(ctx):
    await ctx.reply("That's gay bro.")

@client.command('faqet')
async def faqet(ctx):
    await ctx.reply(embed = embeds.faqetEmbed)

@client.command('hentai')
async def hentai(ctx):
    await ctx.reply(embed = embeds.hentaiEmbed)

@client.command(pass_context = True)
@commands.has_permissions(manage_guild = True)
async def toggle(ctx, userinput=None, taVeEnabled=taVeEnabled):
    print(userinput)
    if userinput == None:
        await ctx.reply(embed = embeds.toggleEmbed)

    elif userinput == 'taVe':
        if taVeEnabled == False:
            taVeEnabled == True
            await ctx.reply('Enabled command "ta ve"')
        elif taVeEnabled == True:
            taVeEnabled == False
            await ctx.reply('Disabled command "ta ve"')
    elif userinput == 'taVe off':
        taVeEnabled = False
        await ctx.reply('Disabled command "ta ve"')
    elif userinput == 'taVe on':
        taVeEnabled = True
        await ctx.reply('Enabled command "ta ve"')


@client.command(name = 'simp')
async def simp(ctx, userinput = None):
    if userinput == None:
        message = await ctx.reply(f'A eshte {ctx.author.mention} simp?')
        await message.add_reaction(emoji = '⬆️')
        await message.add_reaction(emoji = '⬇️')
    else:
        message = await ctx.reply(f'A eshte {userinput} simp?')
        await message.add_reaction(emoji = '⬆️')
        await message.add_reaction(emoji = '⬇️')


@client.command(name = 'zegz')
async def zegz(ctx):
    await ctx.reply('shhhhh kalo dms...')
    await ctx.author.send("Zegz.")
    await ctx.author.send(f"{random.choice(embeds.lewdGIFS)}")

@client.command(name = 'randompic')
async  def randompic(ctx):

    urls = json.loads(open('links.json').read())
    base_url = 'https://prnt.sc/' #random letters will be put after this url, this url doesn't change
    random_letters = ''.join(random.choice(chars) for i in range(6)) #choses 6 random letters
        #checks if generated url is already used, if not then append it to the used list (urls)
        #then import the list in links.json file
        #if it's a duplicate it generates a new one and stores it in the list and imports it as well.
    if random_letters not in urls:
        urls.append(random_letters.lower())
        jsonList = json.dumps(urls)
        with open("links.json", "w") as dataFile:
            dataFile.write(jsonList)
        print("New URL.")
    else:
        print("Duplicate URL, regenerating...")
        random_letters = ''.join(random.choice(chars) for i in range(6))
        urls.append(random_letters.lower())
        jsonList = json.dumps(urls)
        with open("links.json", "w") as dataFile:
            dataFile.write(jsonList)

    url = base_url + random_letters.lower() #full orl to be used
    await ctx.send(url)

@client.command(name = 'kafe')
async def kafe(ctx, arg1 = None, arg2 = None, arg3 = None):
    if arg1 == None:
        kafe = random.choice(embeds.kafeList)
        await ctx.reply(f'Nje kafe per ty!', file = kafe)
    elif arg1 != None and arg2 != None and arg3 != None:
        kafe = random.choice(embeds.kafeList)
        await ctx.reply(f"Nje kafe per {ctx.author.mention} po vje prit nja 2 min.")
        await ctx.send(f"o {arg1}, {arg2}, {arg3} te ftoi {ctx.author.mention} per kafe, pranoje me {PREFIX}pranojekafen (shto edhe prapa llojin e kafes po deshe).")
        await ctx.send(file = kafe)
    elif arg1 != None and arg2 != None:
        kafe = random.choice(embeds.kafeList)
        await ctx.reply(f"Nje kafe per {ctx.author.mention} po vje prit nja 2 min.")
        await ctx.send(f"o {arg1}, {arg2} te ftoi {ctx.author.mention} per kafe, pranoje me {PREFIX}pranojekafen (shto edhe prapa llojin e kafes po deshe).")
        await ctx.send(file = kafe)
    else:
        kafe = random.choice(embeds.kafeList)
        await ctx.reply(f"Nje kafe per {ctx.author.mention} po vje prit nja 2 min.")
        await ctx.send(f"o {arg1} te ftoi {ctx.author.mention} per kafe, pranoje me {PREFIX}pranojekafen (shto edhe prapa llojin e kafes po deshe).")
        await ctx.send(file = kafe)

@client.command(name = 'pranojekafen')
async def pranojekafen(ctx, *, userinput = None):
    if userinput == None:
        await ctx.reply(f"Ju befte mire!")
    else:
        await ctx.reply(f"Ta bera kafen {userinput}, ju beft mire.")

@client.command(name = 'pp')
async def pp(ctx, userinput = None):
    massivePPSign = random.randint(1, 100)
    massivePPConfirm = random.randint(1, 100)
    if userinput == None:
        size = random.randint(1, 10)
        print(f"{ctx.author} dick is {size} / 10 long.")
        if massivePPConfirm != massivePPSign:
            await ctx.reply(f"Your dick size is this long: 8{'='*size}D")
            randomTipNr = random.randint(1, 40)
            if randomTipNr == 19:
                await ctx.send("Fakt Interesant: Egziston nje shanc 1 ne 100 qe te qelloje Super Big Massive Shlong.")
        elif massivePPConfirm == massivePPSign:
            await ctx.send(embed = embeds.massivePPEmbed)
    else:
        size = random.randint(1, 20)
        if massivePPConfirm != massivePPSign:
            await ctx.reply(f"{userinput} dick size is this long: 8{'='*size}D")
        elif massivePPConfirm == massivePPSign:
            await ctx.send(embed = embeds.massivePPEmbed)

@client.command(name = "amogus")
async def amogus(ctx, userinput = None, arg2 = None):
    if userinput == None and arg2 == None:
        await ctx.reply("PAM PAM PAM PAM!")
        await ctx.send('https://cdn.discordapp.com/attachments/630456160230834204/856966895705522236/AMOGUS.mp4')
    elif userinput == "drip":
        await ctx.reply("A M O G U S, ")
        await ctx.send("https://cdn.discordapp.com/attachments/680928395399266314/847236551607976016/video0.mp4")
    elif userinput == "sus" and arg2 != None:
        await ctx.send(f"{ctx.author.mention} SAYS {arg2} IS SUS!!")

@client.command(name = "faekban")
async def fakeban(ctx, userinput = None):
    author = ctx.author.mention
    await ctx.send(embed = embeds.fakeBanEmbed(ctx, userinput, author))

@client.command(name = "fakt")
async def fakte(ctx, arg1 = None, userinput = None):
    if userinput == "pavlefshem":
        await ctx.send(random.choice(embeds.fakteTePavlefshme))
    elif userinput == "vlefshem":
        await ctx.reply("S'kemi ashtu, vetem me te pavlefshme jemi ne stock.")
    elif userinput == None and arg1 == None:
        await ctx.reply("Ka Fol.")

try:
    @client.command(name = 'hapdebat')
    @commands.has_permissions(manage_guild = True)
    async def debat(ctx, time, *, theme):
        guild = client.get_guild(configs.guildID)
        everyoneRole = guild.get_role(configs.senshuRole)
        opinionistRole = guild.get_role(configs.opinionistRole)
        debatChannel = client.get_channel(configs.debatChannel)
        debatLeaderboard = client.get_channel(configs.debatLeaderboard)
        author = ctx.author.name
        time = int(time)
        await debatChannel.purge()
        print("Opening debate channel for everyone...")
        await debatChannel.set_permissions(everyoneRole, read_messages = True, send_messages = True, add_reactions = False)
        print("Debate Channel opened for everyone to read.")
        await ctx.reply(f"{opinionistRole.mention}", embed = embeds.debatEmbed(author, theme, time, debatChannel.mention))
        await debatChannel.send(embed = embeds.debatChannelEmbed(author, theme, time))
        print(f'Async Sleeping.')
        await asyncio.sleep(60*time)
        await debatChannel.set_permissions(everyoneRole, read_messages = False, send_messages = False, view_audit_log = False)
        print("Closed debate channel for everyone")
        openedDebate = False
        messages = await debatChannel.history().flatten()
        votes = []
        votesDict = {}
        for message in messages:
            start = "Opinion: "
            if message.content.startswith(start):
                for reaction in message.reactions:
                    votesDict[message.content] = reaction.count - 1
        await debatChannel.purge()
        sortedVotes = sorted(votesDict.items(), key=lambda x: x[1], reverse=True)
        print(sortedVotes)
        topMessages = ""
        try:
            for j in range(3):
                value = sortedVotes[j]
                message = value[0]
                votes = value[1]
                topMessages += f'Opinioni Numer {j + 1}: "{message}" me {votes} vota.\n'
            await debatLeaderboard.send(embed = embeds.debatResultsEmbed(topMessages, theme))
        except IndexError:
            print("Index Error")

        except:
            print("Some error happened.")

except:
    print("S'ke te drejta ta perdoresh kete komande.")


@client.command(name = 'temedebati')
async def temedebati(ctx, *, args = None):
    if args == None:
        await ctx.reply("Shkruaj pra dicka...")
    else:
        staffChannel = client.get_channel(850298962387664896)
        await staffChannel.send(embed = embeds.temedebati(args, ctx.author.name))
        await ctx.reply("Tema u dergua tek staffi si sugjerim.")

@client.command(name = 'createtour')
@commands.has_permissions(manage_guild = True)
async def createtour(ctx, role : discord.Role, categoryName):
    GUILD = ctx.guild
    members = role.members
    categoryChannel = await GUILD.create_category(f" ▬▬▬▬{categoryName}▬▬▬▬")
    x = 0
    membersdowntwo = int(len(members) / 2)
    print(membersdowntwo)
    print(members)

    await ctx.send(f"Numri i pjesemarresve: {len(members)}")

    if (len(members)  % 2) == 0:
        print("all members in tournament")
    else:
        await ctx.send(f"Numer pjesetaresh tek: nje person do mbetet jashte.")
    fullBracket = f"""
    -==- PJESETARET E TOURNAMENTIT {categoryName} -==-
    """
    membersIn = []
    for member in range(membersdowntwo):
        member1 = members[x]
        print(member1)
        member2 = members[x+1]
        print(member2)
        GUILD = ctx.guild
        everyoneRole = GUILD.get_role(configs.senshuRole)
        textChannel = await categoryChannel.create_text_channel(f"{member1.name}-and-{member2.name}")
        await textChannel.send(embed = embeds.tournamentEmbed(categoryName, member1, member2))
        await textChannel.send(content = f"{member1.mention} {member2.mention}", delete_after = 2)
        membersIn.append(member1)
        membersIn.append(member2)
        await textChannel.set_permissions(everyoneRole, send_messages = False, read_messages = False)
        await textChannel.set_permissions(member1, send_messages = True, read_messages = True)
        await textChannel.set_permissions(member2, send_messages = True, read_messages = True)
        x += 2
        fullBracket += f"{member1} dhe {member2}\n"
    await ctx.reply(fullBracket)

    await ctx.send(f"Lojtare te mbetur jashte: {members - membersIn}")



@client.command(name = 'musicquizz')
@commands.has_permissions(manage_guild = True)
async def musicquizz(ctx,nrofsongs, genre, role : discord.Role, delay):

    d = {}

    voiceChannel = await ctx.author.voice.channel.connect()
    musics = os.listdir('./musics')

    author = ctx.author
    delay = int(delay)
    await ctx.send(f"{role.mention} shpejt!", embed = embeds.quizzEmbed(author, nrofsongs, genre, delay))

    await asyncio.sleep(delay*60)
    quizzStart = discord.Embed(title = '', description = 'Quizzi Filloi!')
    await ctx.send(embed = quizzStart)
    songNum = 0
    for i in range(int(nrofsongs)):

        song = musics[songNum]
        songg = musics[songNum]
        song = songg.replace('.mp3', '')
        songList = song.split('-')
        author = songList[0]
        title = songList[1]
        voiceChannel.play(discord.FFmpegPCMAudio(f"./musics/{songg}"), after=lambda e: print("Song done!"))
        voiceChannel.source = discord.PCMVolumeTransformer(voiceChannel.source)
        voiceChannel.source.volume = 1

        playingSong = discord.Embed(title = '', description = 'Gjeni kengen qe po degjoni, 1 minute kohe!!')
        await ctx.send(embed = playingSong)

        def check1(m: discord.Message):
            return (m.content).lower() == author.lower()

        def check2(m: discord.Message):
            return (m.content).lower() == title.lower()

        L = []
        L = await asyncio.gather(
        client.wait_for(event = 'message', check = check1, timeout = 60.0),
        client.wait_for(event = 'message', check = check2, timeout = 60.0),
        return_exceptions=True)
        authorr = L[0]
        titlee = L[1]

        Error = asyncio.TimeoutError
        x = isinstance(authorr, Error)

        print(f"""X: {x}""")
        y = isinstance(titlee, Error)
        print(f"""Y: {y}""")

        if ((isinstance(L[0], Error)) == True) and ((isinstance(L[1], Error)) == False):
            print("Author wasn't found, only title.")
            print(f"Author was found by: {L[1].author.mention}")
            quizz = discord.Embed(title = '', description = f"Titulli:{title}\nKengetari:{author}\nVetem kengetari u gjet nga {L[1].author.mention}")
            await ctx.send(embed = quizz)
            username = L[1].author.name
            points = 1
            variable = d.get(username)
            if isinstance(variable, int) == False:
                variable = 0
            d1 = {username : points + variable}
            d.update(d1)
            print(d)

        elif ((isinstance(L[1], Error)) == True) and ((isinstance(L[0], Error)) == False):
            print("Title wasn't found, only author.")
            print(f"Title was found by: {L[0].author.mention}")
            quizz = discord.Embed(title = '', description = f"Titulli:{title}\nKengetari:{author}\nVetem titulli u gjet nga {L[0].author.mention}")
            await ctx.send(embed = quizz)

            username = L[0].author.name
            points = 1
            variable = d.get(username)
            if isinstance(variable, int) == False:
                variable = 0
            d1 = {username : points + variable}
            d.update(d1)
            print(d)

        elif ((isinstance(L[1], Error)) == True) and ((isinstance(L[1], Error)) == True):
            quizz = discord.Embed(title = '', description = f"Titulli:{title}\nKengetari:{author}\nAskush s'gjeti asgje.")
            await ctx.send(embed = quizz)
        elif ((isinstance(L[1], Error)) == False) and ((isinstance(L[1], Error)) == False):
            print(f"Title was found by: {L[0].author.mention}")
            print(f"Author was found by: {L[1].author.mention}")
            quizz = discord.Embed(title = '', description = f"Titulli:{title}\nKengetari:{author}\nKengetari u gjet nga {L[1].author.mention}\nTitulli u gjet nga {L[0].author.mention}")
            await ctx.send(embed = quizz)
            username = L[1].author.name
            points = 1
            variable = d.get(username)
            if isinstance(variable, int) == False:
                variable = 0
            d1 = {username : points + variable}
            d.update(d1)
            print(d)

            username = L[0].author.name
            points = 1
            variable = d.get(username)
            if isinstance(variable, int) == False:
                variable = 0
            d1 = {username : points + variable}
            d.update(d1)
            print(d)
        else:
            print("\n\n\nLoop didn't work\n\n\n")

        songNum += 1
        voiceChannel.stop()

    await ctx.send(d)
    d = {}

client.run(TOKEN)
