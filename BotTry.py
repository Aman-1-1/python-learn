import discord
from discord.ext import commands
from discord import app_commands
from pymongo import MongoClient, errors
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)


password = "Aman1029."
uri = f"mongodb+srv://amanregmi10:{password}@cluster0.cynppay.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["inventory_db"]
collection = db["items"]


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="newplayer", description="Start with basic pack")
@app_commands.choices(character=[
    app_commands.Choice(name="Mage", value="Mage"),
    app_commands.Choice(name="Archer", value="Archer"),
    app_commands.Choice(name="Swordmen", value="Swordmen")
])
async def new_player(interaction: discord.Interaction, name: str, character: app_commands.Choice[str]):
    try:
       
        if collection.find_one({"name": name}):
            await interaction.response.send_message("Please choose a unique name!", ephemeral=True)
            return

       
        item1 = {"name": name, "power": 10, "money": 1000, "character": character.value}

       
        if character.value == "Archer":
            image_file = os.path.join(BASE_DIR, "archer.png")
        elif character.value == "Mage":
            image_file = os.path.join(BASE_DIR, "mage.png")
        elif character.value == "Swordmen":
            image_file = os.path.join(BASE_DIR, "swordsmen.png")
        else:
            image_file = None  # fallback if needed

       
        if image_file and not os.path.exists(image_file):
            await interaction.response.send_message(f"Image file for {character.value} not found!", ephemeral=True)
            return


        file = discord.File(image_file, filename=os.path.basename(image_file))
        embed = discord.Embed(
            title="New Player Created!",
            description=f"Your character **{name}** ({character.value}) has been created.",
            color=discord.Color.blue()
        )
        embed.add_field(name="Power", value=f"{item1['power']}", inline=False)
        embed.add_field(name="Money", value=f"{item1['money']}", inline=False)
        embed.add_field(name="Character", value=f"{item1['character']}", inline=False)
        embed.set_thumbnail(url=f"attachment://{os.path.basename(image_file)}")

     
        await interaction.response.send_message(embed=embed, file=file)

      
        collection.insert_one(item1)

    except errors.ConnectionFailure:
        print("Could not connect to MongoDB server")
    except errors.OperationFailure as e:
        print(f"Operation failed: {e}")
    except errors.PyMongoError as e:
        print(f"Some error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


bot.run("Token")

# item1 = {"name": "Laptop", "quantity": 10, "price": 800, "category": "Electronics"}
# item2 = {"name": "Chair", "quantity": 50, "price": 40, "category": "Furniture"}

# collection.insert_many([item1, item2])


