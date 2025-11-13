import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def fill_missing_with_median(self):
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            median_val = self.df[col].median()
            self.df[col].fillna(median_val, inplace=True)
            print(f"Filled missing values in {col} with median {round(median_val, 2)}")
        return self

    def remove_outliers(self, z_thresh=3):
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        z_scores = np.abs((self.df[numeric_cols] - self.df[numeric_cols].mean()) / self.df[numeric_cols].std())
        mask = (z_scores < z_thresh).all(axis=1)
        removed = len(self.df) - sum(mask)
        self.df = self.df[mask]
        print(f"Removed {removed} outlier rows using Z-threshold {z_thresh}.")
        return self

    def clean_column_names(self):
        self.df.columns = [col.strip().replace(" ", "_") for col in self.df.columns]
        return self

    def save_cleaned(self, output_path: str):
        self.df.to_csv(output_path, index=False)
        print(f"Saved cleaned dataset to {output_path}")

    def summary_report(self):
        summary = {
            "rows": len(self.df),
            "columns": list(self.df.columns),
            "missing_values": self.df.isna().sum().to_dict(),
        }
        return summary
