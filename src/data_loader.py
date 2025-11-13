import pandas as pd
from pathlib import Path

class DataLoader:
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)

    def load_csv(self, filename: str) -> pd.DataFrame:
        file_path = self.data_path / filename
        if not file_path.exists():
            raise FileNotFoundError(f"{file_path} not found.")
        df = pd.read_csv(file_path)
        print(f"Loaded {filename} with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df

    def list_csv_files(self):
        files = list(self.data_path.glob("*.csv"))
        return [f.name for f in files]
