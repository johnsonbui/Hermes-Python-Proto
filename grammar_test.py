'''
@author: Johnson Bui
'''

from nltk.parse.generate import generate #, demo_grammar
from nltk import CFG


demo_grammar = """
  S -> NP VP
  NP -> Det N
  PP -> P NP
  VP -> 'slept' | 'saw' NP | 'walked' PP
  Det -> 'the' | 'a'
  N -> 'man' | 'park' | 'dog'
  P -> 'in' | 'with'
"""
grammar = CFG.fromstring(demo_grammar)
print(grammar)


#Join words and generate based off of grammar - for n 
for sentence in generate(grammar, n=12):
    print(' '.join(sentence))

'''
Notes: 
Need to symbolize the grammar
Have the machine process the language
Need to integrate with Markov chain - file 'agiliq-markov.py'
'''
for sentence in generate(grammar, depth=4):
    print(' '.join(sentence))
    
