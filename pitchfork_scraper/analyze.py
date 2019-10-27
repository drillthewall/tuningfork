import json
import operator
from functools import lru_cache
memoize = lru_cache(None)

'''
----------- Change the file name / path of the list of reviews that you would like to analyze -----------
'''
filename = 'EightPlusResults.json'
print("Analyzing",filename)

with open(filename) as json_file:
    data = json.load(json_file)

tot = 0
for review in data:
    tot += float(review['score'])
average_score = tot / len(data)
print("Average score for every review listed in this file is", average_score)

@memoize
def get_average_by_artist(inputartist: str):
    inputartist = inputartist.lower()
    tot, cnt = 0, 0
    for review in data:
        match = False
        for artist in review['artist']:
            if artist.lower() == inputartist:
                match = True
        if match:
            tot += float(review['score'])
            cnt += 1
    assert cnt > 0, "bruh pitchfork didn't even give a 8.0+ review to them"
    print("This artist has", cnt, "albums with a 8+ score, with a total of", tot, "points, which gives an average of")
    return tot / cnt


genreList = [
    'Electronic',
    'Rock',
    'Pop/R&B',
    'Folk/Country',
    'Rap',
    'Experimental',
    'Jazz'
]
genreAverage = {}
genreCount = {}
genreScore = {}

for genre in genreList:
    genreAverage[genre] = 0
    genreCount[genre] = 0
    genreScore[genre] = 0
    for review in data:
        for i in review['genre']:
            if genre == i:
                genreCount[genre] += 1
                genreScore[genre] += float(review['score'])
    genreAverage[genre] = genreScore[genre] / genreCount[genre]

case_insensitive_equal = lambda s1, s2: s1.lower() == s2.lower()

@memoize
def get_average_by_genre(inputgenre: str):
    done = False
    assert type(inputgenre) == str, "You forgot quotes"
    for i in genreList:
        if case_insensitive_equal(i, inputgenre):
            done = True
            return genreAverage[i]
    assert done, "Invalid genre input"







# wholetext = ""
# cnt = 0
# for review in data:
# 	cnt += 1
# 	wholetext += " " + review['text']
# 	if cnt % 100 == 0:
# 		print("concatenated", cnt, "reviews")

# f = open('EightPlusWholeText.txt','w',encoding="utf-8")
# print(wholetext,sep = "\n",file=f)

# text_list = wholetext.split()

# occurence = {}

# for word in text_list:
# 	if len(word) > 5:
# 		occurence[word.lower()] = 0

# for word in text_list:
# 	if len(word) > 5:
# 		occurence[word.lower()] += 1

# # print(genreocc)


# sorted_dict = sorted(occurence.items(), key = lambda x : x[1], reverse=True)

# # print(sorted_dict)

# f = open('EightPluslongwords.txt','w',encoding="utf-8")
# print(*sorted_dict,sep = "\n",file=f)
