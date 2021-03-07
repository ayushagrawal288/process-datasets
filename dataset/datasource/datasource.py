import abc
import os
from pathlib import Path


class DataSource(object, metaclass=abc.ABCMeta):

    def __init__(self, filename, directory='./tmp/'):
        self.filename = filename
        self.directory = directory

    def get_file_path(self):
        Path(self.directory).mkdir(parents=True, exist_ok=True)

        return os.path.join(self.directory, self.filename)

    @abc.abstractmethod
    def process(self):
        raise NotImplementedError("Need to define this method")

    def delete_tmp_file(self):
        file_to_rem = Path(self.get_file_path())
        file_to_rem.unlink(missing_ok=True)
