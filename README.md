# Image Processing API (FastAPI + Pillow)

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Tests](https://img.shields.io/badge/tests-pytest-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)


Upload an image and get a thumbnail in response.

## Run
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
