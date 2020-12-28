import discord
import Utils
from Utils.Log import log

class AogokeClient(discord.Client):
	active_state = False
	active_user = None

	async def callActivate(self,channel,user):
		await channel.send("我在!")
		self.active_state = True
		self.active_user = user.id

	async def on_ready(self):
		log('Logged on as {0}!'.format(self.user))

	async def on_message(self, message):
		if (f"<@!{self.user.id}>" in message.content) and (not self.active_state):
			await self.callActivate(message.channel, message.author)