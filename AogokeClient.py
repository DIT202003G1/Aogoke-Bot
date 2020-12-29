import discord
import asyncio
import Utils
import CommandLine
from Utils.Log import log
from CommandLine import CustomCommands
from CommandLine.AsyncInterpreter import interpret

def connect(client, token):
	log("Waiting to login/connect ...")
	client.run(token)

class AogokeClient(discord.Client):
	active_state = False
	active_user = None

	async def callActivate(self,channel,user):
		await channel.send("我在!")
		self.active_state = True
		self.active_user = user.id
		await client.change_presence(status=discord.Status.dnd)

	async def on_ready(self):
		log('Logged on as {0}!'.format(self.user))
		await self.loop.create_task(self.background(),name="cli prompt")

	async def on_message(self, message):
		if (f"<@!{self.user.id}>" in message.content) and (not self.active_state):
			await self.callActivate(message.channel, message.author)

	async def background(self):
		await asyncio.sleep(0.3)
		await interpret(self)
		await self.loop.create_task(self.background(),name="cli prompt")
