"""Module that starts the pipeline"""

__author__ = "yesemsanthoshkumar"
__version__ = "0.0.1"

import pandas as pd

from pymongo import MongoClient
from vectorizer.tf_idf import tf_idf

MG_CLIENT = MongoClient("mongodb://localhost//27017")

DB_ = MG_CLIENT["news_docs"]

docs = list()
df = pd.DataFrame(columns=["document"])
for document in DB_["news"].find():
    features, matrix = tf_idf([document["content"]])
    temp_df = pd.DataFrame(matrix.todense()[0], columns=features)
    temp_df["document"] = document["_id"]
    df = df.append(temp_df, ignore_index=True)
    # print(df.shape)
# print(df.head())
