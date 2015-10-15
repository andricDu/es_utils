import json
from elasticsearch import Elasticsearch
import progressbar
from config import *

__author__ = 'andricDu'

def read_json_dump():
    print('Finding File...')
    global hits
    with open(conf_file_path) as data_file:
        print('Starting JSON Loading...')
        data = json.load(data_file)
        hits = data['hits']['hits']


def bootstrap_local_es():
    global es_local
    print('Bootstrapping ES')
    es_local = Elasticsearch(hosts=conf_hosts)
    es_local.indices.delete(index=conf_index, ignore=[400, 404])
    es_local.indices.create(index=conf_index)


def index_hits():
    global hits
    print('\nLoading Documents')
    progress = progressbar.ProgressBar(max_value=len(hits))
    count = 0
    for hit in hits:
        es_local.index(index=conf_index, doc_type=hit['_type'], body=hit['_source'], id=hit['_id'])
        count += 1
        progress.update(count)


def run():
    bootstrap_local_es()
    read_json_dump()
    index_hits()

run()
