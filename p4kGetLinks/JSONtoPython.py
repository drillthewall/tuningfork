import json

with open("BNMlinks.json") as json_file:
	data = json.loads(json_file.read())
	for review in data:
		print(review['album'])
