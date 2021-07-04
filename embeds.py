import discord
from discord.ext import commands
import configs

PREFIX = configs.PREFIX
client = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
allintents = intents = discord.Intents.all()
ASENSHUURL = 'https://asenshu.com'
ICON_URL = 'https://i.imgur.com/LVymnhK.png'
COLOR = 0x109319


introductionEmbed = discord.Embed(title = "Asenshu Bot©", url = ASENSHUURL, description="Boti Official Ne Discord!", color = COLOR )
introductionEmbed.set_author(name = 'Asenshu Bot', url = ASENSHUURL, icon_url = ICON_URL)
introductionEmbed.add_field(name = "Pershendetje!", value = "Ju paraqesim botin official te Asenshu ne DISCORD!", inline = False)
introductionEmbed.set_footer(text="Asenshu - All Rights Reserved®")


helpEmbed = discord.Embed(title = 'Ndihme', url = 'https://asenshu.com', description = '', color = COLOR)
helpEmbed.set_author(name = 'Asenshu Bot', url = ASENSHUURL, icon_url = ICON_URL)
helpEmbed.add_field(name = "Ndihme rreth komandave te Asenshu Bot!", value = f"""
{PREFIX}faqet -> Liston faqet e Asenshut.
{PREFIX}faq -> Shfaq komanda per FAQ (Frequently Asked Questions)
{PREFIX}help -> Shfaq kete qe po lexon tani.
{PREFIX}simp @user -> Hap votimet a eshte @user simp apo jo, lere bosh @user per veten.
{PREFIX}kafe -> Nje kafe per ty! Bej {PREFIX}kafe @user per te ftuar edhe shoke. (mund te ftosh maksimumi 3 shoke, s'kemi tavolina per me teper)
{PREFIX}randompic -> Dergon nje imazh random nga [ky script.](https://github.com/adornerz/lightshot-exploit)
{PREFIX}hapdebat -> Hap nje debat. Shembull: {PREFIX}hapdebat 30 a pi peshku uje? ku 30 eshte kohezgjatja ne minuta dhe pasohet nga tema e debatit.
{PREFIX}faekban -> fake ban. usage:  {PREFIX}faekban @user#1234
""", inline = False)

helpEmbed.add_field(name = "Amogus", value = f"""
{PREFIX}amogus -> A M O G U S. Nenkomandat:
        {PREFIX}amogus -> Bass Boosted Masterpiece
        {PREFIX}amogus drip -> Te tregon sensin me te larte rreth fashionit.
        {PREFIX}amogus sus @user -> @user#1230 IS SUS?!?@#?!

""", inline = False)
helpEmbed.add_field(name = "For hornies", value = f"""
{PREFIX}hentai -> Shows you the dark path.
{PREFIX}zegz -> Nje kohe e kenaqshme me botin.
{PREFIX}pp -> analizon sa tgjat e ke, 100% i sakte.
edhe ca qe duhet t'i gjesh vete.
""")
helpEmbed.set_footer(text="Asenshu - All Rights Reserved®")


faqetEmbed = discord.Embed(title = 'Faqet e Asenshu', url = 'https://asenshu.com', description = '', color = COLOR)
faqetEmbed.set_author(name = 'Asenshu Bot', url = ASENSHUURL, icon_url = ICON_URL)
faqetEmbed.add_field(name = "Lista e faqeve te Asenshu:", value = f"""
[Asenshu.com](https://asenshu.com) --> Faqja zyrtare e Asenshu ku ndodhet cdo anime e perkthyer nga ne.
[Hasenshu.com](https://hasenshu.com) --> Pjesa e erret e asenshut, faqja ku publikohen hentai me titra shqip.
""", inline = False)
faqetEmbed.set_footer(text="Asenshu - All Rights Reserved®")


