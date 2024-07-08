import os
import dotenv

from elasticsearch import Elasticsearch
from backend.src.com.storage.mappings import Mappings

dotenv.load_dotenv()

ES_URL = os.getenv("ES_URL")
ES_USER_NAME = os.getenv("ES_USER_NAME")
ES_PASSWORD = os.getenv("ES_PASSWORD")


class ESClient:
    def __init__(self):
        self.es = Elasticsearch(ES_URL, basic_auth=(ES_USER_NAME, ES_PASSWORD))

    def get_esclient(self):
        return self.es


