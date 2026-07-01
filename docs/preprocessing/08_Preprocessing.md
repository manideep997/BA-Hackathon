
# Preprocessing

**Project:** Fill in the Frames Seamlessly – Enhancing Temporal Resolution of Satellite Imagery using AI/ML based Optical Flow

**Document Version:** 1.0

**Status:** Approved

**Owner:** Data Engineering Team

**Depends On:**

- 01_Project_Mission.md
- 02_Repository_Architecture.md
- 03_System_Architecture.md
- 04_Data_Flow.md
- 05_API_Architecture.md
- 06_Dataset_Acquisition.md
- 07_Dataset_Validation.md

**Next Document:**

09_Training_Dataset_Generation.md

---

# 1. Purpose

The preprocessing stage converts scientific satellite datasets into machine learning compatible tensors while preserving all essential metadata.

The preprocessing pipeline shall:

- Read scientific datasets
- Extract thermal infrared channels
- Preserve metadata
- Normalize values
- Handle missing pixels
- Prepare tensors
- Generate reusable datasets

This stage acts as the bridge between raw satellite products and AI model training.

---

# 2. Objectives

The preprocessing pipeline shall:

✔ Read NetCDF files

✔ Read HDF5 files

✔ Extract required thermal channel

✔ Remove invalid values

✔ Normalize images

✔ Preserve metadata

✔ Generate tensors

✔ Store processed datasets

✔ Generate preprocessing logs

✔ Validate outputs

---

# 3. Input Data

Supported inputs:

NetCDF (.nc)

HDF5 (.h5)

Supported datasets:

GOES-19

INSAT-3DS

INSAT-3DR

Himawari-8

---

# 4. Output Data

Processed outputs:

Tensor datasets

Metadata files

Dataset manifests

Cache files

Logs

Validation reports

---

# 5. Preprocessing Workflow

Raw Dataset

↓

Open Scientific File

↓

Read Metadata

↓

Extract Required Variables

↓

Extract Thermal Channel

↓

Handle Missing Values

↓

Normalize

↓

Resize (if required)

↓

Generate Tensor

↓

Save Processed Dataset

↓

Validation

---

# 6. Reading Scientific Files

Preferred libraries:

xarray

netCDF4

h5py

Responsibilities:

- Open dataset
- Read variables
- Read metadata
- Verify structure
- Close file safely

---

# 7. Metadata Preservation

Preserve:

Satellite Name

Sensor

Projection

Latitude

Longitude

Timestamp

Resolution

Channel

Units

Orbit Information (if available)

Metadata shall remain associated with every processed sample.

---

# 8. Channel Extraction

Extract:

GOES

ABI Channel 13

INSAT

TIR1

Himawari

Thermal Infrared Channel

Channel selection shall be configurable.

---

# 9. Missing Data Handling

Detect:

NaN

Fill Values

Invalid Pixels

Negative Values (where invalid)

Possible strategies:

- Replace with NaN mask
- Interpolate if scientifically justified
- Exclude affected samples
- Log affected regions

---

# 10. Data Normalization

Normalization strategies shall be configurable.

Possible methods:

Min-Max Scaling

Z-score Normalization

Physical Temperature Scaling

No normalization (research mode)

The selected strategy shall be documented.

---

# 11. Image Resizing

Resize only if required.

Preferred interpolation:

Bilinear

Bicubic

Lanczos

Preserve aspect ratio.

Document the chosen resolution.

---

# 12. Tensor Generation

Convert processed images into tensors.

Preferred framework:

PyTorch

Tensor shape example:

Batch × Channels × Height × Width

Maintain consistent tensor dimensions.

---

# 13. Data Augmentation

Default:

Disabled.

Optional techniques:

Horizontal Flip

Small Rotation

Brightness Perturbation

Gaussian Noise

Augmentation must not distort scientific meaning.

---

# 14. Batch Processing

The preprocessing pipeline shall support:

Single file

Directory

Recursive processing

Batch jobs

GPU-assisted preprocessing (optional)

---

# 15. Parallel Processing

Support:

Multi-threading

Multi-processing

Asynchronous I/O

Configuration shall determine the number of workers.

---

# 16. Caching

Cache reusable outputs.

Suggested structure:

cache/

preprocessed/

tensors/

metadata/

Avoid recomputing unchanged files.

---

# 17. Output Directory

processed/

GOES/

INSAT/

Himawari/

Each processed sample shall include:

Tensor

Metadata

Validation status

---

# 18. Validation After Preprocessing

Verify:

Tensor dimensions

Metadata completeness

No invalid values

Expected resolution

Expected channel

Correct normalization

---

# 19. Logging

Generate logs containing:

Timestamp

Filename

Processing Time

Dataset

Normalization Method

Output Path

Status

Warnings

Errors

---

# 20. Error Handling

Recoverable Errors

Corrupted sample

Missing optional metadata

Minor formatting issues

Action:

Skip sample

Continue processing

Critical Errors

Unreadable dataset

Missing required variables

Invalid channel

Action:

Stop current file

Record failure

Continue remaining datasets

---

# 21. Performance Optimization

The preprocessing module shall:

Reuse cache

Avoid duplicate processing

Stream large files

Release memory after processing

Support configurable batch sizes

---

# 22. AI Agent Responsibilities

The AI agent shall:

Read datasets

Extract channels

Normalize images

Generate tensors

Preserve metadata

Generate cache

Validate outputs

Create logs

Update manifests

---

# 23. Folder Structure

preprocessing/

readers/

normalization/

resizing/

tensor_generation/

metadata/

cache/

validators/

utils/

---

# 24. Expected Outputs

For every processed dataset:

Tensor File

Metadata File

Validation Report

Processing Log

Manifest Entry

---

# 25. Validation Checklist

Before dataset generation:

✔ Metadata preserved

✔ Channel extracted

✔ Tensor generated

✔ Dimensions verified

✔ Normalization verified

✔ Logs created

✔ Manifest updated

✔ Cache created

---

# 26. Acceptance Criteria

The preprocessing pipeline is complete when:

✓ All supported datasets can be processed.

✓ Metadata is preserved.

✓ Tensors generated successfully.

✓ Validation completed.

✓ Logs generated.

✓ Processed datasets stored correctly.

✓ Cache generated.

---

# 27. Future Enhancements

Possible improvements:

GPU preprocessing

Distributed preprocessing

Cloud storage integration

Automatic resolution detection

Compression

Streaming datasets

Incremental preprocessing

---

# Definition of Done

This document is complete when:

- Scientific datasets are transformed into AI-ready tensors.
- Metadata preservation is guaranteed.
- Validation is successful.
- Logging is implemented.
- Processed datasets are reproducible.

Only after preprocessing has completed successfully may the project proceed to training dataset generation.
