import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """Loads a CSV file from the given path."""
    return pd.read_csv(path)

def drop_missing_rows(df):
    """Drops rows with any missing values."""
    return df.dropna()

