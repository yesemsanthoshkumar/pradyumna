"""Module that starts the pipeline"""

__author__ = "yesemsanthoshkumar"
__version__ = "0.0.1"

from pymongo import MongoClient
from config import CONFIG
from sentence_segmentation import sentence_segmentation
from tokenizer import word_tokenization
from tagger import pos_tagger
from tf_idf.tf_idf import tf_idf

MG_CLIENT = MongoClient("mongodb://localhost//27017")

DB_NAME = CONFIG["mongodb"]["database name"]
DB_ = MG_CLIENT[DB_NAME]
COLLECTIONS_ = DB_.collection_names(include_system_collections=False)

docs = list()
for collection in COLLECTIONS_:
    for document in DB_[collection].find():
        docs.append(document["content"])
    print(tf_idf(
        docs,
        0.5
    ))
    print("==" * 10)
    break
