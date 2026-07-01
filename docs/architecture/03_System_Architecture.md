
# System Architecture

**Project:** Fill in the Frames Seamlessly – Enhancing Temporal Resolution of Satellite Imagery using AI/ML based Optical Flow

**Document Version:** 1.0

**Status:** Approved

**Owner:** AI Software Engineering Team

**Depends On:**
- 01_Project_Mission.md
- 02_Repository_Architecture.md

**Next Document:**
04_Data_Flow.md

---

# 1. Purpose

This document defines the complete system architecture of the project.

It specifies how every subsystem interacts with every other subsystem.

Every implementation must follow this architecture.

This document acts as the blueprint for:

- Data Engineering
- Machine Learning
- Backend
- Frontend
- Dashboard
- Evaluation
- Deployment

---

# 2. High-Level System Overview

The platform consists of six major layers.

```text
                   USER
                     │
                     ▼
             Web Dashboard
                     │
                     ▼
              FastAPI Backend
                     │
                     ▼
          AI Inference Service
                     │
                     ▼
        Frame Interpolation Model
                     │
                     ▼
       Scientific Data Processing
                     │
                     ▼
     Satellite NetCDF / HDF5 Files
```

Each layer communicates only with adjacent layers.

---

# 3. Major Components

The complete system consists of:

### Dataset Layer

Responsibilities

- Download datasets
- Verify datasets
- Organize datasets
- Preserve metadata

Input

Official satellite products

Output

Validated datasets

---

### Preprocessing Layer

Responsibilities

- Read NetCDF
- Read HDF5
- Extract thermal channels
- Normalize data
- Build training images
- Preserve metadata

Output

Training dataset

---

### AI Layer

Responsibilities

- Optical Flow
- Frame Interpolation
- Model Training
- Model Evaluation
- Checkpoint Management

Candidate Models

- RIFE
- IFRNet
- Super SloMo
- EMA-VFI

Model selection must be based on measured validation performance.

---

### Inference Layer

Responsibilities

- Load trained model
- Generate intermediate frame
- Reconstruct NetCDF output
- Batch inference

---

### Evaluation Layer

Responsibilities

Compute:

- SSIM
- PSNR
- MSE
- FSIM

Generate:

- CSV
- Charts
- Reports

---

### Dashboard Layer

Responsibilities

- Upload files
- Timeline playback
- Original animation
- Interpolated animation
- Ground truth comparison
- Heatmaps
- Optical flow visualization
- Metric display
- Download outputs

---

# 4. End-to-End Workflow

```text
Official Dataset

        │

        ▼

Dataset Validation

        │

        ▼

Preprocessing

        │

        ▼

Training Dataset

        │

        ▼

Model Selection

        │

        ▼

Training

        │

        ▼

Evaluation

        │

        ▼

Checkpoint

        │

        ▼

Inference

        │

        ▼

Dashboard

        │

        ▼

Deployment
```

---

# 5. Training Architecture

```text
Satellite Images

↓

Triplet Generator

↓

Training Dataset

↓

DataLoader

↓

Frame Interpolation Model

↓

Loss Functions

↓

Optimizer

↓

Scheduler

↓

Checkpoint

↓

Validation

↓

Best Model
```

---

# 6. Inference Architecture

```text
Input NetCDF

↓

Read Metadata

↓

Extract Images

↓

Load Model

↓

Generate Intermediate Frame

↓

Restore Metadata

↓

Export NetCDF

↓

Dashboard
```

---

# 7. Backend Architecture

Responsibilities

- API
- Authentication (if enabled)
- File Upload
- Model Inference
- Evaluation
- Download Service

Communication

Frontend ⇄ Backend ⇄ Inference Engine

---

# 8. Frontend Architecture

Modules

- Landing Page
- Upload Page
- Dashboard
- Timeline
- Metrics
- Comparison Viewer
- Downloads
- Settings

The frontend communicates only with the backend API.

---

# 9. Dashboard Architecture

The dashboard consists of:

- Navigation
- Dataset Browser
- Upload Panel
- Timeline
- Playback Controls
- Comparison View
- Heatmap View
- Metrics Panel
- Download Panel

All visualizations should be synchronized.

---

# 10. Component Interaction

```text
Frontend

↓

Backend API

↓

Inference Engine

↓

Frame Interpolation Model

↓

Generated Frame

↓

Evaluation

↓

Frontend
```

---

# 11. Data Lifecycle

Dataset Download

↓

Validation

↓

Storage

↓

Preprocessing

↓

Training

↓

Checkpoint

↓

Inference

↓

Output

↓

Visualization

↓

Archive

---

# 12. Model Lifecycle

Model Selection

↓

Training

↓

Validation

↓

Checkpoint

↓

Evaluation

↓

Deployment

↓

Monitoring

---

# 13. Error Recovery Flow

If a phase fails:

Detect Failure

↓

Log Failure

↓

Identify Cause

↓

Retry (if recoverable)

↓

Validate Again

↓

Continue

Critical failures must halt the current phase until resolved.

---

# 14. Logging Architecture

Every subsystem shall produce structured logs.

Minimum fields:

- Timestamp
- Module
- Operation
- Status
- Duration
- Error Details (if any)

Logs should support debugging and reproducibility.

---

# 15. Validation Gates

Each phase concludes with a validation gate.

Validation includes:

- Functional verification
- Data integrity
- Test execution
- Documentation update

Only validated phases may proceed.

---

# 16. Security Considerations

The implementation should:

- Validate uploaded files.
- Preserve dataset integrity.
- Protect API endpoints as appropriate.
- Avoid exposing sensitive configuration.
- Use authenticated deployment targets when required.

---

# 17. Scalability

The architecture should support future additions including:

- Additional satellite missions
- New interpolation models
- New evaluation metrics
- Distributed training
- Cloud inference
- Batch processing

without requiring major architectural changes.

---

# 18. Acceptance Criteria

The architecture is accepted when:

- All major components are implemented.
- Component boundaries are respected.
- Data flows follow the documented paths.
- Validation gates are enforced.
- Logging is consistent.
- The end-to-end workflow operates successfully.
