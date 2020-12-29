import datetime

def log(msg,logType="LOG"):
	print(f"[{datetime.datetime.now()}][{logType}] {msg}")