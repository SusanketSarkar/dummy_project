import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """Loads a CSV file from the given path."""
    return pd.read_csv(path)
