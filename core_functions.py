''' 
@author: Johnson Bui 
'''
import string as st

from nltk.book import *
from nltk.corpus import *
from matplotlib import pylab

''' Welcome to my mess. '''
def core_status():
    """ I hope this is never broken. """
    return "Hello! My core is not broken at this moment. Please try again later!"

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    percent = 100 * count / total
    return percent, "%"

def read_suffix_ING(text):
    for line in text:
        for word in line.split():
            if word.endswith('ing'):
                return word

def generate_model(conditional_frequency_distribution, word, num):
    for i in range(num):
        print(word, end=' ')
        word = conditional_frequency_distribution[word].max()

# Remove punct, lower, split, sort, and tokenize ##########################################
phrase = "After all is done and said, more is said than done."

def convertToSetOfFlatTokens(phrase):
    # Remove puntuation for the whole phrase
    translator = str.maketrans('', '', st.punctuation)
    phrase = phrase.translate(translator)
    # Lower to later conform words to same set
    phrase = phrase.lower()
    # Split by space
    phrase = phrase.split(' ')
    # Tokenize for digest
    tokens = set(phrase)
    # Sort by alpha 
    tokens = sorted(tokens)
    print(tokens)

# Simpler way to find Number of Occurrences for a specific word
# print(FreqDist(text2)["sense"])

# Frequency Distribution Test ###############################
textGiven = text1
specificString = 'grail'

def findMostCFD(textGiven, topNum, specificString):
    # Not precise results yet, need to find way to convert nltk.text.Text to string
    # Lower and find freqDist of text given
    textGiven = (word.lower() for word in textGiven if word.isalpha())
    fdist = FreqDist(textGiven)
    # Find given number of top words
    most = fdist.most_common(topNum)
    # Give appearances for specific word
    specificDist = fdist[specificString]
    print("{} \n Top {} Words: {} \n The word '{}' appears {} time(s).".format(fdist, topNum, most, specificString, specificDist))
    


# Top 7 seven "words"

def plotForMe(textGiven, topNum):
    fdist = FreqDist(textGiven)
    fdist.plot(topNum, cumulative=True)

# Remove non-alphanumeric characters from texts
def countVocab(textGiven):
    text = len(set(word.lower() for word in textGiven if word.isalpha()))
    print(text)

# Finish with tokenization later
# def cleanText(text):
    

# Pairs of Usage
# print(text2.common_contexts(["Good", "morning"]))

# Generate similar words based on given word parts and given text
def similarWords(textGiven, wordPart):
    similarWords = sorted(w for w in set(textGiven) if wordPart in w)
    for word in similarWords:
        print(word, end=' ')

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


def dPlot(textGiven,string1, string2): 
    graph = textGiven.dispersion_plot([string1, string2])
    occur1 = textGiven.count(string1)
    occur2 = textGiven.count(string2)
    print("{} \n {} occurs {} time(s) and {} occurs {} time(s)".format(graph, string1, occur1, string2, occur2))

# Find Distribution of Stylistic Words
style = ['who', 'what', 'when', 'where', 'why']

def findStyle_News(style):
    text = brown.words(categories='news')
    fdist = FreqDist(w.lower() for w in text)
    
    for s in style:
        print(s + ':', fdist[s], end=' ')
        
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']

def cfdPair(genre, word):
    cfd = ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories=genre))
    cfd.tabulate(conditions=genres, samples=modals)


# can only be used with brown categories for now
# change to later assess top words that are not prepositions
def cfdCrossGenre(textGiven, topNum):
    textGiven = (w.lower() for w in textGiven if w.isalpha())
    fdist = FreqDist(textGiven)
    most = fdist.most_common(topNum)
    
    aCommon = []   
    iMax = len(most)
    
    for i in range(iMax):
        aMost = most[i]
        aCommon += [aMost[0]]
    # print(aCommon)
        
    genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']  
    # Compare list of words to list of genre
    cfd = ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories=genre))
    cfd.tabulate(conditions=genres, samples=aCommon)
    
# Plot use of america and citizen over time for inaugural speeches
# Known working variables
word1 = 'america'
word2 = 'citizen'
textSet = inaugural
def plotUseOverTime(textSet, word1, words2):
    cfd = ConditionalFreqDist((target, fileid[:4]) for fileid in textSet.fileids() for w in textSet.words(fileid) for target in [word1, word2] if w.lower().startswith(target))
    cfd.plot()


    

    
    
    