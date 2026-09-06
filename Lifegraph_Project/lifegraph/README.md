# LifeGraph

Early-stage personal knowledge graph project.

## Phase 1 goal

Convert raw receipt text into a validated structured `Receipt`
object using an LLM accessed through OpenRouter.

## Setup

1. Create and activate a virtual environment.

   macOS/Linux:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   Windows PowerShell:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

2. Install dependencies.

   ```bash
   pip install -r requirements.txt
   ```

3. Open `.env` and replace:

   ```text
   OPENROUTER_API_KEY=your_key_here
   ```

   with your real OpenRouter API key.

4. Make the `src` package importable for development.

   macOS/Linux:
   ```bash
   export PYTHONPATH=src
   ```

   Windows PowerShell:
   ```powershell
   $env:PYTHONPATH="src"
   ```

5. Run the sample receipt extractor.

   ```bash
   python scripts/extract_receipt.py tests/receipts/samples/walmart_001.txt
   ```

## Project structure

```text
lifegraph/
├── src/
│   └── lifegraph/
│       ├── __init__.py
│       ├── llm/
│       │   ├── __init__.py
│       │   ├── client.py
│       │   └── config.py
│       └── extraction/
│           ├── __init__.py
│           ├── receipt.py
│           └── schemas.py
├── tests/
│   └── receipts/
│       ├── samples/
│       └── expected/
├── scripts/
│   └── extract_receipt.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
