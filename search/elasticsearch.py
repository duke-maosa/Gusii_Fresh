# search/elasticsearch.py

from elasticsearch_dsl import Document, Text

from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['localhost'])  # Update with your Elasticsearch host

class ProductIndex(Document):
    name = Text()
    description = Text()

    class Index:
        name = 'product_index'

class SellerIndex(Document):
    name = Text()

    class Index:
        name = 'seller_index'

class BuyerIndex(Document):
    name = Text()

    class Index:
        name = 'buyer_index'
