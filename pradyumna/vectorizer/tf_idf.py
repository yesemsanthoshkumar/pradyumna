"""Module to find tf-idf of from a set of documents"""

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

def tf_idf(documents):
    """Computes tf-idf for the given set of documents and return the words
    above the given threshhold

    Parameters
    ----------
    documents   :   list
        A list of documents to use for the tf-idf
    """
    tf_idf_vect = TfidfVectorizer(
        input=documents,
        encoding='utf-8',
        analyzer='word',
        stop_words=stopwords.words('english'),
        smooth_idf=False
    )
    sparse_mat = tf_idf_vect.fit_transform(documents)
    return sparse_mat
