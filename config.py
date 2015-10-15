__author__ = 'andricDu'


# CONFIGURATION
conf_index = 'test-index'

conf_file_path = 'test.json'
conf_hosts = ['localhost:9200']

conf_delete_query = {
    'size': 1000,
    'query': {
        'term': {'FIELD': 'VALUE'}
    }
}