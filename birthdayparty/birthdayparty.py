import discord
from discord.ext import commands

class BirthdayParty
	"""A custom birthday party widget.
	Celebrate with the whole server!
	"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")
	
	@commands.group(name="party", pass_context=True)
	async def _party(self)
		"""Everyone deserves to have their birthday celebrated.
		Register your birthday so that everyone else has to celebrate with you!
		
		Commands:
			- !party register <birthday> : Registers your birthday
			- !party showbirthdays : Shows all recorded birthdays
			- !party shownext : Shows the next birthday
		"""
		await self.bot.say("Debug")

	@_party.command(pass_context=True)
	async def register(self, user, *, bday_input : str)
		"""Registration, yeah!
		
		Command: !party register <birthday>
		<birthday> input should be in MM/DD format.
		"""
		account = user.name
		bday_setdate = bday_input
		
		openFile = open("data/birthday/birthdays.txt", "w+")
		findUser = openFile.find(account)
		if account is in openFile:
			await self.bot.say("User found.")
		else:
			await self.bot.say("User not found, creating record now.")
			openFile = open("data/birthday/birthdays.json", "a+")
			openFile.write(user.name)
			findUser = openFile.find(account)
			if account is in openFile:
				await self.bot.say("Operation success, account created.")
			else:
				await self.bot.say("Operation failed, account not created.")
	
def setup(bot):
    bot.add_cog(BirthdayParty(bot))