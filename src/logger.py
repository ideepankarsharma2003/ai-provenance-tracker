# logger.py
"""
Append-only usage logger for model inference.
Stored in registry/usage_log.json
"""

import os
import json
from datetime import datetime

USAGE_LOG = os.path.join("registry", "usage_log.json")


def log_usage(user: str, model_hash: str, action: str = "inference"):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user": user,
        "model_hash": model_hash,
        "action": action,
    }

    if not os.path.exists(USAGE_LOG):
        logs = []
    else:
        with open(USAGE_LOG, "r", encoding="utf-8") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []

    logs.append(entry)

    with open(USAGE_LOG, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4)

    print(f"📒 Logged usage: {entry}")


if __name__ == "__main__":
    # Example usage
    log_usage("Alice", "abc123", "inference")
