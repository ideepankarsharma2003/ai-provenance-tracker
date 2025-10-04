# test_registry.py
import os
import json
from src.uploader import upload_model, load_registry

def test_upload_and_registry(tmp_path):
    # create fake registry dir
    reg_dir = tmp_path / "registry"
    reg_dir.mkdir()
    reg_file = reg_dir / "registry.json"
    reg_file.write_text("[]")

    # create fake model
    model_file = tmp_path / "dummy.pkl"
    model_file.write_bytes(b"model-weights")

    # monkeypatch global path
    import src.uploader as uploader
    uploader.REGISTRY_FILE = str(reg_file)

    upload_model(str(model_file), "TestUser", "Test model")

    registry = load_registry()
    assert len(registry) == 1
    assert registry[0]["author"] == "TestUser"
