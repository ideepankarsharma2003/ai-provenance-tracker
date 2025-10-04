# uploader.py
import os
import json
import hashlib
from datetime import datetime, timezone

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

    print(f"✅ Model uploaded: {entry['filename']}")
    print(f"   SHA256: {model_hash}")


if __name__ == "__main__":
    # Example usage
    # python src/uploader.py
    test_file = os.path.join("models", "dummy_model.pkl")
    os.makedirs("models", exist_ok=True)
    with open(test_file, "wb") as f:
        f.write(b"example-model-weights")

    upload_model(test_file, author="Alice", description="Demo model")
