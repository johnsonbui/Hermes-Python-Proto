'''
@author: Johnson Bui
'''
import nltk as nk

from nltk import *
# List sorted list of Titles (propers)
strTitle = sorted(word for word in set(text6) if word.istitle() and word.startswith("R"))
# How about just the upper words in appearance
strUpOrd = [word.upper() for word in text4]

