# Repository: python-ml-model
# New Feature: Train model on a custom dataset

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_on_custom_data(dataset_path):
    """Train a Random Forest model on a custom dataset."""
    data = pd.read_csv(dataset_path)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model accuracy: {accuracy * 100:.2f}%")

# Example usage
train_on_custom_data("custom_dataset.csv")
