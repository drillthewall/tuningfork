import json

filename = 'EightPlusResults.json'
print("Analyzing",filename)

with open(filename) as json_file:
    data = json.load(json_file)

artist_name_to_num = dict()
num_to_artist_name = ['PLACEHOLDER']
graph = list()


cnt = 0
for review in data:
    for artist in review['artist']:
        if artist not in artist_name_to_num.keys():
            cnt += 1
            artist_name_to_num[artist] = cnt
            num_to_artist_name.append(artist)
        # for related_artist in review['artistLinks']:
        #     if related_artist not in artist_name_to_num.keys():
        #         cnt += 1
        #         artist_name_to_num[related_artist] = cnt
        #         num_to_artist_name.append(related_artist)            

graph = [[0 for _ in range(cnt+2)] for _ in range(cnt+2)]

for i in range(1,cnt+1):
    artist_name = num_to_artist_name[i]
    for other_review in data:
        if artist_name in other_review['text']:
            for other_artist in other_review['artist']:
                graph[artist_name_to_num[artist_name]][artist_name_to_num[other_artist]] += 1
                graph[artist_name_to_num[other_artist]][artist_name_to_num[artist_name]] += 1


# f1 = open('graph.txt','w',encoding="utf-8")
# print(repr(graph),file=f1)




# for review in data:
#     for artist in review['artist']:
#         for related_artist in review['artistLinks']:
#             graph[artist_name_to_num[artist]][artist_name_to_num[related_artist]] += 1
#             graph[artist_name_to_num[related_artist]][artist_name_to_num[artist]] += 1

# num = artist_name_to_num['Radiohead']
# print([(num_to_artist_name[i], graph[num][i]) for i in range(cnt+2) if graph[num][i] > 0])





        


