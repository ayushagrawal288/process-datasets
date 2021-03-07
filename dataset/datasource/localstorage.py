import os
from dataset.datasource.datasource import DataSource
from shutil import copy2


class LocalStorage(DataSource):
    def __init__(self, filepath, filename, tmp_directory=None):
        if tmp_directory:
            super().__init__(filename, tmp_directory)
        else:
            super().__init__(filename)
        self.filepath = filepath

    def process(self):
        cur_directory = os.path.join(self.filepath, self.filename)
        copy2(cur_directory, self.get_file_path())
