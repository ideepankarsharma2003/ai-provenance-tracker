# evaluator.py
"""
Evaluator for uploaded ML models.
Loads a benchmark dataset (Iris for now) and computes accuracy/F1 score.

Usage:
    python src/evaluator.py --file models/iris_clf.pkl
    python src/evaluator.py   # falls back to dummy model
"""

import os
import joblib
import argparse
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def evaluate_model(model_path: str) -> dict:
    """Evaluate a model on the Iris dataset."""
    print(f"📥 Loading model from: {model_path}")
    model = joblib.load(model_path)

    print("📊 Loading Iris dataset...")
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    print("🔮 Running predictions...")
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Accuracy on Iris test set: {acc:.2f}")

    return {"dataset": "iris", "accuracy": acc}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a model on the Iris dataset.")
    parser.add_argument("--file", type=str, help="Path to model file (.pkl)")
    args = parser.parse_args()

    if args.file:
        model_path = args.file
    else:
        # fallback
        model_path = os.path.join("models", "dummy_model.pkl")
        print(f"⚠️ No --file provided. Using default: {model_path}")

    try:
        results = evaluate_model(model_path)
        print("📊 Final Evaluation Results:", results)
    except Exception as e:
        print(f"⚠️ Could not evaluate: {e}")
