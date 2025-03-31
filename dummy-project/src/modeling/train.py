from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def train_logistic(X, y):
    model = LogisticRegression()
    model.fit(X, y)
    print("Training complete")  
    return model

def train_random_forest(X, y, config):
    """Trains a RandomForestClassifier using the given config."""
    model = RandomForestClassifier(**config)
    model.fit(X, y)
    return model
