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

“I built an Image Processing Toolkit using Python, OpenCV, and NumPy to explore computer vision fundamentals. The project includes core operations like grayscale conversion, Gaussian blurring, Sobel/Canny edge detection, thresholding, histogram equalization, and color transformations.

I designed it as a modular pipeline so you can feed an image through multiple processing steps and visualize outputs at each stage. I also added utility functions for resizing, cropping, masking, and detecting contours. This project shows my ability to work with matrices, implement filters manually using convolution, optimize operations with NumPy, and understand how classical CV algorithms work under the hood. It also lays the foundation for higher-level tasks like segmentation or feature extraction.”
