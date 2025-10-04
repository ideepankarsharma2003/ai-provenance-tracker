# 🛣 Project Roadmap — AI Model Provenance Tracker

This roadmap outlines the milestones for building a provenance system for AI models, starting with **Python-only prototypes** and progressively moving into **blockchain/web3 integration**.  

---

## ✅ Phase 1: Core MVP (Python only)

**Goal:** Be able to upload a model, create a provenance fingerprint, evaluate it, and store metadata in a registry.

- [ ] **Uploader Script (`uploader.py`)**  
  - Accept model file, author, and description  
  - Save to `/models/` directory  
  - Copy to standardized filename based on hash  

- [ ] **SHA256 Fingerprinting (`utils.py`)**  
  - Generate unique fingerprint for each model file  
  - Prevent duplicates (skip re-registering same model)  

- [ ] **Automated Evaluation (`evaluator.py`)**  
  - Load simple benchmark dataset (Iris or MNIST subset)  
  - Test model accuracy / F1-score  
  - Store results alongside metadata  

- [ ] **Provenance Registry (`registry_manager.py`)**  
  - Store entries in `registry/registry.json`  
  - Each entry includes:  
    ```json
    {
      "hash": "abc123...",
      "author": "Alice",
      "description": "Iris classifier",
      "accuracy": 0.92,
      "timestamp": "2025-10-05"
    }
    ```  
  - Provide CLI to list all registered models  

---

## 🔄 Phase 2: Provenance & Logging

**Goal:** Add accountability and traceability to how models are used.  

- [ ] **Usage Logging (`logger.py`)**  
  - Log each inference into `usage_log.json`  
  - Append-only, includes: `timestamp`, `user`, `model_hash`, `action`  

- [ ] **Registry Queries**  
  - CLI/API to retrieve models by hash  
  - Search/filter by accuracy, author, description  

---

## 🌐 Phase 3: API Layer

**Goal:** Expose the system via a simple REST API.  

- [ ] **FastAPI Server (`api.py`)**  
  - `POST /upload` → Upload and register a model  
  - `GET /models` → List all registered models  
  - `POST /infer/{hash}` → Run inference with a model (logs usage)  

- [ ] **Swagger/OpenAPI Docs**  
  - Auto-generated API docs with FastAPI  
  - Allow contributors to test endpoints easily  

---

## 🚀 Phase 4: Extensions

**Goal:** Move beyond local storage to decentralized and community-driven trust.  

- [ ] **IPFS Storage**  
  - Upload models to IPFS/Filecoin  
  - Store returned content hash (CID) in registry  
  - Replace local file paths with IPFS links  

- [ ] **Reputation System**  
  - Allow users to rate/upvote models  
  - Track contributor reputation (simple token system)  
  - Penalize bad actors (low accuracy / flagged models)  

---

## 💡 Phase 5: Future

**Goal:** Integrate blockchain for transparent, tamper-proof provenance.  

- [ ] **Smart Contract Registry**  
  - Solidity contract to store model hashes + metadata  
  - Deployed to Ethereum/Polygon testnet  
  - Use `web3.py` to interact from Python scripts  

- [ ] **Tokenized Incentives**  
  - Contributors stake tokens on their models  
  - Good models → earn tokens, bad models → lose stake  
  - Aligns incentives around quality & trust  

- [ ] **Community Auditing**  
  - Allow other users to verify/evaluate models  
  - Store audit results on-chain for transparency  

---

📌 **Contributor Note:** Each phase is modular. You can contribute to **just one part** (e.g., usage logger, FastAPI API, or Solidity contract) without needing to understand the entire system.  

---
