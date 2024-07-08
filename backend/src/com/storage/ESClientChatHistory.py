from backend.src.com.storage.ESClient import ESClient


class ESClientChatHistory:
    def __init__(self):
        self.index = "chat-history"
        self.es = ESClient().get_esclient()



