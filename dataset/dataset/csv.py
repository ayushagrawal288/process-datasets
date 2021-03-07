import pandas as pd
from dataset.dataset.dataset import Dataset
from dataset.datasource.datasource import DataSource
from dataset.output.output import DataOutput


class CSV(Dataset):
    def __init__(self, datasource: DataSource, output: DataOutput, delimiter=","):
        super().__init__(datasource, output)
        self.delimiter = delimiter

    def _read_to_memory(self) -> dict:
        df = pd.read_csv(self.datasource.get_file_path(), delimiter=self.delimiter).to_dict()
        return df
