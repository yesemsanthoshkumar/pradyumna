"""Utilities"""

class NodeObj(object):
    """Represents a dependency parsing node"""

    _dependency = list()

    def __init__(self, word, tag):
        self.word = word
        self.tag = tag

    def add_dependency(self, another_node):
        """Adds another nodeobj as a dependency relation to this nodeobj

        Parameters
        ----------
        another_node    :   NodeObj
            The nodeobj object to add as a dependency
        """
        self._dependency.append(another_node)