hentaiEmbed = discord.Embed(title = 'Do Hentai e👀', url = 'https://hasenshu.com', description = '', color = COLOR)
hentaiEmbed.add_field(name = "Kemi kemi edhe ashtu...", value = "[shtyp ketu](https://hasenshu.com) po mos i thuaj njeriu.")


def debatEmbed(author, theme, time, channel):
    debatEmbed = discord.Embed(url = 'https://asenshu.com', description = '', color = COLOR)
    debatEmbed.add_field(name = 'Debat:', value = f'{author} hapi debatin me teme: "{theme}" per {time} minuta.\nShkoni tek kanali {channel} per te shprehur opinione dhe per votuar ne to.')
    return debatEmbed

def debatChannelEmbed(author, theme, time):
    debatChannelEmbed = discord.Embed(color = COLOR)
    debatChannelEmbed.add_field(name = 'Debati i hapur:', value = f'''
    Tema: {theme}.
    Koha: {time} minuta.
    Autori: {author}
    ''')
    debatChannelEmbed.set_footer(text = f"LEXONI DESCRIPTIONIN E CHANNELIT.")
    return debatChannelEmbed

def debatResultsEmbed(topMessages, theme):
    debatResults = discord.Embed(title = "Rezultatet e Debatit:", color = COLOR)
    debatResults.add_field(name = f'"{theme}"', value = f"Mesazhet me te votuara jane:\n{topMessages}")
    return debatResults

def temedebati(args, author):
    temeDebati = discord.Embed(title = f'{author} sugjeron per teme debati: ', description = f"{args}" )
    return temeDebati


def tournamentEmbed(theme, member1, member2):
    tournamentEmbed = discord.Embed(title = f"Tourmanenti i {theme}", color = COLOR)
    tournamentEmbed.add_field(name = f"Pershendetje!", value = f"""
    {member1.mention} dhe {member2.mention}, do te jeni kunder njeri tjetrit ne tournamentin e {theme}.
    Per kohen dhe detaje te tjera ju lutem prisni nje njoftim ne kanalin e njoftimeve te pergjithshme.
    Faleminderit per pjesemarrjen, dhe fitofte me i miri!""")
    tournamentEmbed.set_footer(text="Asenshu - All Rights Reserved®")
    return tournamentEmbed

def quizzEmbed(author, nrofsongs, genre, delay):
    quizzEmbed = discord.Embed(title = f'', color = COLOR)
    quizzEmbed.add_field(name = 'Quizz!', value = f'{author.mention} krijoi nje quizz muzike te llojit {genre} per {nrofsongs} kenge!\nQuizzi fillon per {delay} minuta!')
    return quizzEmbed

toggleEmbed = discord.Embed(title = 'Nenkomandat e Toggle', url = 'https://asenshu.com', description = '', color = COLOR)
toggleEmbed.set_author(name = 'Asenshu Bot', url = ASENSHUURL, icon_url = ICON_URL)
toggleEmbed.add_field(name = "TaVe:", value = f"""
{PREFIX}toggle TaVe -> Toggles TaVe on and off.
""", inline = False)
toggleEmbed.set_footer(text="Asenshu - All Rights Reserved®")

doHentai = discord.Embed(title = '', url = 'https://hasenshu.com', description = '', color = COLOR)
doHentai.add_field(name = "Ska.", value = "se bej shaka ka te [hasenshu](https://hasenshu.com) sa te doje")
doHentai.set_footer(text="Horny mfs...")


massivePPEmbed = discord.Embed(url = 'https://asenshu.com', description = '', color = COLOR)
massivePPEmbed.add_field(name = "Your PP so huge you unlocked the rare massive PP:", value = f"""
NO PP FOR U
""", inline = False)
massivePPEmbed.set_footer(text="YOU UNLOCKED THE MASSIVE PP!!!!!")

def fakeBanEmbed(ctx, user, author):
    BanEmbed = discord.Embed(url = "https://asenshu.com/", description = f"{author} banned {user}. They will be remembered.", color = COLOR)
    return BanEmbed



