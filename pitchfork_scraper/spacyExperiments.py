from spacy.lemmatizer import Lemmatizer
from nltk.stem import WordNetLemmatizer
from spacy.lang.en import LEMMA_INDEX, LEMMA_EXC, LEMMA_RULES
# import enchant
lemmatizer = Lemmatizer(LEMMA_INDEX, LEMMA_EXC, LEMMA_RULES)

from nltk.corpus import wordnet as wn
nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
adverbs = {x.name().split('.', 1)[0] for x in wn.all_synsets('r')}
verbs = {x.name().split('.', 1)[0] for x in wn.all_synsets('v')}
adjs = {x.name().split('.', 1)[0] for x in wn.all_synsets('a')}



wnl = WordNetLemmatizer()

print(lemmatizer('riding','ADV'))
print(wnl.lemmatize('bridges'))

print("suffering" in verbs)
t = ['hello']

ride = lemmatizer('riding','VERB')[0]
print(ride)
print(ride in verbs)
# d = enchant.Dict("en_US")
# d.check("blindsided")

def get_base_form(word: str):
    word = word.lower()
    if word in adjs:
        return word
    if word in adverbs:
        return word
    nouncopy = lemmatizer(word,'NOUN')[0]
    verbcopy = lemmatizer(word,'VERB')[0]
    if verbcopy in verbs:
        return verbcopy
    if nouncopy in nouns:
        return nouncopy
    return word
    # if copyword in verbs:
    #     return copyword
    # return word




# from spacy.lang.en import English

# nlp = English()

# doc = nlp("He has been living in the U.K. for quite a long time now. I haven't met him since 1994!")
# for token in doc:
#     print(token.text)