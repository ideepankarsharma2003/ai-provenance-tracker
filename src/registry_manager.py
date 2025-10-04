# registry_manager.py
"""
Manages the provenance registry (registry/registry.json).
Allows listing, searching, and adding entries.
"""

import os
import json

REGISTRY_FILE = os.path.join("registry", "registry.json")


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


def list_models():
    registry = load_registry()
    if not registry:
        print("📂 No models registered yet.")
        return
    for i, entry in enumerate(registry, 1):
        print(f"{i}. Hash: {entry['hash']} | Author: {entry['author']} | "
              f"Accuracy: {entry.get('accuracy', 'N/A')} | Desc: {entry['description']}")


def get_model_by_hash(model_hash: str):
    registry = load_registry()
    for entry in registry:
        if entry["hash"] == model_hash:
            return entry
    return None


if __name__ == "__main__":
    list_models()
