# Base System Packages (187 total)

Pre-installed in container image. Survives session reset. Always available.

## Core Scientific
- numpy==2.2.5
- scipy==1.16.2
- pandas==2.3.2
- matplotlib==3.10.3
- seaborn==0.13.2
- plotly==6.3.0
- scikit-learn==1.7.2
- scikit-image==0.25.2
- statsmodels==0.14.5
- lightgbm==4.6.0

## Deep Learning (CPU-only)
- torch==2.8.0+cu128
- torchvision==0.23.0
- triton==3.4.0
- nvidia-cublas-cu12 through nvidia-nvtx-cu12 (runtime libs, no GPU)

## Computer Vision
- opencv-python-headless==4.12.0.88
- pillow==11.2.1
- imageio==2.37.0
- tifffile==2025.9.9
- easyocr==1.7.2
- pytesseract==0.3.13
- pyclipper==1.3.0.post6

## Web/API
- fastapi==0.116.1
- uvicorn==0.34.2
- starlette==0.46.2
- httpx==0.28.1
- requests==2.32.3
- urllib3==2.4.0
- websockets==15.0.1
- pydantic==2.11.4

## Document Processing
- python-docx==1.2.0
- python-pptx==1.0.2
- openpyxl==3.1.5
- xlrd==2.0.2
- xlsxwriter==3.2.9
- fpdf==1.7.2
- reportlab==4.4.3
- pypdf2==3.0.1
- pdfminer-six==20250506
- tabula==1.0.5
- striprtf==0.0.29
- pylatex==1.4.2
- lxml==6.0.1

## Geospatial
- geopandas==1.1.1
- shapely==2.1.1
- pyproj==3.7.2
- pyogrio==0.11.1

## Crypto/Security
- cryptography==44.0.2
- bcrypt==4.3.0
- paramiko==3.5.1
- PyNaCl==1.5.0
- pycryptodome==3.23.0

## Math/Symbolic
- sympy==1.14.0
- mpmath==1.3.0
- networkx==3.5

## Jupyter/IPython
- ipython==9.4.0
- ipykernel==6.29.5
- jupyter-client==8.6.3
- jupyter-core==5.8.1
- prompt-toolkit==3.0.51
- pyzmq==27.0.0

## Utilities
- psutil==7.0.0
- loguru==0.7.3
- click==8.2.1
- typer==0.15.3
- rich==14.0.0
- markdown-it-py==3.0.0
- tabulate==0.9.0
- PyYAML==6.0.2
- packaging==25.0
- platformdirs==4.3.8
- python-dotenv==1.1.0
- sentry-sdk==2.33.0

## Simulation
- simpy==4.1.1
- chess==1.11.2

## Build Tools
- setuptools==80.9.0
- wheel==0.45.1
- pip==25.0.1
- ninja==1.13.0
