from sklearn.preprocessing import LabelEncoder

def encode_labels(df, column):
    """Performs label encoding on a column."""
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    return df
