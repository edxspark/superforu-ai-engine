import os

import dotenv
import requests
dotenv.load_dotenv()

NDB_HOST = os.getenv("NDB_HOST")
NDB_PORT = os.getenv("NDB_PORT")

NDB_API_TOKEN = os.getenv("NDB_API_TOKEN")
NDB_PROJECT = os.getenv("NDB_PROJECT")


class NocoDB:
    @staticmethod
    def get(api_path, params):
        url = "{}:{}{}".format(NDB_HOST, NDB_PORT, api_path)
        print("#####Nocodb.get={}".format(url))
        return requests.get(url, headers={"xc-token": NDB_API_TOKEN}, params=params)

    @staticmethod
    def post(api_path, params):
        url = "{}:{}{}".format(NDB_HOST, NDB_PORT, api_path)
        print("#####NocodbHttpClient.post.url={}".format(url))
        return requests.get(url, headers={"xc-token": NDB_API_TOKEN,"Content-Type": "application/json"}, params=params)

