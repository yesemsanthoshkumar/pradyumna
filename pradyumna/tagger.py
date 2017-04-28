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
                (r'[0-9]+[.0-9]{,1}', "NUM"),         # Numbers      ==> 32.85, 300
                (r'am|is|was|are|were', "BVRB"),    # Be verbs,
                (r'\w+[fl]y', "VB"),                     # Adjectives   ==> beautify
                (r'\w+ness', "NN"),                  # Noun      ==> effectiveness
                (r'\w+', "NN"),                      # Any word
    ]

    for regex, tag in pos_regex:
        if re.match(regex, token.strip()):
            return tag
        else:
            continue

    return "NN"
