import discord
import Utils
from Utils.Log import log

class AogokeClient(discord.Client):
    async def on_ready(self):
        log('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        log('Message from {0.author}: {0.content}'.format(message))
