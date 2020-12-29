commands = {}

def registerCommand(name, function, isAsync = False):
	commands[name] = (function, isAsync)

