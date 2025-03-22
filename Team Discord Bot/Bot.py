#A Disord Bot For your team
#Some settings may need to be a filled out
Token = '<Enter Token Here>'

import discord
from discord.ext import commands
from discord import app_commands
from random import randint
import requests
from bs4 import BeautifulSoup as bs
import urllib.request 
import json
from geopy.geocoders import Nominatim
import translate
import wikipedia as wiki

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
ctx = commands.Context

def determine_winner(player1, player2):
    if (player1 == "rock" and player2 == "rock") or (player1 == "Rock" and player2 == "rock") or (player1 == "scissors" and player2 == "scissors") or (player1 == "Scissors" and player2 == "scissors") or (player1 == "paper" and player2 == "paper") or (player1 == "Paper" and player2 == "paper"):
        return "It's a tie!"
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "Rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "Scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock") or (player1 == "Paper" and player2 == "rock"):
        return "Player wins!"
    else:
        return "Computer wins!"

    
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} commands")
async def update_presence():
        total_member_count = 0
        for guild in bot.guilds:
            if guild.member_count:
                total_member_count += guild.member_count

        activity = discord.Activity(
            name=f"{total_member_count} users", type=discord.ActivityType.listening
        )

        await bot.change_presence(activity=activity)
update_presence()

@bot.tree.command(name="mvp", description="Get the mvp of the team (randomly)")
async def mvp(interaction: discord.Interaction):
    people = ["Team Member 1", "Team Member 2"]
    person = randint(0,7)
    mvp_embeded = discord.Embed()
    mvp_embeded.title = "MVP of <Team>"
    mvp_embeded.add_field (name="",value=f"{people[person]} is the MVP of CyberAegis Pandora.")
    await interaction.response.send_message(embed=mvp_embeded)


@bot.tree.command(name="rps", description="Play the popular game rock-paper-scissors with the bot.")
@app_commands.describe(choice = "Choose your move: rock, paper, or scissors.")
@app_commands.choices(choice=[
         app_commands.Choice(name="Rock", value="rock"),
         app_commands.Choice(name="Paper", value="paper"),
         app_commands.Choice(name="Scissors", value="scissors")
    ])
async def rps(interaction: discord.Interaction, choice: app_commands.Choice[str]):
    computer_choice = randint(0,2)
    possible_choices = ["rock", "paper", "scissors"]
    computer_rps = possible_choices[computer_choice]
    winner = determine_winner(choice.value, computer_rps)
    if winner == "Computer wins!":
        rps_color = 0xFF0000
    elif winner == "Player wins!":
        rps_color = 0x2ecc71
    else:
        rps_color = 0x992d22
    rps_embeded = discord.Embed(color=rps_color)
    rps_embeded.title = winner
    results = f"You chose {choice.value}. Computer chose {computer_rps}. {winner}"
    rps_embeded.add_field (name="", value=results)
    await interaction.response.send_message(embed=rps_embeded)

@bot.tree.command(name="coinflip", description="Flip a coin")
async def coinflip(interaction: discord.Interaction):
    coin_num = randint(1,2)
    if coin_num == 1:
        coin_landing = "Heads"
        coin_landing2 = "heads"
    elif coin_num == 2:
        coin_landing = "Tails"
        coin_landing2 = "tails"
    coin_embeded = discord.Embed(color=0x7d7979)
    coin_embeded.title = coin_landing
    coin_embeded.add_field(name="", value=f"You flipped a coin and it landed on {coin_landing2}.")
    await interaction.response.send_message(embed=coin_embeded)

@bot.tree.command(name="scapegoat", description="get whover sold the last TR (randomly)")
async def scapegoat(interaction: discord.Interaction):
    people = ["Team Member 1", "Team Member 2"]
    seller = randint(0,8)
    wstltr_embeded = discord.Embed()
    wstltr_embeded.title = "Who Sold the Last TR"
    wstltr_embeded.add_field (name="",value=f"{people[seller]} sold the last TR.")
    await interaction.response.send_message(embed=wstltr_embeded)

@bot.tree.command(name="wikipedia_random", description="Get a random wikipedia article.")
async def wikipedia(interaction: discord.Interaction):
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
    "action": "query",
    "format": "json",
    "list": "random",
    "rnnamespace": 0,
    "rnlimit": 1
    }
    request_response = requests.get(api_url, params=params)
    data = request_response.json()
    article_title = data["query"]["random"][0]["title"]
    article_url = f"https://en.wikipedia.org/wiki/{article_title.replace(' ', '_')}"
    await interaction.response.send_message(f"[{article_title}]({article_url})")

