"""Module to find tf-idf of from a set of documents"""

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

def tf_idf(documents, threshhold):
    """Computes tf-idf for the given set of documents and return the words
    above the given threshhold

    Parameters
    ----------
    documents   :   list
        A list of documents to use for the tf-idf

    threshold   :   float
        The threshold value to filter for the tf_idf. Only the words with the
        value above or equal to this threshold will be returned
    """
    tf_idf_vect = TfidfVectorizer(
        input=documents,
        encoding='utf-8',
        analyzer='word',
        stop_words=stopwords.words('english'),
        smooth_idf=False
    )
    tf_idf_vect.fit_transform(documents)
    print(tf_idf_vect.fit_transform(documents).todense())
    return tf_idf_vect.fit_transform(documents)
