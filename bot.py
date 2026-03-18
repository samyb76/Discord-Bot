import discord
from discord.ext import commands
import random
import requests

TOKEN = "Your_Discord_Bot_Token_Here"
API_KEY = "Your_OpenWeatherMap_API_Key_Here"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")


@bot.command()
async def help(ctx):
    await ctx.send("Commandes : !help, !joke, !weather <ville>")


@bot.command()
async def joke(ctx):
    jokes = [
        "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau !",
        "Pourquoi les canards ont-ils des plumes ? Pour couvrir leur derrière !",
        "Pourquoi les éléphants n'utilisent-ils pas d'ordinateurs ? Parce qu'ils ont peur des souris !",
        "Pourquoi les squelettes ne se battent-ils jamais entre eux ? Parce qu'ils n'ont pas le cran !",
        "Pourquoi les poissons détestent-ils l'ordinateur ? Parce qu'ils ont peur du net !"
        "Quel est le comble pour un électricien ? De ne pas être au courant !",
        "Comment appelle-t-on un chat qui a perdu ses pattes ? Un chat-pitre !",
    ]
    await ctx.send(random.choice(jokes))


@bot.command()
async def weather(ctx, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        await ctx.send("Ville introuvable")
        return

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    await ctx.send(f"{city} : {temp}°C, {desc}")


bot.run(TOKEN)
