import nextcord
from nextcord.ext import commands
from discord import application_command
from nextcord.ext.commands import cooldown, BucketType
from discord.ext.commands import cooldown, BucketType   
from discord.ui import Button, View
from discord import ButtonStyle



bot = commands.Bot(command_prefix="n!",intents=nextcord.Intents.all())
myserverid= 835199166346821632



@bot.event
async def on_ready():
    print(f"Bot Ready for Action!")
    


bot.load_extension(f"cogs.pp_cog")


    




#question:
#pick the apple; choose between apple, grape, pear, and banana
#ask in 3 different types; 
    

##PROMPT! Discord does not update its slash commands unless you set a guild id or wait a couple hours... Additionally


bot.run('MTA0MzgzOTU1NTE3MTc3ODY1MA.GwBuk7.ZlaL51pRwdLg_-FiFv6RKMSkyaR5aHCykw8Dhg')