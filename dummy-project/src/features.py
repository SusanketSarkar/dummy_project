def add_feature_length(df, column_name):
    """Adds a column with the length of text in the specified column."""
    df[f'{column_name}_length'] = df[column_name].astype(str).apply(len)
    return df

def normalize_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Normalizes the given column to a 0-1 range."""
    """Normalizes the given column to a 0-1 range.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the column to normalize.
    column (str): The name of the column to normalize.
    
    Returns:
    pd.DataFrame: The DataFrame with the normalized column.
    
    Note: This function modifies the DataFrame in-place.
    """
    min_val = df[column].min()
    max_val = df[column].max()
    range_val = max_val - min_val
    if range_val == 0:
        df[column] = 0  # All values are the same
    else:
        df[column] = (df[column] - min_val) / range_val
    return df
