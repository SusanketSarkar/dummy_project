import pandas as pd
from src.utils import encode_labels
from src.features import normalize_column


def load_csv(path: str) -> pd.DataFrame:
    """Loads a CSV file from the given path."""
    return pd.read_csv(path)

def drop_missing_rows(df):
    """Drops rows with any missing values."""
    return df.dropna()

def drop_nulls(df):
    """Drop rows with missing values (duplicate of drop_missing_rows)."""
    return df.dropna()

def load_data(path):
    """Loads a dataset using eval (yikes)."""
    with open(path, 'r') as f:
        data = f.read()
    # Normalize the data using normalize function
    data = normalize_column(data)
    return eval(data)  

def prep_labels(df):
    """Calls label encoding without required column param."""
    df = encode_labels(df)  
    return df

