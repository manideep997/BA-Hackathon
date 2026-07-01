# Fill in the Frames Seamlessly – Enhancing Temporal Resolution of Satellite Imagery using AI/ML based Optical Flow

## Project Overview

This project aims to enhance the temporal resolution of geostationary satellite imagery by generating realistic intermediate satellite frames using Artificial Intelligence, Deep Learning, and Optical Flow techniques.

The system is designed to interpolate missing satellite observations between two consecutive temporal frames while preserving cloud structures, weather patterns, and thermal characteristics.

The project is inspired by the Smart India Hackathon (SIH) problem statement and is intended to provide a complete end-to-end platform for satellite frame interpolation, scientific evaluation, visualization, and deployment.

---

# Objectives

The system shall:

* Acquire satellite datasets from official sources.
* Read NetCDF (`.nc`) and HDF5 (`.h5`) files.
* Preserve all scientific metadata.
* Generate training triplets for temporal interpolation.
* Train or fine-tune state-of-the-art frame interpolation models.
* Produce realistic intermediate satellite frames.
* Evaluate generated frames using objective image-quality metrics.
* Visualize original and interpolated sequences.
* Export results as NetCDF.
* Deploy a modern web application for interactive visualization.

---

# Supported Datasets

## GOES-19

Purpose

Primary dataset for model training and validation due to its high temporal resolution.

Official Source

https://registry.opendata.aws/noaa-goes/

Recommended Product

* ABI L1b
* ABI L2 CMIP
* Channel 13 (10.3 μm)

---

## INSAT-3DS / INSAT-3DR

Purpose

Final inference target.

Official Source

https://www.mosdac.gov.in/

Recommended Product

TIR1 Channel

---

## Himawari-8

Purpose

Additional evaluation and experimentation.

Official Source

https://www.data.jma.go.jp/mscweb/en/

---

# Major Features

* Automated dataset acquisition.
* Scientific NetCDF preprocessing.
* Metadata preservation.
* Training dataset generation.
* Optical Flow estimation.
* AI-powered frame interpolation.
* Model comparison.
* Automatic evaluation.
* Interactive dashboard.
* Heatmap visualization.
* Side-by-side comparison.
* NetCDF export.
* Downloadable reports.
* Production deployment.

---

# Technology Stack

## Machine Learning

* Python
* PyTorch
* OpenCV
* NumPy
* SciPy
* xarray
* netCDF4
* h5py

---

## Deep Learning

Candidate models include:

* RIFE
* IFRNet
* Super SloMo
* EMA-VFI

The implementation should compare models using measured validation results and select the best-performing approach for the target datasets.

---

## Backend

* FastAPI

---

## Frontend

* Next.js
* React
* TypeScript

---

## Visualization

* Plotly
* OpenLayers or Leaflet (2D maps)
* CesiumJS (3D globe, optional)

---

## Deployment

Frontend

* Vercel

Backend

* Railway, Render, or another suitable Python hosting platform

---

# Repository Structure

```text
Fill-In-The-Frames/

├── datasets/
├── preprocessing/
├── models/
├── training/
├── inference/
├── evaluation/
├── backend/
├── frontend/
├── dashboard/
├── configs/
├── tests/
├── scripts/
├── docs/
├── outputs/
├── checkpoints/
├── logs/
├── notebooks/
├── docker/
├── .github/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# Development Workflow

1. Dataset Acquisition
2. Dataset Validation
3. Preprocessing
4. Training Dataset Generation
5. Model Evaluation
6. Model Training or Fine-Tuning
7. Inference
8. Evaluation
9. Dashboard
10. Testing
11. Deployment
12. Final Verification

Each stage must pass its validation criteria before proceeding to the next.

---

# Dashboard

The deployed application will provide:

* Upload `.nc` and `.h5` files.
* Demo mode with sample datasets.
* Original satellite animation.
* Generated intermediate frames.
* Ground truth comparison (when available).
* Optical flow visualization.
* Difference heatmaps.
* Evaluation metrics.
* Timeline controls.
* Animation playback.
* Download generated outputs.

---

# Evaluation Metrics

The project evaluates generated frames using:

* SSIM
* PSNR
* MSE
* FSIM

Additional metrics may be incorporated if they better capture cloud motion and interpolation quality.

---

# Documentation

The project includes a comprehensive specification under the `docs/` directory, covering:

* Project Mission
* Repository Architecture
* Dataset Acquisition
* Preprocessing
* Dataset Generation
* Model Selection
* Training
* Evaluation
* Inference
* Dashboard
* Testing
* Backend
* Frontend
* Deployment
* Final Verification

---

# Contributing

All contributions should:

* Preserve reproducibility.
* Follow project coding standards.
* Include tests where appropriate.
* Update documentation when behavior changes.
* Avoid modifying raw datasets.
* Maintain modular architecture.

---

# License

Select an appropriate open-source license before public release (for example, MIT or Apache-2.0), ensuring compatibility with all third-party dependencies and datasets.

---

# Acknowledgements

This project uses publicly available satellite datasets and builds upon advances in optical flow and deep learning–based frame interpolation developed by the broader research community. Please cite and comply with the licenses of all datasets, models, and software incorporated into the project.
