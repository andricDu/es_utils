import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es_host = ''
index_name = 'terms-lookup'


def read_json_dump():
    with open('/home/dandric/terms-lookup-1.json') as data_file:
        print('Starting JSON Loading...')
        data = json.load(data_file)
        hits = data['hits']['hits']
        return hits


def bootstrap_es():
    es = Elasticsearch(hosts=[es_host])
    return es


def hit_to_action(hit):
    return {
        '_index': index_name,
        '_type': hit['_type'],
        '_id': hit['_id'],
        '_source': hit['_source']
    }


def index_hits(es, hits):
    print('Starting Bulk Index')
    actions = map(hit_to_action, hits)
    helpers.bulk(es, actions, max_retries=5, request_timeout=120)


def run():
    hits = read_json_dump()
    es = bootstrap_es()
    index_hits(es, hits)


run()
