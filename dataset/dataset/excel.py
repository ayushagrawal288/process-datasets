import pandas as pd
from dataset.dataset.dataset import Dataset
from dataset.datasource.datasource import DataSource
from dataset.output.output import DataOutput


class Excel(Dataset):
    def __init__(self, datasource: DataSource, output: DataOutput, sheet_name=0):
        super().__init__(datasource, output)
        self.sheet_name = sheet_name

    def _read_to_memory(self) -> dict:
        df = pd.read_excel(self.datasource.get_file_path(), sheet_name=self.sheet_name).to_dict()
        return df
