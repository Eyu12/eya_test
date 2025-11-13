import pandas as pd

def load_data(country):
    path_map = {
        "Benin": "../data/benin_clean.csv",
        "Sierra Leone": "../data/sierraleone_clean.csv",
        "Togo": "../data/togo_clean.csv"
    }
    return pd.read_csv(path_map[country])

def get_top_regions(df, metric):
    if "Region" in df.columns:
        top = df.groupby("Region")[metric].mean().sort_values(ascending=False).head(10)
        return top.reset_index()
    else:
        # fallback if no region column
        return pd.DataFrame({
            "Region": [f"Sample {i+1}" for i in range(5)],
            metric: [df[metric].mean()] * 5
        })
