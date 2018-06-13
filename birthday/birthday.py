import discord
import random
from discord.ext import commands
from random import choice

class Birthday:
	"""Birthday commands."""
	
	def __init__(self, bot):
		self.bot = bot
		self.wish = ["Have a great birthday!", "Remember to treat yourself today!", "I hope your day is as wonderful as your smile!",
					 "Don't forget to smile!", "Today is your day! Make it good!"]
	
	@commands.command()
	async def test(self):
		"""Testing."""
		
		await self.bot.say("`" + choice(self.wish) + "`")

def setup(bot):
    bot.add_cog(Birthday(bot))
