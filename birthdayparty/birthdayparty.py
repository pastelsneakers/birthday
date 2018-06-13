import discord
from discord.ext import commands

class Birthdayparty:
	"""A custom birthday party widget. Celebrate with the whole server!"""

	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def mycom(self, user : discord.Member):
		await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")

def setup(bot):
	bot.add_cog(Birthdayparty(bot))
