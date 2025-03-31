from sklearn.ensemble import RandomForestClassifier

def train_random_forest(X, y, config):
    """Trains a RandomForestClassifier using the given config."""
    model = RandomForestClassifier(**config)
    model.fit(X, y)
    return model
