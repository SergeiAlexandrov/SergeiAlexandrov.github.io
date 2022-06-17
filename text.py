#!/usr/bin/python3
import json
import time
while True:
	text = ""

	with open("./text.json", "w") as json_file:
		text_file = open("./text.txt", "r")
		for x in text_file.readlines():
			text += x + "<br>"
		text_dict = {
			"text" : text
		}
		json_dict = json.dumps(text_dict, indent = 4)
		json_file.write(json_dict)
		json_file.close()
		text_file.close()
		print("Update Time: " + time.asctime())
	time.sleep(15)