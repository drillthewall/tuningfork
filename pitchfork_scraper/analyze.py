	import json
import operator

with open('results.json') as json_file:
	data = json.load(json_file)

tot = 0
for review in data:
	tot += float(review['score'])
average_score = tot / len(data)
print("average score is", average_score)

wholetext = ""
for review in data:
	wholetext += " " + review['text']

text_list = wholetext.split()

occurence = {}

for word in text_list:
	if len(word) > 6:
		occurence[word.lower()] = 0

for word in text_list:
	if len(word) > 6:
		occurence[word.lower()] += 1

for review in data:
	genre = review['genre']
	scoregenre[genre] = 0

for review in data:
	genre = review['genre']
	scoregenre[genre] += review['score']

print(genreocc)


sorted_dict = sorted(occurence.items(), key = lambda x : x[1], reverse=True)

# print(sorted_dict)

f = open('longwords.txt','w',encoding="utf-8")
print(*sorted_dict,sep = "\n",file=f)