@bot.tree.command(name="roll_dice", description="Roll a dice")
@app_commands.describe(dice_types = "Enter the type of dice: ")
@app_commands.choices(dice_types = [
    app_commands.Choice(name = "4-sided die", value = "4-sided die"),
    app_commands.Choice(name = "6-sided die", value = "6-sided die"),
    app_commands.Choice(name = "8-sided die", value = "8-sided die"),
    app_commands.Choice(name = "10-sided die", value = "10-sided die"),
    app_commands.Choice(name = "12-sided die", value = "12-sided die"),
    app_commands.Choice(name = "20-sided die", value = "20-sided die"),
    app_commands.Choice(name = "50-sided die", value = "50-sided die"),
    app_commands.Choice(name = "100-sided die", value = "100-sided die"),
]
)
async def roll_dice(interaction: discord.Interaction, dice_types: str):
    if dice_types == "4-sided die":
        roll = randint(1, 4)
        await interaction.response.send_message(f"You rolled `{roll}` on a {dice_types}.")
    elif dice_types == "6-sided die":
        roll = randint(1, 6)
        await interaction.response.send_message(f"You rolled `{roll}` on a {dice_types}.")
    elif dice_types == "8-sided die":
        roll = randint(1, 8)
        await interaction.response.send_message(f"You rolled `{roll}`on a {dice_types}.")
    elif dice_types == "10-sided die":
        roll = randint(1, 10)
        await interaction.response.send_message(f"You rolled `{roll}`on a {dice_types}.")
    elif dice_types == "12-sided die":
        roll = randint(1, 12)
        await interaction.response.send_message(f"You rolled `{roll}`on a {dice_types}.")
    elif dice_types == "20-sided die":
        roll = randint(1, 20)
        await interaction.response.send_message(f"You rolled `{roll}`on a {dice_types}.")
    elif dice_types == "50-sided die":
        roll = randint(1, 50)
        await interaction.response.send_message(f"You rolled `{roll}`on a {dice_types}.")
    elif dice_types == "100-sided die":
        roll = randint(1, 100)
        await interaction.response.send_message(f"You rolled `{roll}`on a {dice_types}.")

@bot.tree.command(name="8ball", description="Magic 8 ball")
@app_commands.describe(question = "Question to be asked")
async def ball(interaction:discord.Interaction, question:str):
    Answers = ["Yes", "No", "Maybe", "No way!", "Thats cap", "yes???", "Ask again later", "I don't know"]
    Respone_num = randint(0,7)
    response = Answers[Respone_num]
    ballEmbed = discord.Embed()
    ballEmbed.title = "Magic 8 Ball"
    ballEmbed.add_field(name="Question",value=question)
    ballEmbed.add_field(name="\u200B", value="\u200B")
    ballEmbed.add_field(name="Answer", value=response)
    ballEmbed.set_footer(text="The 8ball never lies.")
    await interaction.response.send_message(embed=ballEmbed)

@bot.tree.command(name="live_weather", description="Get the current weather of a location")
@app_commands.describe(region = "Enter a city, country, state, or zip code")
async def live_weather(interaction:discord.Interaction, region: str):
    city2 = region.replace(" ", "+")
    #HEADERS
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    # US english
    LANGUAGE = "en-US,en;q=0.5"
    #get html

    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    weatherData = session.get(f"https://www.google.com/search?q={city2}+weather")

    #Live Temp
    soup = bs(weatherData.content, "html.parser")
    temp = soup.find_all(class_="wob_t q8U8x")[0]
    temp = temp.text
    def FtoC(Farenheit) :
        Celsius =  (Farenheit - 32)/1.8
        return (Celsius)

    #Conditions
    condtions = soup.find_all(id="wob_dc")[0]
    condtions = condtions.text

    #Wind speed
    wind = soup.find_all(id="wob_ws")[0]
    wind = wind.text

    #Precipitation
    rain = soup.find_all(id="wob_pp")[0]
    rain = rain.text

    #Humidity
    Humidity = soup.find_all(id="wob_hm")[0]
    Humidity = Humidity.text

    weather_embed=discord.Embed(color=0x3971cc)
    weather_embed.title = f"Live Weather Report for {region}"
    weather_embed.add_field(name="Temperature", value=f"{temp} °F or {round(FtoC(int(temp)))} °C")
    weather_embed.add_field(name="\u200B", value="\u200B")
    weather_embed.add_field(name="Conditions", value=condtions)
    weather_embed.add_field(name="Chance of Rain", value=rain)
    weather_embed.add_field(name="\u200B", value="\u200B")
    weather_embed.add_field(name="Wind Speed", value=wind)
    weather_embed.add_field(name="Humidity", value=Humidity)
    weather_embed.set_footer(text="Powered by Google")
    await interaction.response.send_message(embed=weather_embed)

@bot.tree.command(name="iss", description="Get the current location of the ISS")
async def ISS(interaction: discord.Interaction):
    ISS_embed = discord.Embed(color=0x1E90FF)
    
    async with aiohttp.ClientSession() as session:
        async with session.get("http://api.open-notify.org/iss-now.json") as resp1:
            data1 = await resp1.json()
        async with session.get("http://api.open-notify.org/astros.json") as resp2:
            data2 = await resp2.json()
    
    # Latitude & Longitude
    lat, long = data1["iss_position"]["latitude"], data1["iss_position"]["longitude"]
    
    geolocator = Nominatim(user_agent="my-app", timeout=10)
    try:
        location = geolocator.reverse((lat, long), language="en")
        final_location = location.address if location else "Unknown"
    except Exception:
        final_location = "Location lookup failed"
    
    ISS_embed.add_field(name="Location", value=final_location)
    ISS_embed.add_field(name="Latitude and Longitude", value=f"{lat}, {long}")
    
    # People Onboard
    people_on_board = [person["name"] for person in data2.get("people", [])]
    ISS_embed.add_field(name=f"Humans in Space ({len(people_on_board)})", 
                        value=", ".join(people_on_board) if people_on_board else "No data")
    ISS_embed.set_footer(text="Powered by open-notify.org API")
    
    await interaction.response.send_message(embed=ISS_embed)

bot.run(Token)
