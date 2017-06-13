"""Part of speech tagging for tokens"""

from nltk import pos_tag

def pos_tagger(token_list):
    """Takes a sentence as input and tags tokens with its part of speech

        Parameters
        ----------
        token_list  :   List of tokens to tag its part-of-speech
    """
    return pos_tag(token_list)
