import pandas as pd
from src import features
from src.modeling import train_logistic


def test_add_feature_length():
    df = pd.DataFrame({'text': ['hello', 'world']})
    df = features.add_feature_length(df, 'text')
    assert 'text_length' in df.columns
    assert df['text_length'].tolist() == [5, 5]

def test_train_logistic_runs():
    train_logistic([], [])  # ⚠️ No assertion, dummy data

