import abc
from dataset.datasource.datasource import DataSource
from dataset.output.output import DataOutput


class Dataset(object, metaclass=abc.ABCMeta):
    def __init__(self, datasource: DataSource, output: DataOutput):
        self.datasource = datasource
        self.output = output

    @abc.abstractmethod
    def _read_to_memory(self) -> dict:
        raise NotImplementedError("Need to define this method")

    def refresh(self):
        self.datasource.process()
        self.output.commit(self._read_to_memory())
        self.datasource.delete_tmp_file()

    def fetch_all(self) -> dict:
        return self.output.get_all()
