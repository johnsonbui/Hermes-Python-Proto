'''
@author: Johnson Bui
'''
import nltk as nk

from nltk import *

# Chapter 2 test on Sort, token and neg slice ##########################################
saying = ['After', 'all', 'is', 'said', 'and', 'done', 'more', 'is', 'said', 'than', 'done']
tokens = set(saying)
tokens = sorted(tokens)
tokens[-2:]
#print(tokens)

# Frequency Distribution Test ###############################
fdist1 = FreqDist(text1)
#print(fdist1)
most = fdist1.most_common(10)
whale = fdist1["whale"]
#print(most)
#print(FreqDist(text2)["sense"])

# Top 7 seven "words"
#fdist1.plot(7, cumulative=True)

# Pairs of Usage
#print(text2.common_contexts(["Good", "morning"]))

# One time occurences
#print(fdist1.hapaxes())

# Fine grain selection of words #########################
V = set(text1)
wordsOver15 = [w for w in V if len(w) > 15]
sorted15 = sorted(wordsOver15)

# Find common words with under 8 letters and occurring over 12 times
fdist5 = FreqDist(text5)
sortedUnder8 = sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 12)

# Generate Bigrams ##################################
wordPairs = list(bigrams(['more', 'is', 'said', 'than', 'done']))
#moreFreqBigrams = text4.collocations()


# Counting ######################

wordLen = [len(w) for w in text7]
fDist7 = FreqDist(len(w) for w in text7)
fDist7text = FreqDist(text7)
most7 = fDist7text.most_common(10)
#print(fDist7)
