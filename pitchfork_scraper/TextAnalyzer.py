import re
import typing
from nltk.stem import WordNetLemmatizer
from spacy.lemmatizer import Lemmatizer
from spacy.lang.en import LEMMA_INDEX, LEMMA_EXC, LEMMA_RULES
lemmatizer = Lemmatizer(LEMMA_INDEX, LEMMA_EXC, LEMMA_RULES)
from nltk.corpus import words

from nltk.corpus import wordnet as wn
nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
adverbs = {x.name().split('.', 1)[0] for x in wn.all_synsets('r')}
verbs = {x.name().split('.', 1)[0] for x in wn.all_synsets('v')}
adjs = {x.name().split('.', 1)[0] for x in wn.all_synsets('a')}

wnl = WordNetLemmatizer()

from functools import lru_cache
memoize = lru_cache(None)
@memoize
def get_base_form(word: str):
    word = word.lower()
    if word in adjs:
        return word
    if word in adverbs:
        return word
    nouncopy = wnl.lemmatize(word)
    verbcopy = lemmatizer(word,'VERB')[0]
    if verbcopy in verbs:
        return verbcopy
    if nouncopy in nouns:
        return nouncopy
    return word


eightPlus = open("EightPlusWholeText.txt",encoding="utf-8").read()
# print(processedText[10].text)

'''splits the entire text into a list of words'''
textList = re.findall(r'\w+', eightPlus)
# copyTextList = textList.copy()

occurence = {}

# wordset = set()

for word in textList:
    w = get_base_form(word.lower())
    occurence[w] = 0

print("HEY")

for word in textList:
    occurence[get_base_form(word.lower())] += 1

sorted_dict = sorted(occurence.items(), key = lambda x : x[1], reverse=True)

# print(sorted_dict)

f = open('out6.txt','w',encoding="utf-8")
print(*sorted_dict,sep = "\n",file=f)

# textset = {'it'}
# for word in textList:
#     textset.add(lemmatizer.lemmatize(word.lower()))

# print(len(textset))

# f = open('out.txt','w',encoding="utf-8")
# print("lemmatized",file=f)
# for word in textset:
#     print(word,file=f)