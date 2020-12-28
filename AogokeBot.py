from AogokeClient import AogokeClient
import json
import sys

DEBUG = False
# DEBUG = True

with open("AogokeConfig.json","r") as r:
	AogokeConfig = json.load(r)

client = AogokeClient()

if not DEBUG:
	client.run(AogokeConfig["Token"])
	sys.exit(0)