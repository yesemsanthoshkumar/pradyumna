"""Pradyumna - A friendly bot"""

__author__ = "yesemsanthoshkumar"
__version__ = "0.0.1"

import pandas as pd

from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

MG_CLIENT = MongoClient("mongodb://localhost//27017")

DB_ = MG_CLIENT["news_docs"]
MODEL = TfidfVectorizer()
DF = pd.DataFrame()
ANSWERING_MODEL = RandomForestClassifier()

def generate_matrix():
    """Generates a dataframe with tfidf vectors from the news documents

    Returns
    ----------
    all_df  :   pandas.DataFrame
        The dataframe with the tfidf vectors as features
    """
    ids = []
    cont = []
    for doc in DB_['news'].find().limit(50):
        ids.append(doc['_id'])
        print(doc["data_section"])
        cont.append(doc['content'])
    trans_content = MODEL.fit_transform(cont)
    id_frame = pd.DataFrame({'_doc_': ids})
    cont_frame = pd.DataFrame(trans_content.todense(), columns=MODEL.get_feature_names())
    df =  pd.concat([id_frame, cont_frame], axis=1).reset_index(drop=True)
    return df

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
    inp = MODEL.transform([usr_input])
    doc_index = ANSWERING_MODEL.predict(inp.todense())
    add_to_response = DB_['news'].find_one({
        '_id': DF.iloc[doc_index]['_doc_'].values[0]
    })['content']
    return add_to_response

if __name__ == "__main__":
    DF = generate_matrix()
    features = list(DF.columns)
    features.remove('_doc_')
    ANSWERING_MODEL.fit(DF[features], DF.index)
    awake_bot()
