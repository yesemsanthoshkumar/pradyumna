"""
Part of speech tagging for tokens
"""

import re

def tagger(token):
    """Takes a token as input and tags it with its part of speech

        Parameters
        ----------
        token       Input word to tag for its part of speech
    """
    pos_regex = [
                (r'[0-9]+[\.0-9]*', "NUM")      # Numbers
                (r'\w+', "WD")                  # Any word
    ]

    if re.match(token, pos_regex[0][0]):
        return pos_regex[0][1]
    else:
        return pos_regex[1][1]
