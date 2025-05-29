import pandas as pd

def load_local_csv(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df["RestockDate"] = pd.to_datetime(df["RestockDate"], errors='coerce')
    return df
