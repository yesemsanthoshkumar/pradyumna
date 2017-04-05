"""
Sentence segmentation for documents
"""


def sentence_segmentation(paragraph):
    """Takes a paragraph or a document and yields sentences"""
    for sentence in paragraph.split("."):
        yield sentence.strip()
