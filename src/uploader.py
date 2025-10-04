# uploader.py
"""
Uploader script for AI Model Provenance Tracker.
- Takes a model file path as argument.
- If no argument is given, uses a default dummy model (dummy_model.pkl).
- Computes SHA256 hash, registers metadata, and saves entry into registry.json.

Usage:
    python src/uploader.py --file models/iris_clf.pkl --author Alice --desc "Iris classifier"
    python src/uploader.py   # falls back to dummy_model.pkl
"""

import os
import json
import hashlib
from datetime import datetime, timezone
import argparse

REGISTRY_FILE = os.path.join("registry", "registry.json")


def compute_hash(file_path: str) -> str:
    """Compute SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def load_registry():
    if not os.path.exists(REGISTRY_FILE):
        return []
    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_registry(registry):
    os.makedirs("registry", exist_ok=True)
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=4)


def upload_model(file_path: str, author: str, description: str):
    """Register a model file with provenance metadata."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Model file not found: {file_path}")

    # Compute fingerprint
    model_hash = compute_hash(file_path)

    # Create entry
    entry = {
        "hash": model_hash,
        "author": author,
        "description": description,
        "filename": os.path.basename(file_path),
        "timestamp": datetime.now(tz=timezone.utc).isoformat()
    }

    # Append to registry
    registry = load_registry()
    registry.append(entry)
    save_registry(registry)

    print("===================================")
    print(f"✅ Model uploaded: {entry['filename']}")
    print(f"   SHA256: {model_hash}")
    print(f"   Author: {author}")
    print(f"   Description: {description}")
    print("===================================")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a model to the provenance registry.")
    parser.add_argument("--file", type=str, help="Path to the model file")
    parser.add_argument("--author", type=str, default="Anonymous", help="Author of the model")
    parser.add_argument("--desc", type=str, default="No description provided", help="Model description")

    args = parser.parse_args()

    if args.file:
        model_file = args.file
    else:
        # fallback to dummy model
        os.makedirs("models", exist_ok=True)
        model_file = os.path.join("models", "dummy_model.pkl")
        with open(model_file, "wb") as f:
            f.write(b"example-model-weights")
        print("⚠️ No --file provided, using dummy model at models/dummy_model.pkl")

    upload_model(model_file, author=args.author, description=args.desc)
