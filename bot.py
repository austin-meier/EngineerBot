import discord
from discord.ext import commands
from jacket import create_jacket

token = "MTA5Nzk0NTIyNzkyODU0MzI3Mg.GYqedC.Oige98ulA2Irhy5sTTm5IoobrxYBWucdPLfjFk"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

usage_statement = """This command will generate an AWS golden jacket for you.
Please supply a list of the certifications you have, separated by a space.

ex:
```
>jacket ccp dva saa ...
```
"""

@bot.command()
async def jacket(ctx, *args):

    if len(args) < 1:
        await ctx.send(usage_statement)
        return

    if args[0].lower() == "help":
        await ctx.send(usage_statement)
        return

    image_bytes = create_jacket(args)
    image_file = discord.File(fp = image_bytes, filename="aws-jacket.jpg")
    await ctx.send("One AWS Golden Jacket coming up!", file=image_file)

bot.run(token)