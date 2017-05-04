"""
Part of speech tagging for tokens
"""

import re
from nltk import pos_tag

from tokenizer import word_tokenization

def tagger(sentence):
    """Takes a sentence as input and tags tokens with its part of speech

        Parameters
        ----------
        sentence       Input sentence to tag for its part of speech
    """
    tok_sentence = word_tokenization(sentence)

    return pos_tag(tok_sentence)
