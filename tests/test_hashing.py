# test_hashing.py
import os
from src.utils import compute_hash

def test_compute_hash(tmp_path):
    # create a temp file
    file = tmp_path / "test.txt"
    file.write_text("hello world")

    h1 = compute_hash(str(file))
    h2 = compute_hash(str(file))

    assert h1 == h2
    assert isinstance(h1, str)
    assert len(h1) == 64  # SHA256 hex length
