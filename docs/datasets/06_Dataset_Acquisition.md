# Dataset Acquisition

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

**Next Document:**

07_Dataset_Validation.md

---

# 1. Purpose

The purpose of this document is to define the complete data acquisition pipeline for the project.

The AI agent shall automatically obtain, organize, verify, and catalogue all required datasets before any preprocessing, training, or inference begins.

This document ensures:

- Reproducibility
- Dataset integrity
- Metadata preservation
- Automated downloading
- Proper storage hierarchy
- Consistent file naming
- Fault-tolerant downloads

---

# 2. Supported Datasets

The project shall support the following official satellite datasets.

## GOES-19 ABI

Purpose

Primary dataset for model development and validation due to its high temporal resolution.

Official Source

https://registry.opendata.aws/noaa-goes/

Products

- ABI L1b Radiances
- ABI L2 Cloud & Moisture Imagery (CMIP)

Recommended Channel

Channel 13

Wavelength

10.3 µm

Temporal Resolution

Approximately 10 minutes

Preferred Usage

Training

Validation

Hyperparameter tuning

---

## INSAT-3DS / INSAT-3DR

Purpose

Primary inference dataset required by the SIH problem statement.

Official Source

https://www.mosdac.gov.in

Dataset

TIR1

Preferred Format

NetCDF

HDF5

Temporal Resolution

Approximately 30 minutes

---

## Himawari-8

Purpose

Cross-validation and experimentation.

Official Source

https://www.data.jma.go.jp/mscweb/en/

Recommended Product

AHI Infrared Channel

Temporal Resolution

10 minutes

---

# 3. Dataset Selection Strategy

The AI agent shall prioritize datasets as follows.

Training

GOES-19

↓

Validation

GOES-19 + Himawari-8

↓

Inference

INSAT-3DS

This strategy provides dense temporal observations for learning while preserving the evaluation target.

---

# 4. Directory Structure

Raw datasets shall be organized as follows.

datasets/

    GOES/

        raw/

        processed/

        metadata/

    INSAT/

        raw/

        processed/

        metadata/

    Himawari/

        raw/

        processed/

        metadata/

Never overwrite files in the raw directory.

---

# 5. Download Requirements

The AI agent shall:

✔ Download only from official sources.

✔ Preserve original filenames.

✔ Preserve timestamps.

✔ Resume interrupted downloads where supported.

✔ Log every download.

✔ Skip duplicate files.

✔ Validate downloaded files before indexing.

---

# 6. Supported Formats

The acquisition module shall support:

NetCDF (.nc)

HDF5 (.h5)

Compressed archives where officially provided (after extraction).

Unsupported formats shall be rejected with meaningful error messages.

---

# 7. Download Workflow

Official Dataset

↓

Connect

↓

Verify Availability

↓

Download

↓

Integrity Check

↓

Metadata Extraction

↓

Dataset Index

↓

Raw Storage

↓

Validation

---

# 8. Download Automation

The project shall include scripts for automated downloading.

Suggested scripts:

scripts/

download_goes.py

download_insat.py

download_himawari.py

download_all.py

Each script shall support:

- Date range
- Product selection
- Channel selection
- Resume downloads
- Logging
- Retry on network failures

---

# 9. Metadata Extraction

For every file, extract and store:

Satellite Name

Sensor

Acquisition Time

Channel

Spatial Resolution

Projection

Latitude

Longitude

Image Dimensions

Data Type

Units

Store metadata separately without modifying the original dataset.

---

# 10. Dataset Manifest

Generate a manifest (CSV or JSON) containing:

- File name
- Dataset
- Timestamp
- Channel
- File size
- Checksum (if available)
- Validation status
- Processing status

This manifest will be used throughout the pipeline.

---

# 11. File Naming Policy

Do not rename original files.

Generated files shall use deterministic naming.

Example:

GOES_2026-07-01_0010_processed.nc

INSAT_2026-07-01_0030_interpolated.nc

---

# 12. Retry Strategy

Network failures shall trigger:

Retry 1

↓

Retry 2

↓

Retry 3

↓

Log Failure

↓

Continue Remaining Downloads

Do not terminate the entire pipeline due to one failed download.

---

# 13. Storage Policy

Raw datasets remain immutable.

Processed datasets are stored separately.

Generated outputs are stored in the outputs directory.

Never mix raw and generated files.

---

# 14. Logging Requirements

Each download log shall contain:

Timestamp

Dataset Name

File Name

Source URL

Download Duration

Status

File Size

Retry Count

Checksum Result (if available)

---

# 15. Error Handling

Recoverable Errors

- Temporary network failures
- Interrupted downloads
- Timeout

Action

Retry automatically.

Critical Errors

- Authentication failure
- Corrupted downloads
- Unsupported format

Action

Log the issue.

Skip affected file.

Continue remaining pipeline where appropriate.

---

# 16. Dataset Indexing

After download, generate an index.

Example

dataset_index.csv

Columns

Dataset

Timestamp

Satellite

Channel

Path

Status

Validation

Metadata File

---

# 17. Security Considerations

Never download datasets from unofficial sources.

Validate HTTPS certificates where applicable.

Avoid executing downloaded content.

Restrict file permissions appropriately.

---

# 18. AI Agent Responsibilities

The AI agent shall:

- Download official datasets.
- Verify file integrity.
- Preserve metadata.
- Build dataset manifests.
- Organize directory structure.
- Generate logs.
- Resume interrupted downloads.
- Validate before preprocessing.

---

# 19. Acceptance Criteria

The acquisition pipeline is complete when:

✓ All required datasets have been downloaded.

✓ Directory structure is correct.

✓ Metadata has been extracted.

✓ Manifest generated.

✓ Dataset index created.

✓ Logs generated.

✓ Validation passed.

Only then may the preprocessing stage begin.

---

# 20. Future Enhancements

Potential improvements include:

- Parallel downloads
- Cloud object storage integration
- Incremental synchronization
- Dataset versioning
- Automatic update scheduler
- Multi-threaded downloading
- Distributed data ingestion
- Automatic archival of old datasets

---

# Definition of Done

This document is considered complete when:

- Official dataset sources are defined.
- Download procedures are documented.
- Storage policies are established.
- Metadata handling is specified.
- AI agent responsibilities are clear.
- Validation and logging requirements are complete.
- The acquisition workflow is reproducible and ready for implementation.
