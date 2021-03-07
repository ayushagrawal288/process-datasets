import os
from pandas import DataFrame, read_csv
from dataset.output.output import DataOutput
from pathlib import Path


class LocalStorageOutputCSV(DataOutput):
    def __init__(self, filename: str, path="./out/", delimiter=","):
        super().__init__()
        self.path = path
        self.filename = filename
        self.delimiter = delimiter

    def _to_file_path(self):
        Path(self.path).mkdir(parents=True, exist_ok=True)
        filename = ".".join(self.filename.split(".")[:-1]) + ".csv"
        return os.path.join(self.path + filename)

    def commit(self, data: dict):
        df = DataFrame(data)
        df.to_csv(self._to_file_path(), header=True, index=False)

    def get_all(self) -> dict:
        df = read_csv(self._to_file_path(), delimiter=self.delimiter).to_dict()
        return df
