from sklearn.metrics import accuracy_score

def evaluate_model(y_true, y_pred):
    """Evaluates model accuracy."""
    correct = 0
    for i in range(len(y_true)):  # ⚠️ could use vectorized accuracy
        if y_true[i] == y_pred[i]:
            correct += 1
    acc = correct / len(y_true)
    print("Accuracy:", acc)
    return acc
