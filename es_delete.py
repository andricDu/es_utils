from elasticsearch import Elasticsearch
from config import *

__author__ = 'andricDu'


def bootstrap_local_es():
    global es_local
    print('Bootstrapping ES')
    es_local = Elasticsearch(hosts=conf_hosts)


def delete(query):

    response = es_local.search(index=conf_index, body=query)
    hits = response['hits']['hits']
    print(len(hits))

    for hit in hits:
        es_local.delete(index=conf_index, id=hit['_id'], doc_type=hit['_type'])


def run():
    bootstrap_local_es()
    delete(conf_delete_query)

run()
