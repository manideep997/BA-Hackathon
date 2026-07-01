
# Data Flow Architecture

**Project:** Fill in the Frames Seamlessly – Enhancing Temporal Resolution of Satellite Imagery using AI/ML based Optical Flow

**Document Version:** 1.0

**Status:** Approved

**Owner:** AI Software Engineering Team

**Depends On:**
- 01_Project_Mission.md
- 02_Repository_Architecture.md
- 03_System_Architecture.md

**Next Document:**
05_API_Architecture.md

---

# 1. Purpose

This document defines the complete data lifecycle of the project.

Every dataset, image, metadata object, checkpoint, prediction, evaluation result, and dashboard visualization must follow this architecture.

The objective is to ensure:

- Data consistency
- Metadata preservation
- Reproducibility
- Traceability
- Validation at every stage

---

# 2. High-Level Data Pipeline

```text
Official Satellite Data
        │
        ▼
Dataset Downloader
        │
        ▼
Dataset Validation
        │
        ▼
Raw Dataset Storage
        │
        ▼
Scientific Data Reader
        │
        ▼
Metadata Extraction
        │
        ▼
Image Extraction
        │
        ▼
Normalization
        │
        ▼
Training Triplet Generator
        │
        ▼
Training Dataset
        │
        ▼
Frame Interpolation Model
        │
        ▼
Generated Intermediate Frame
        │
        ▼
Evaluation
        │
        ▼
NetCDF Reconstruction
        │
        ▼
Dashboard
```

---

# 3. Data Sources

The system supports:

### GOES-19

Purpose

Primary training dataset

Format

NetCDF

---

### INSAT-3DS / INSAT-3DR

Purpose

Primary inference dataset

Format

NetCDF / HDF5

---

### Himawari-8

Purpose

Validation and experimentation

Format

NetCDF

---

# 4. Raw Dataset Storage

All downloaded datasets shall be stored without modification.

```text
datasets/

GOES/

INSAT/

Himawari/
```

Rules

- Never overwrite raw files.
- Preserve timestamps.
- Preserve filenames.
- Preserve metadata.

---

# 5. Dataset Validation Flow

Downloaded File

↓

Checksum Verification (if available)

↓

Open File

↓

Validate Format

↓

Validate Metadata

↓

Validate Required Channels

↓

Validation Passed

↓

Store

If validation fails:

- Log error
- Record filename
- Skip corrupted file
- Continue processing remaining files

---

# 6. Metadata Flow

Each dataset contains valuable metadata.

Preserve:

- Timestamp
- Latitude
- Longitude
- Projection
- Satellite name
- Channel
- Resolution
- Units

Metadata must remain associated with the image throughout preprocessing, training, inference, and output generation.

---

# 7. Image Extraction Flow

Scientific File

↓

Extract Thermal Channel

↓

Convert to Array

↓

Normalize

↓

Resize (if required)

↓

Generate Image Tensor

↓

Store Temporary Cache

The original scientific file remains unchanged.

---

# 8. Preprocessing Flow

Input

NetCDF

↓

Read Variables

↓

Read Metadata

↓

Extract Target Channel

↓

Handle Missing Values

↓

Normalize

↓

Resize

↓

Generate Tensor

↓

Store Processed Sample

---

# 9. Training Dataset Generation

Consecutive Frames

Frame A

Frame B

Frame C

↓

Training Sample

Input:

Frame A

Frame C

Ground Truth:

Frame B

Repeat across the entire dataset.

---

# 10. Training Flow

Training Samples

↓

DataLoader

↓

Batch Generator

↓

GPU

↓

Model

↓

Prediction

↓

Loss Computation

↓

Backpropagation

↓

Checkpoint

↓

Validation

---

# 11. Checkpoint Flow

Training

↓

Checkpoint Manager

↓

Best Model

↓

Latest Model

↓

Epoch Models

↓

Resume Training

---

# 12. Inference Flow

Input NetCDF

↓

Read Metadata

↓

Extract Image

↓

Load Model

↓

Generate Intermediate Frame

↓

Convert Back to Scientific Format

↓

Restore Metadata

↓

Export NetCDF

---

# 13. Evaluation Flow

Prediction

↓

Ground Truth

↓

Metric Computation

↓

SSIM

↓

PSNR

↓

MSE

↓

FSIM

↓

Generate Report

↓

Dashboard

---

# 14. Dashboard Flow

User Upload

↓

Backend API

↓

Inference Engine

↓

Generated Output

↓

Evaluation

↓

Visualization

↓

Download

---

# 15. Output Flow

Generated Frame

↓

NetCDF Writer

↓

Metadata Restoration

↓

Output File

↓

Dashboard

↓

Download

---

# 16. Data Validation Points

Validation shall occur at:

- Dataset Download
- Dataset Reading
- Metadata Extraction
- Image Extraction
- Preprocessing
- Training Dataset Generation
- Training
- Inference
- NetCDF Export
- Dashboard Upload

---

# 17. Error Handling

Recoverable errors:

- Retry operation
- Log issue
- Continue processing

Critical errors:

- Stop current phase
- Save diagnostics
- Notify through logs

---

# 18. Storage Layout

```text
datasets/
processed/
outputs/
checkpoints/
logs/
reports/
cache/
```

---

# 19. Data Integrity Rules

The system shall:

- Never modify raw datasets.
- Preserve metadata.
- Preserve timestamps.
- Avoid duplicate outputs.
- Maintain deterministic file naming where practical.

---

# 20. Logging

Log every transformation.

Example

Input File

↓

Operation

↓

Output File

↓

Duration

↓

Status

↓

Error (if any)

---

# 21. Acceptance Criteria

This document is satisfied when:

- Every data transformation is documented.
- Metadata preservation is enforced.
- Validation exists at every stage.
- Error recovery is defined.
- Storage locations are specified.
- End-to-end data movement is reproducible.
