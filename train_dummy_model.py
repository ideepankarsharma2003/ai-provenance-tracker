"""
train_dummy_model.py
--------------------
Train and save a simple Decision Tree classifier on the Iris dataset.

This script is mainly for demonstration purposes:
- It shows how to generate a dummy ML model.
- Saves the model into the ./models directory.
- Can be used to test the provenance pipeline (uploader, evaluator, etc.).

Run:
    python train_dummy_model.py
"""

import os
import joblib
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_and_save():
    print("📥 Loading dataset: Iris (150 samples, 4 features)...")
    iris = load_iris()
    X, y = iris.data, iris.target

    print("📊 Splitting data into train/test (80/20)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("🌳 Training DecisionTreeClassifier...")
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    print("🔍 Evaluating model on test set...")
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Model accuracy on test set: {acc:.2f}")

    print("💾 Saving model to ./models/iris_clf.pkl ...")
    os.makedirs("models", exist_ok=True)
    model_path = os.path.join("models", "iris_clf.pkl")
    joblib.dump(clf, model_path)

    print(f"🎉 Dummy model successfully saved at: {model_path}")
    return model_path


if __name__ == "__main__":
    print("=======================================")
    print("  AI Model Provenance Tracker - Trainer ")
    print("=======================================")
    train_and_save()
    print("Done! You can now upload and register this model.")
