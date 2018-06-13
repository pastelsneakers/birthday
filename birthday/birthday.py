import discord
import random
import logging
from discord.ext import commands
from random import choice
from cogs.utils.dataIO import dataIO
from copy import deepcopy
from .utils import checks

class BirthdayError(Exception):
    pass

class BirthdayAlreadyExists(BirthdayError):
    pass

class NoBirthday(BirthdayError):
    pass

class Birthdays:
	def __init__(self, bot, file_path):
		self.birthdays = dataIO.load_json(file_path)
		self.bot = bot
	
    def create_account(self, user, *, birth_date : str):
        server = user.server
		if not self.birthday_exists(user):
			if server.id not in self.birthdays:
				self.birthdays[server.id] = {}
			else:
				birthdate = birth_date
				account = {"name": user.name,
						   "birthday": birth_date
						   }
			self.birthdays[server.id][user.id] = account
			self._save_birthdays()
			return self.birthday_get(user)
		else:
			raise BirthdayAlreadyExists()

    def birthday_exists(self, user):
        try:
            self._get_birthday(user)
        except NoAccount:
            return False
        return True
	
	def birthday_get(self, user):
        bdy = self._get_birthday(user)
        bdy["id"] = user.id
        bdy["server"] = user.server
        return self._create_birthday_obj(bdy)

    def _create_birthday_obj(self, account):
        account["member"] = account["server"].get_member(account["id"])
        account["birthday_set_as"] = datetime.strptime(account["birthday_set_as"],
                                                  "%Y-%m-%d")
        Account = namedtuple("Account", "id name birth_date_set "
                             "birthday_set_at server member")
        return Account(**account)
	
	def _save_birthdays(self):
        dataIO.save_json("data/birthday/birthdays.json", self.birthdays)

class Birthday:
	"""Birthday commands."""
	
	def __init__(self, bot, file_path):
		self.bot = bot
		self.wish = ["Have a great birthday!", "Remember to treat yourself today!", "I hope your day is as wonderful as your smile!",
					 "Don't forget to smile!", "Today is your day! Make it good!"]
		self.birthday_record = Birthdays(bot, "data/birthday/birthdays.json")
		self.settings = dataIO.load_json(self.file_path)
	
	@commands.group(name="bank", pass_context=True)
    async def birthdayp(self, ctx):
        """Birthday operations"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
	
	@birthdayp.command(pass_context=True)
	async def register(self, ctx, user, *, bday : str)
		birfday = bday
		settings = self.settings[ctx.message.server.id]
        author = ctx.message.author
		try:
            account = self.birthday_record.create_account(author, birfday)
            await self.bot.say("Birthday registered! You will receive a birthday wish from DaddyBot on " + bday + ", " + author.display_name + ".")
		except AccountAlreadyExists:
            await self.bot.say("You are already registered, " + author.display_name + ".")

def setup(bot):
    bot.add_cog(Birthday(bot))
