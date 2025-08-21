import discord
import discord
from discord.ext import commands
import requests


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="info",description="Discription about pokemon")
async def pokeinfo(interaction: discord.Interaction,pokemon_name:str):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    url1 = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}"
    response1 = requests.get(url1)
    if response1.status_code == 200:
        data1=response1.json()
        pokemon_info1 = {
            "flavor_text_entries": data1["flavor_text_entries"],
        }       
    if response.status_code == 200:
        data=response.json()
        pokemon_info = {
            "name": data["name"].capitalize(),
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]],
            "abilities": [a["ability"]["name"] for a in data["abilities"]],
            "sprite": data["sprites"]["front_default"]
        }        
        
        embed = discord.Embed(
            
            title=pokemon_info["name"],
            description=pokemon_info1["flavor_text_entries"][0]["flavor_text"],
            color=discord.Color.blue()
        )
        embed.add_field(name="Abilities", value=", ".join(pokemon_info["abilities"]), inline=True)
        embed.set_thumbnail(url=pokemon_info["sprite"])
        await interaction.response.send_message(embed=embed)
    
bot.run("1MTQwNzk4OTMxNTE5MDkxOTIzMQ.GY4x7S1.12jrKiKNuDIUyPDVHOMhr0wFz1-1TnM3jveqnvI901")