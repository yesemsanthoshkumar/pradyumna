"""Sentence segmentation for documents"""


def sentence_segmentation(paragraph):
    """Takes a paragraph or a document and yields sentences

        Parameters
        ----------
        paragraph       A multiline string that represents a document of information
    """
    for sentence in paragraph.split("."):
        yield sentence.strip()
