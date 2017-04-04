"""
Pradyumna
__author__: yesemsanthoshkumar
"""

from pymongo import MongoClient
import spacy
from py2neo import Graph, Node, Relationship

mongo_python = MongoClient("mongodb://localhost//27017")

#Assuming the database name as news
db = mongo_python.news
db_collections = db.collection_names(include_system_collections = False)

engine = spacy.load('en')

username = input("Enter neo4j username: ")
password = input("Enter your password: ")
graph = Graph("http://" + username + ":" + password + "@localhost:7474")

class DepTree(object):
    """docstring for DepTree."""
    def __init__(self, sentence):
        super(DepTree, self).__init__()
        self.sentence = sentence # A SPACY SPAN OBJECT

    def GraphCreate(self):
        for chunk in self.sentence.noun_chunks:
            curr_node = Node("PHRASE", name=chunk.text)
            root_node = Node("PHRASE", name=chunk.root.head.text)
            rel = Relationship(curr_node, chunk.root.dep_, root_node)
            graph.create(rel)

for collection in db_collections:
    for document in db[collection].find().limit(2):
        parsed_doc = engine(document['content'])    # Assuming the text is present in the content field of the document
        for sentence in parsed_doc.sents:
            d_tree = DepTree(engine(sentence.text))
            d_tree.GraphCreate()
