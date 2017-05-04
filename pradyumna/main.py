"""
Pradyumna
__author__: yesemsanthoshkumar
"""

from pymongo import MongoClient
import spacy
from py2neo import authenticate, Graph, Node, Relationship

from config import CONFIG
from sentence_segmentation import sentence_segmentation

MG_CLIENT = MongoClient("mongodb://localhost//27017")

#   Assuming the database name as news
DB_NAME = CONFIG["mongodb"]["database name"]
DB = MG_CLIENT[DB_NAME]
if CONFIG["mongodb"]["collections"] == "SYS_COLLECTIONS":
    COLLECTIONS = DB.collection_names(include_system_collections=False)
else:
    COLLECTIONS = CONFIG["mongodb"]["collections"]

ENGINE = spacy.load('en')

NEO_AUTH = authenticate(
    CONFIG["neo4j"]["database url"] + ":" + CONFIG["neo4j"]["port"],
    CONFIG["neo4j"]["username"],
    CONFIG["neo4j"]["password"])
graph = Graph("http://localhost:7474")


class DepTree(object):
    """docstring for DepTree."""
    def __init__(self, sent):
        super(DepTree, self).__init__()
        # A SPACY SPAN OBJECT
        self.sentence = sent

    def GraphCreate(self):
        """Create graph from the sentence"""
        for chunk in self.sentence.noun_chunks:
            curr_node = Node("PHRASE", name=chunk.text)
            root_node = Node("PHRASE", name=chunk.root.head.text)
            rel = Relationship(curr_node, chunk.root.dep_, root_node)
            graph.create(rel)

for collection in COLLECTIONS:
    for document in DB[collection].find():
        #   Assuming the text is present in the content field of the document
        parsed_doc = sentence_segmentation(document['content'])
        for sentence in parsed_doc:
            d_tree = DepTree(ENGINE(sentence))
            d_tree.GraphCreate()
            # print(sentence)