faqEmbed = discord.Embed(title = 'Asenshu FAQ', url = 'https://asenshu.com/faq/', description = 'Pyetje të Shpeshta rreth Asenshu.', color = COLOR)
faqEmbed.set_author(name = 'Asenshu Bot', url = ASENSHUURL, icon_url = ICON_URL)
faqEmbed.add_field(name = 'Frequently Asked Questions (FAQ)', value = 'FAQ janë te listuara tek faqja zyrtare e Asenshu, kliko [ketu](https://asenshu.com/faq/) për të shkuar tek faqja.', inline = False)
faqEmbed.add_field(name = 'Komandat:', value = f"[Për të lexuar FAQ këtu, provo komandën '{PREFIX}faq' e ndjekur nga fjala kryesore për më shumë informacion.](https://asenshu.com)", inline = False)
faqEmbed.add_field(name = 'Asenshu- Pyetje rreth Faqes', value = f"""
{PREFIX}faq kerko: Si mundemi ta kërkojmë Faqen e Asenshu?
{PREFIX}faq lloji: Çfarë lloj faqeje është Asenshu?
{PREFIX}faq koha: Kur u krijua Asenshu?
{PREFIX}faq pronesia: Në pronësi të kujt është Asenshu?
{PREFIX}faq viruse: Përmban faqja e Asenshu viruse qe janë të rrezikshme?
{PREFIX}faq rezolucioni: Pse për disa filma ose seriale ka një version HD dhe nuk ka një 480p ose anasjelltas?
{PREFIX}faq shkarko: Si mund t'i shkarkoj episodet në faqe?
{PREFIX}faq donato: Mundem të donatoj për faqen Asenshu?
{PREFIX}faq app: Ka Asenshu App?
{PREFIX}faq disqus: Çfarë është Disqus që del në faqe?
{PREFIX}faq animeawards: Organizon Asenshu, Anime Awards?""", inline = False)

faqEmbed.add_field(name = 'Asenshu- Pyetje Discord', value = f"""
{PREFIX}faq discordizyrtar: Ështe ky komuniteti zyrtar i faqes Asenshu?
{PREFIX}faq discordawards: Organizon komuniteti Asenshu Discord Award?
{PREFIX}faq aplikimstaffi: Dua të bëhem pjesë e stafit të Asenshu dhe të punoj për ju, kujt t'i drejtohem?
{PREFIX}faq partneritet: Kujt t'i drejtohem nëse dua të bëj Partneritet me ju?
{PREFIX}faq njoftime: Dua të marr njoftimet më të reja, njoftime rreth discordit, episodeve, filmave, votimeve dhe gjërave të tjera...
{PREFIX}faq turne: Kur do bëhet Turneu i radhës për Anime?
{PREFIX}faq risi: Do të sjellë Asenshu Anime të reja?
{PREFIX}faq sugjerim: Nëse e sugjeroj një anime a do e përktheni?
{PREFIX}faq mirupafshim: Do të mbyllet Asenshu???
{PREFIX}faq kur: Kur do të dalë X episodi i ri i një simulcats?
{PREFIX}faq kur2: Kur dalin episodet në përgjithësi?
""", inline =  False)
faqEmbed.set_footer(text="Asenshu - All Rights Reserved®")


