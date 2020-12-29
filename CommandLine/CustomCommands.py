from CommandLine.CommandControl import cliCommand, commands
from Utils.StringManipulation import textPadding
from Utils.Log import log
import asyncio
import sys

@cliCommand(name="exit")
def exitClient(args):
	"""Exit the current program with exit code 0"""
	sys.exit(0)

@cliCommand(name="help")
def commandHelp(args):
	"""Show a list of available commands."""
	log(f"Showing help menu", "CLI")
	longest = 0
	for i in commands:
		if len(i) > longest:
			longest = len(i)
	for i in commands:
		val = commands[i]
		cmdName = textPadding(i, longest)
		cmdDescription = val[0].__doc__
		log(f"\t{cmdName}\t{cmdDescription}","CLI")