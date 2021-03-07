import json
from dataset.dataset.dataset import Dataset
from dataset.datasource.datasource import DataSource
from dataset.output.output import DataOutput


class JSON(Dataset):
    def __init__(self, datasource: DataSource, output: DataOutput, delimiter=","):
        super().__init__(datasource, output)
        self.delimiter = delimiter

    def _read_to_memory(self) -> dict:
        with open(self.datasource.get_file_path(), 'r') as file:
            data = json.load(file)
            return data
