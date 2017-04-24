'''
@author: Johnson Bui
'''

from nltk.book import *
from nltk.corpus import *
from nltk.tag import pos_tag_sents
from matplotlib import pylab

# Test Code to verify integrity of twitter samples
'''
# Displays the files in the sample
twitter.samples.fileids()

# Verifies the text involved
twitter_samples.strings('tweets.20150430-223406.json')

'''

# Break text down to essentials (nouns, adjectives)

tweets = twitter_samples.strings('positive_tweets.json')
tweets_tokens = twitter_samples.tokenized('positive_tweets.json')
tweets_tagged = pos_tag_sents(tweets_tokens)



def countTags(): 
    
    singNoun_count = 0
    plurNoun_count = 0
    adj_count = 0    
    
    for tweet in tweets_tagged:
        for pair in tweet:
            tag = pair[1]
            if tag == 'JJ':
                adj_count += 1
            elif tag == 'NN':
                singNoun_count += 1
            elif tag == 'NNS':
                plurNoun_count += 1
                
    print ("Adjectives: {0}\nSingular Nouns: {1}\nPlural Nouns: {2}".format(adj_count, singNoun_count, plurNoun_count))
