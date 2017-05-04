"""
Tokenizer
"""

def word_tokenization(sentence):
    """Tokenizer function that takes a sentence and returns tokens

        Parameters
        ----------
        sentence        A string that represents a sentence in a document
    """
    return sentence.split(" ")