kerko = "Asenshu është faqja më e madhe për anime shqip, mundeni thjesht ta kërkoni Asenshu, ose nëse doni direkt të shkoni tek faqja kërkoni asenshu.com"
lloji = """
Asenshu është Platforma më e madhe e Animeve në Shqipëri.
Asenshu është risi në Shqipëri. Ne sollëm të parët Animet nga Japonia me titra në Gjuhën Shqipe dhe tani jemi shërbimi më i madh Streaming për Anime si dhe më të ndjekurit. Në dispozicion kemi vendosur me mijëra episode si dhe shumë seriale e filma për t’u ndjekur kurdo dhe kudo. Çdo gjë është pa pagesë dhe me siguri."""
koha = "Asenshu u krijua më 1 Janar 2018 dhe filloi me lançimin e animeve të ndryshme."
pronesia = "Asenshu është një Projekt në pronësi të TOP TECH ALBANIA që është financuesi kryesor i këtij shërbimi. "
viruse = "Asenshu NUK permban viruse, por ajo thjesht permban reklama. Nese shtypni ne reklamat do te kaloni ne faqe tjeter qe NUK menaxhohet nga Asenshu. Nese kaloni ne ato faqe ju sugjerojme te kaloni menjehere tek faqja Asenshut ku ishit. Nese faqja ku beheni redirect ka viruse ato nuk jane te Asenshut edhe as qe e kemi qellimin te promovojme faqe me viruse, por nuk i menaxhojme dot ato faqe. Nese ktheheni menjehere perseri tek faqja zyrtare e Asenshuatehere nuk keni asnje rrezik per viruse ose te tilla gjera."
rezolucioni = "Ne bëjmë të pamundurën që të sjellim Filmat dhe Serialet sa më shpejt dhe ndonjëherë nuk e kemi mundësinë për t’i bërë në dy versione."
shkarko = "Çdo film ose episod ka pothuajse gjithmonë pranë një buton që lexon “SHKARKO”, kliko mbi të dhe mund ta shkarkosh aty."
donato = "Po, Gjatë këtyre tri viteve, jemi vet-financuar dhe pjesëtarët e stafit tonë kanë bërë një punë shumë të madhe. Por, çdo punë ka vështirësitë e saj, dhe prandaj po ju drejtohemi ju, që të merrni pjesë në mbështetjen e punës sonë. E ardhmja e faqes varet nga ju. Nëse doni të ndihmoni, kemi vendosur disa mundësi mbështetjeje të cilat ndodhen në faqen tonë në kategorinë LAJME."
app = "Për momentin Asenshu nuk ka një app. Nuk është e lehtë ta kemi një të tillë. Por në të ardhmen shpresojmë."
disqus = "Disqus është platformë komentuese e Faqes Asenshu. Mund të lexoni më shumë në: https://www.disqus.com/"
animeawards = "Asenshu çdo vit organizon Asenshu Anime Awards (AAA), zakonisht në fund të vitit ose fillim të vitit."
discordizyrtar = "Po. Asenshu ~ Komuniteti Zyrtar i Platformës 'ASENSHU'. Ky është një komunitet miqësor dhe i sigurt për të gjithë ata që shohin dhe pëlqejnë animet. Sigurohu të lexosh dhe respektosh rregullat për të siguruar mbarëvajtje për gjithsecilin."
discordawards = "Po, në çdo vit komuniteti zyrtar i Asenshu organizon Discord Award, për më shumë mund t'i shikoni tek #hall-of-fame."
aplikimstaffi = "Nëse doni të bëheni pjesë e Asenshu, kontaktoni në DM me @Kíra#4303."
partneritet = "Për arsye të tjera në lidhje me website, si: bashkëpunime, partneritete etj.; kontaktoni me @mghdus0128 në DM."
njoftime = "Nëse doni të merrni njoftime rreth episodit më të ri, lajmeve më të reja, votimeve më të reja ju mund të merrni rolin përkatës tek #rolet."
turne = "Nuk kemi ndonjë periudhë të saktë, por sapo të shtohen disa anime të reja në faqen tonë, do bëjmë përsëri Turne."
risi = "Asenshu vazhdimisht sjell Anime të reja, që ju i dëshironi dhe i shikoni. Animet më të reja nga Japonia direkt në Asenshu në gjuhën shqipe."
sugjerim = "Për momentin po merremi me projekte që na duhet pak kohë t'i mbarojmë, prandaj ju lutemi të mos sugjeroni shumë anime sepse vërtet nuk mundemi. Ju faleminderit."
mirupafshim = "Kjo varet nga ju nëse kemi përkrahjet tuaja, nëse vazhdoni të na ndiqni ne do të bëjmë të pamundurën për juve. Edhe pse shpenzimet janë shumë të larta dhe nuk kemi shumë mundësi, prandaj mbetet të shikohet në të ardhmen fati i Asenshu."
kur = "Asenshu përpiqet të nxjerrë episodet më të reja shumë shpejt, nga koha e transmetimit të tyre, por kjo mund të vonohet për shkak të gjërave të tilla si shpejtësia e ngadaltë e ngarkimit ose hostet e videos që kanë probleme me përpunimin e videos."
kur2 = "Nuk kemi ndonjë orar të saktë se kur del një episod, por që në momentin qe do të përkthehet do të publikohet në faqen tonë! Prandaj ju lutemi për durim dhe mirëkuptim."

