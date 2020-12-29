from RequestHandling.IntentionControl import useCase
from six.moves.urllib.parse import quote
import requests
import re

#### True = Usecase has end, False = Usecase continues ####

#Cancel usecase
@useCase('cancel','begin')
async def cancel_begin(client, context):
	return True

#Null Usecase Handling
@useCase('null','begin')
async def null_begin(client,context):
	await context.channel.send("不好意思，我不明白你說了什麼，請換一種方式說明")
	client.activeStep = ""
	client.activeIntention = ""
	return False

# Weather
@useCase("weather","begin")
async def weather_begin(client, context):
	await context.channel.send("正在查詢 請稍候")
	url = r"https://www.google.com/search?q=" + quote(context.content)
	headers = {
		'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
	}
	response = requests.get(url,headers=headers).text
	
	result = {}

	#Match results
	#where
	matches = re.search(r'(?<=<div class="wob_loc mfMhoc vk_gy vk_h" id="wob_loc">)[a-z|A-Z|0-9|\s|\,]*(?=<\/div>)',response)
	if matches:
		result["where"] = matches.group(0)
	#status
	matches = re.search(r'(?<=<span class="vk_gy vk_sh" id="wob_dc">)[a-z|A-Z|0-9|\s|\,]*(?=<\/span>)',response)
	if matches:
		result["status"] = matches.group(0)
	#temp
	matches = re.search(r'(?<=<span class="wob_t TVtOme" id="wob_tm" style="display:inline">)[\-|a-z|A-Z|0-9|\s|\,]*(?=<\/span>)',response)
	if matches:
		result["temp"] = matches.group(0)
	#preciptation
	matches = re.search(r'(?<=<span id="wob_pp">)[a-z|A-Z|0-9|\s|\,|\%]*(?=<\/span>)',response)
	if matches:
		result["preciptation"] = matches.group(0)
	#humidity
	matches = re.search(r'(?<=<span id="wob_hm">)[a-z|A-Z|0-9|\s|\,|\%]*(?=<\/span>)',response)
	if matches:
		result["humidity"] = matches.group(0)
	#wind
	matches = re.search(r'(?<=<span class="wob_t" id="wob_ws">)[a-z|A-Z|0-9|\s|\,|\%|\/]*(?=<\/span>)',response)
	if matches:
		result["wind"] = matches.group(0)

	if result:
		try:
			message = (
				f'查詢到 {result["where"]} 的天氣爲 {result["status"]}\n' + 
				f'氣溫爲{result["temp"]}攝氏度(C)，降雨/雪機率{"高達" if int(result["preciptation"][:-1]) >= 50 else "爲"}'+
				f' {result["preciptation"]}，風速爲 {result["wind"]}\n')
			if int(result["temp"]) <= 16:
				message += "氣溫寒冷，請做好防寒措施"
			elif int(result["temp"]) <= 20:
				message += "氣溫稍微有點冷，請做好防寒措施"
			elif int(result["temp"]) < 27:
				message += "氣溫適中，記得補充水分"
			elif int(result["temp"]) >= 27:
				message += "炎炎夏日，記得補充水分，謹防中暑!"
			await context.channel.send(message)
		except Exception:
			await context.channel.send("很抱歉  我未能查找到任何天氣資訊  或  查詢的過程中出錯 (請聯繫開發者)\n你可以嘗試換一個地方或問法")
	else:
		await context.channel.send("很抱歉  我未能查找到任何天氣資訊\n你可以嘗試換一個地方或問法!")

	return True