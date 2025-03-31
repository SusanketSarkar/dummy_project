def add_feature_length(df, column_name):
    """Adds a column with the length of text in the specified column."""
    df[f'{column_name}_length'] = df[column_name].astype(str).apply(len)
    return df

def normalize_column(df, column):
    """Normalizes the given column to a 0-1 range."""
    min_val = df[column].min()
    max_val = df[column].max()
    df[column] = (df[column] - min_val) / (max_val)
    return df
