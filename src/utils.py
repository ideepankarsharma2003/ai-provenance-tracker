# utils.py
"""
Utility functions (hashing, file helpers).
"""

import hashlib


def compute_hash(file_path: str) -> str:
    """Compute SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


if __name__ == "__main__":
    # Demo run
    import os
    test_file = os.path.join("models", "dummy_model.pkl")
    if os.path.exists(test_file):
        print("Hash:", compute_hash(test_file))
    else:
        print("⚠️ No file found at", test_file)
