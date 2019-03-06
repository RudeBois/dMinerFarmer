import discord
from discord.ext import commands
import asyncio
import json
import datetime

config = json.load(open("config.json", "r"))

bot = commands.Bot(command_prefix="!", self_bot=True)
initial_extensions = ['cogs.TokenVerification']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except:
            print(f'Failed to load extension {extension}.')

async def miningAway():
    await bot.wait_until_ready()
    destination = bot.get_channel(config['destination'])
    while not bot.is_closed():
        await destination.send("m!m")
        await asyncio.sleep(config['delay'])
bot.bg_task = bot.loop.create_task(miningAway())

@bot.event
async def on_ready():
    print('dMinerFarmer Operational!')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    # Only handling messages in the channel specified in config.json
    if message.channel.id == config['destination']:
        # Only handling messages from the Discord Miner bot specifically
        if message.author.id == 492969308201418756:
            try:
                # If the message is an embed, and contains an image, this is a verification image
                if message.embeds[0].image.url:
                    # Parses the url to recieve the code, and sends it to the channel
                    verifCode = message.embeds[0].image.url[-4:]
                    await message.channel.send(f"m!verify {verifCode}")
                    print(f"[{datetime.datetime.utcnow()}] Verification was passed with code {verifCode}")
            except IndexError:
                pass
            try:
                # The bot mentions the user on auto-mine completion; this will fire if your auto-mine completes
                if message.mentions[0]:
                    await message.channel.send("m!s bonus 2")
                    print(f"[{datetime.datetime.utcnow()}] Auto-mine was purchased.")
            except IndexError:
                pass
            # If the bot sends this message, you must repair
            if config['autoRepair']:
                if message.content == "Your pickaxe is broken. Type `m!repair` to repair it!":
                    await message.channel.send("m!repair")
                    print(f"[{datetime.datetime.utcnow()}] Pickaxe was repaired.")


bot.run(config['token'], bot=False)
