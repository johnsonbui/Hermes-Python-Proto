# This example uses choice to choose from possible expansions
from random import choice
# This function is based on _generate_all() in nltk.parse.generate
# It therefore assumes the same import environment otherwise.

demo_grammar = """
  S -> NP VP
  NP -> Det N
  PP -> P NP
  VP -> 'slept' | 'saw' NP | 'walked' PP
  Det -> 'the' | 'a'
  N -> 'man' | 'park' | 'dog'
  P -> 'in' | 'with'
"""


# Use in conjunction with core_functions -> first part of cfdCrossGenre
# Should be able to generate a list of the words that we can use for passing through this with that
# Better Yet! Can probably pass bigrams through this
def generate_sample(grammar, items=["S"]):
    frags = []
    if len(items) == 1:
        if isinstance(items[0], Nonterminal):
            for prod in grammar.productions(lhs=items[0]):
                frags.append(generate_sample(grammar, prod.rhs()))
        else:
            frags.append(items[0])
    else:
        # This is where we need to make our changes
        chosen_expansion = choice(items)
        frags.append(generate_sample,chosen_expansion)
    return frags
