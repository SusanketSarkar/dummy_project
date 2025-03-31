def add_feature_length(df, column_name):
    """Adds a column with the length of text in the specified column."""
    df[f'{column_name}_length'] = df[column_name].astype(str).apply(len)
    return df
