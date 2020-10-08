from AogokeClient import AogokeClient
import json

with open("AogokeConfig.json","r") as r:
	AogokeConfig = json.load(r)

client = Aogo()
client.run(AogokeConfig["Token"])