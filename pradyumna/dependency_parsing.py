"""Dependency parsing module"""

from .utils import NodeObj

def parse_dependency(word_tag_list):
    """Parses dependency of the list of word tag tuples

    Parameters
    ----------
    word_tag_list   :   list
        List of tuples composing a token/word and its part-of-speech tag
    """
    current_node = None
    next_node = None

    for word, tag in word_tag_list:
        current_node = NodeObj(word, tag)
        if not next_node:
            next_node = current_node
        # Finish this dependdency parser
    else:
        pass