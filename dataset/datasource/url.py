from urllib.request import urlretrieve
from dataset.datasource.datasource import DataSource


class URL(DataSource):
    def __init__(self, url, filename):
        super().__init__(filename)
        self.url = url

    def process(self):
        urlretrieve(self.url, self.get_file_path())
