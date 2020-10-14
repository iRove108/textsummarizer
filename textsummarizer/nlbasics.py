import nltk
from pprint import pprint

# Tokenizing text
text = input ("Enter your text to tokenize here: ")
from nltk.tokenize import word_tokenize, sent_tokenize

sents=sent_tokenize(text)
print(sents)

words=[word_tokenize(sent) for sent in sents]
print(words)

# Removing stopwords
from nltk.corpus import stopwords
from string import punctuation
customStopWords=set(stopwords.words('english')+list(punctuation))
wordsWOStopwords=[word for word in word_tokenize(text) if word not in customStopWords]
print(wordsWOStopwords)

#Identifying bigrams
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(wordsWOStopwords)
print(finder.ngram_fd.items())

# Stemming
text2 = input ("Enter your text to stem and identify POS here: ")
from nltk.stem.lancaster import LancasterStemmer
st = LancasterStemmer()
stemmedWords = [st.stem(word) for word in word_tokenize(text2)]
print(stemmedWords)

# POS Tagging
tagList = nltk.pos_tag(word_tokenize(text2))
pprint(tagList)
