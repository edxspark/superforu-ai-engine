from backend.src.com.storage.ESClient import ESClient
from backend.src.com.storage.mappings import Mappings


class ESClientKmFile:
    def __init__(self):
        self.index = "km-files"
        self.es = ESClient().get_esclient()
        if not self.es.indices.exists(index=self.index):
            self.es.indices.create(
                index=self.index,
                mappings=Mappings.km_files_mappings
            )




