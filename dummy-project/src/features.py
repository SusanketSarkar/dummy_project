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

def extract_keywords(df, column):
    """Extract keywords from text."""
    keywords = []
    for text in df[column]:  # ⚠️ slow for large data
        tokens = text.split()
        keywords.append([t for t in tokens if len(t) > 5])
    df['keywords'] = keywords
    return df

def one_hot_encode(df, column):
    """One hot encode the specified column."""
    dummies = pd.get_dummies(df[column])
    df = pd.concat([df, dummies], axis=1)
    return df
