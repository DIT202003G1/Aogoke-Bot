from CommandLine.CommandControl import registerCommand, commands
import sys

def exitClient(args):
	"""Exit the current program with exit code 0"""
	sys.exit(0)

def registerCommands():
	registerCommand("exit",exitClient)