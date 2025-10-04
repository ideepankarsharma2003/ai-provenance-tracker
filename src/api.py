# api.py
"""
FastAPI server to interact with the provenance system.
Endpoints:
- POST /upload
- GET /models
- POST /infer/{hash}
"""

import os
import joblib
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import RedirectResponse
from src.uploader import upload_model
from src.registry_manager import get_model_by_hash
from src.logger import log_usage
from fastapi import Body

app = FastAPI(title="AI Model Provenance Tracker")


# Redirect root to Swagger UI
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


@app.post("/upload")
async def upload(file: UploadFile, author: str = Form(...), desc: str = Form(...)):
    file_path = os.path.join("models", file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    upload_model(file_path, author=author, description=desc)
    return {"status": "success", "filename": file.filename}


@app.get("/models")
async def get_models():
    from src.registry_manager import load_registry
    return load_registry()


from fastapi import Body

@app.post("/infer/{model_hash}")
async def infer(
    model_hash: str,
    features: list[float] = Body(
        ...,
        example=[5.1, 3.5, 1.4, 0.2]
    ),
    user: str = "anonymous"
):
    entry = get_model_by_hash(model_hash)
    if not entry:
        return {"error": "Model not found"}

    model_path = os.path.join("models", entry["filename"])
    model = joblib.load(model_path)

    expected = getattr(model, "n_features_in_", None)
    if expected and len(features) != expected:
        return {
            "error": f"Expected {expected} features, got {len(features)}. Features: {features}"
        }

    prediction = model.predict([features]).tolist()
    log_usage(user, model_hash, "inference")

    return {"prediction": prediction, "expected_features": expected, "model": entry}
