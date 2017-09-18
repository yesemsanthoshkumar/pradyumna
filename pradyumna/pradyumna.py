"""Pradyumna - A friendly bot"""

__author__ = "yesemsanthoshkumar"
__version__ = "0.0.1"

import pandas as pd

from pymongo import MongoClient
from vectorizer.tf_idf import tf_idf
from sklearn.cluster import KMeans

MG_CLIENT = MongoClient("mongodb://localhost//27017")

DB_ = MG_CLIENT["news_docs"]

def generate_matrix():
    """Generates a dataframe with tfidf vectors from the news documents

    Returns
    ----------
    all_df  :   pandas.DataFrame
        The dataframe with the tfidf vectors as features
    """
    ids = []
    cont = []
    for doc in DB_['news'].find().limit(10):
        ids.append(doc['_id'])
        cont.append(doc['content'])
    df = pd.DataFrame({'_doc_': ids})
    cont_df = pd.DataFrame(tf_idf(cont).todense())
    all_df = pd.concat([df, cont_df], axis=1)
    return all_df

def train_model(data):
    """Train a cluster model from the dataframe

    Parameters
    ----------
    data    :   pandas.DataFrame
        The dataframe with the document id and tfidf vectorizer output as features
    """
    kmns = KMeans()
    cols = list(data.columns)
    cols.remove('_doc_')
    model = kmns.fit_transform(data[cols])
    return model

def awake_bot():
    """Wake up the bot and starts the conversation. My bot loves to sleep :P"""
    print("Yes Boss!")
    usr_input = None
    while usr_input != 'exit':
        print("Human: ", end='')
        usr_input = input()
        print("Pradyumna: ", end='')
        print(generate_response(usr_input))

def generate_response(usr_input):
    """Generates response for the obtained human input"""
    return "I feel sleepy..."

if __name__ == "__main__":
    DF = generate_matrix()
    MODEL = train_model(DF)
    awake_bot()
