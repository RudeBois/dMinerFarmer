# dMinerFarmer
An easy to use self-mining tool for Discord Miner, written in Python and utilizing the rewrite branch of Rapptz's Python Discord API wrapper, discord.py.

# Prerequisites
- Python3.6 <= must be installed on your system. You can install Python here: https://www.python.org/downloads/
- Install git and add it to your PATH, if you haven't already: https://git-scm.com/
- Must install the discord.py rewrite branch. This can be done by running the following command in your command prompt:
`pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]`
- aiohttp is required by discord.py and will be installed alongside it. JSON and datetime come with Python.

# Setting up config.json
THE BOT WILL NOT WORK UNLESS YOU SUCCESSFULLY SET UP `config.json`. DO NOT MAKE NEW ISSUES RELATED TO THIS.
Enter the `config.json` file. Within this file, there are 4 things that you must fill out:
- `destination` is a channel ID in which the bot will operate. This channel ID must be provided to `config.json` as an integer.
- `token` is the unique token for your Discord account. You can find a guide to locate your token here: https://discordhelp.net/discord-token. Your token must be provided to `config.json` as a string.
- `delay` is the delay in seconds in between each new mine. This must be provided to `config.json` as an integer.
- `autoRepair` is to specify if you want to enable automatic pickaxe repairing. This must be provided to `config.json` as a boolean (true or false).

If you wish to make any changes have effect, you must save the changes within `config.json` and restart your bot. 

# Running the bot
Once you have successfully completed filling in `config.json`, navigate to your command prompt and run the Python script with `python main.py`.

# Disclaimer
I, the creator of this bot, remind you that user-bots, or self-bots, are against the Discord Terms of Service and may result in your account being terminated. Utilizing this bot may also result in you being banned from the Discord Miner community. By downloading this script and utilizing it, you claim all responsibility for the effects of your usage of this bot.