kafe1 = discord.File('./assets/kafe.jpeg')
kafe2 = discord.File('./assets/kafe2.jpeg')
kafe3 = discord.File('./assets/kafe3.jpeg')
kafe4 = discord.File('./assets/kafe4.jpeg')
kafe5 = discord.File('./assets/kafe5.jpeg')
kafe6 = discord.File('./assets/kafe6.jpeg')
kafe7 = discord.File('./assets/kafe7.jpeg')
kafe8= discord.File('./assets/kafe8.jpg')
kafe9= discord.File('./assets/kafe9.jpg')
kafe10= discord.File('./assets/kafe10.jpeg')
kafe11 = discord.File('./assets/kafe11.jpg')
kafe12 = discord.File('./assets/kafe12.png')
kafe13 = discord.File('./assets/kafe13.jpg')
kafe14 = discord.File('./assets/kafe14.jpeg')

kafeList = [kafe1, kafe2, kafe3, kafe4, kafe5, kafe6, kafe7, kafe8, kafe9, kafe10, kafe11, kafe12, kafe13, kafe14]



lewdGIF1 = "https://tenor.com/view/anime-boob-hentai-nico-yazawa-love-live-gif-17393176"
lewdGIF2 = "https://tenor.com/view/dancing-anime-sexy-hentai-gif-5476864"
lewdGIF3 = "https://tenor.com/view/grab-grab-sheets-nisemonogatari-flustered-bakemonogatari-gif-18711125"
lewdGIF4 = "https://tenor.com/view/hentai-kamen-hero-underwear-pose-gif-16434636"
lewdGIF5 = "https://tenor.com/view/hentai-sexy-anime-cum-gif-18835007"
lewdGIF6 = "https://tenor.com/view/anime-kanokon-chizuru-booty-shake-gif-17170726"
lewdGIF7 = "https://tenor.com/view/sasuke-thinking-anime-naruto-gif-13593873"
lewdGIF8 = "https://tenor.com/view/boobs-memes-indi-home-hentai-gif-20239384"

lewdGIFS = [lewdGIF1, lewdGIF2, lewdGIF3, lewdGIF4, lewdGIF5, lewdGIF6, lewdGIF7, lewdGIF8]



faktiPavlefshem1 = "Nqs merr fryme me bythe edhe ulesh ke shanse te larta per te vdekur."
faktiPavlefshem2 = "Nje njeri mund te hidhet nga avioni pa parashute, por vetem nje here."
faktiPavlefshem3 = "Pellumbat vdesin pasi bejne seks. ||dmth ai qe qiva une vdiq, s'e di per te tjeret||"
faktiPavlefshem4 = "Eminemi eshte Slim Shady i vertete."
faktipavlefshem5 = "Nqs domatja eshte frut, atehere ketchupi eshte recel."

fakteTePavlefshme = [faktiPavlefshem1, faktiPavlefshem2, faktiPavlefshem3, faktiPavlefshem4, faktipavlefshem5]
