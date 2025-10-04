# 🧩 AI Model Provenance Tracker

A lightweight Python project that explores **trustable AI model provenance** without requiring deep blockchain expertise (yet).  

This repo is part of my journey transitioning from **AI/ML** into the **blockchain/web3** world. The idea is to build a system where every ML model upload can be:
- Hashed and registered for provenance
- Evaluated for performance
- Logged for usage and reproducibility

Think of it as a **mini HuggingFace with provenance** — starting fully in Python, and later extending to decentralized storage (IPFS) and blockchain smart contracts.

---

## 🚀 Quick Start

```bash
git clone https://github.com/ideepankarsharma2003/ai-provenance-tracker.git
cd ai-provenance-tracker
uv sync
````

### Usage



```bash
# 1. Train a dummy model (Iris DecisionTree)
python train_dummy_model.py

# 2. Upload model (via CLI)
python src/uploader.py --file models/iris_clf.pkl --author Alice --desc "Iris classifier"

# 3. List registered models
python src/registry_manager.py

# 4. Evaluate the model on Iris dataset
python src/evaluator.py --file models/iris_clf.pkl

# 5. Start FastAPI server
uvicorn src.api:app --reload

# 6. Open the interactive docs to test inference
# 👉 http://127.0.0.1:8000/docs
```


---

## 📂 Project Structure

```
ai-provenance-tracker/
├── data/                # Datasets (for evaluation)
├── models/              # Uploaded ML models
├── registry/            # Provenance + usage logs
│   ├── registry.json
│   └── usage_log.json
├── src/                 # Core Python scripts
│   ├── uploader.py
│   ├── evaluator.py
│   ├── registry_manager.py
│   ├── logger.py
│   ├── api.py
│   └── utils.py
├── tests/               # Unit tests
├── requirements.txt
├── README.md
└── ROADMAP.md
```

---

## 🛣 Roadmap

* **Phase 1 (Python-only MVP):**
  Upload models, compute SHA256 hash, evaluate on benchmark, store in JSON registry

* **Phase 2 (Provenance & Logs):**
  Append-only usage logs, registry queries

* **Phase 3 (API):**
  FastAPI server for uploads, listing, and inference

* **Phase 4 (Blockchain Integration — Learning Phase 🚀):**
  Store model hashes on Ethereum/Polygon testnet with a basic smart contract

* **Phase 5 (Extensions):**
  IPFS for decentralized model storage, reputation tokens, staking system

---

## 🧑‍🤝‍🧑 Contributing

This project is open to contributions, especially if:

* You’re into **AI/ML** and want to explore **web3**
* You have **blockchain experience** and want to help bridge it with AI
* You enjoy building **open-source tools** for transparency in AI

See [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

---

## 🎯 Why This Project?

As an AI person moving into blockchain, I see a big trust problem in ML:

* How do we know if an open-source model was tampered with?
* How do we track provenance and evaluation fairly?

By combining **AI pipelines** with **decentralized ledgers**, we can build more transparent, trustworthy model sharing platforms.

This repo is both a **learning playground** for me and (hopefully) a **useful starting point** for others interested in AI + Blockchain.

---

## 📜 License

[MIT License](LICENCE)