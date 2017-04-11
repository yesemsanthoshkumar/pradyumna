"""
Pradyumna
__author__: yesemsanthoshkumar
"""

from pymongo import MongoClient
import spacy
from py2neo import authenticate, Graph, Node, Relationship

from sentence_segmentation import sentence_segmentation

mongo_python = MongoClient("mongodb://localhost//27017")

#   Assuming the database name as news
db = mongo_python.news
db_collections = db.collection_names(include_system_collections=False)

engine = spacy.load('en')

username = input("Enter neo4j username: ")
password = input("Enter your password: ")
neo_auth = authenticate("localhost:7474", username, password)
graph = Graph("http://localhost:7474")


class DepTree(object):
    """docstring for DepTree."""
    def __init__(self, sent):
        super(DepTree, self).__init__()
        # A SPACY SPAN OBJECT
        self.sentence = sent

    def graphCreate(self):
        """Create graph from the sentence"""
        for chunk in self.sentence.noun_chunks:
            curr_node = Node("PHRASE", name=chunk.text)
            root_node = Node("PHRASE", name=chunk.root.head.text)
            rel = Relationship(curr_node, chunk.root.dep_, root_node)
            graph.create(rel)

for collection in db_collections:
    for document in db[collection].find():
        #   Assuming the text is present in the content field of the document
        parsed_doc = sentence_segmentation(document['content'])
        for sentence in parsed_doc:
            d_tree = DepTree(engine(sentence))
            d_tree.GraphCreate()
            # print(sentence)
