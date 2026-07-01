
# Dataset Validation

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

**Next Document:**

08_Preprocessing.md

---

# 1. Purpose

The purpose of this document is to define the complete validation pipeline for every satellite dataset before it enters preprocessing.

Every downloaded file shall undergo multiple validation stages to ensure:

- Scientific correctness
- Metadata completeness
- Temporal consistency
- Spatial consistency
- Data integrity
- Model compatibility

No dataset shall proceed to preprocessing unless all required validation checks have passed.

---

# 2. Validation Objectives

The validation pipeline shall ensure:

✔ File is readable

✔ File format is supported

✔ Required metadata exists

✔ Required thermal infrared channel exists

✔ Timestamp is valid

✔ Latitude and longitude grids are valid

✔ Image dimensions are correct

✔ Missing values are identified

✔ Corrupted files are rejected

✔ Dataset manifest is updated

---

# 3. Supported File Formats

The validation module shall support:

• NetCDF (.nc)

• HDF5 (.h5)

Reject:

- ZIP archives (until extracted)
- Unsupported binary files
- Images without metadata
- Partial downloads

---

# 4. Validation Workflow

Downloaded Dataset

↓

File Exists

↓

File Size Check

↓

Open Dataset

↓

Read Metadata

↓

Validate Variables

↓

Validate Dimensions

↓

Validate Timestamp

↓

Validate Required Channel

↓

Validate Data Values

↓

Validation Report

↓

Pass / Fail

---

# 5. File Integrity Validation

Checks:

- File exists
- File size > 0
- File readable
- Correct extension
- No truncation

Failure Action:

Reject file.

Record reason.

Continue with remaining datasets.

---

# 6. Metadata Validation

Verify presence of:

Satellite Name

Sensor

Acquisition Time

Projection

Latitude

Longitude

Resolution

Channel Information

Units

Missing metadata shall trigger a validation failure.

---

# 7. Variable Validation

Verify that required variables exist.

For GOES:

Example variables:

CMI

DQF

x

y

t

For INSAT:

Verify:

TIR1

Navigation Variables

Calibration Variables

The exact variable names depend on the dataset specification and should be configurable rather than hard-coded.

---

# 8. Channel Validation

Required channel:

GOES

Channel 13

INSAT

TIR1

Himawari

Equivalent Thermal Infrared Channel

If missing:

Reject dataset.

---

# 9. Timestamp Validation

Verify:

- Timestamp exists
- Timestamp format valid
- Chronological ordering
- No duplicate timestamps

Dataset ordering shall be deterministic.

---

# 10. Dimension Validation

Verify:

Image Width

Image Height

Latitude Grid

Longitude Grid

Dimension consistency across files.

Unexpected dimensions should be logged and reviewed.

---

# 11. Missing Value Detection

Detect:

NaN

Infinity

Missing Pixels

Invalid Radiance

Fill Values

Generate statistics.

If missing data exceeds configurable thresholds, flag the file for review or exclusion.

---

# 12. Scientific Range Validation

Verify brightness temperature values fall within physically reasonable ranges for the selected product.

Example checks:

Minimum value

Maximum value

Mean

Standard deviation

Values outside expected ranges should generate warnings or validation failures depending on severity.

---

# 13. Duplicate Detection

Check:

Filename

Timestamp

Checksum (if available)

Metadata

Duplicate files shall not be processed twice.

---

# 14. Dataset Consistency

Verify consistency across sequences:

Resolution

Projection

Channel

Image Dimensions

Metadata Schema

Mixed datasets shall not be grouped into one sequence unless explicitly supported.

---

# 15. Manifest Validation

Update dataset_manifest.csv

Columns:

Dataset

Filename

Timestamp

Validation Status

Failure Reason

Metadata Status

Checksum Status

Processing Status

---

# 16. Validation Report

Generate:

validation_report.csv

validation_report.json

Include:

Passed Files

Failed Files

Warnings

Errors

Summary Statistics

---

# 17. Logging

Log every validation operation.

Example fields:

Timestamp

Dataset

Filename

Validation Step

Status

Duration

Error Message

---

# 18. Error Categories

Recoverable

Missing optional metadata

Minor warnings

Temporary read issues

Critical

Unreadable file

Missing required variables

Corrupted structure

Missing required channel

Invalid dimensions

Critical failures prevent preprocessing.

---

# 19. AI Agent Responsibilities

The AI agent shall:

- Validate every downloaded file
- Generate validation reports
- Update manifests
- Detect duplicates
- Preserve metadata
- Reject invalid datasets
- Continue processing valid datasets
- Log all validation activities

---

# 20. Validation Checklist

Before preprocessing, confirm:

✔ Dataset readable

✔ Metadata complete

✔ Channel verified

✔ Timestamp valid

✔ Dimensions verified

✔ Missing values acceptable

✔ Manifest updated

✔ Logs generated

✔ Reports generated

---

# 21. Acceptance Criteria

Dataset validation is complete when:

✓ Every downloaded dataset has been checked.

✓ Validation reports are generated.

✓ Invalid files are isolated.

✓ Dataset manifest updated.

✓ Metadata preserved.

✓ Logs generated.

✓ Only validated datasets proceed to preprocessing.

---

# 22. Future Enhancements

Potential improvements:

- Automatic checksum verification using official manifests
- Parallel validation
- Cloud storage validation
- Metadata schema versioning
- Interactive validation dashboard
- Automated anomaly detection

---

# Definition of Done

This document is considered complete when:

- Validation workflow is fully specified.
- Metadata checks are defined.
- Scientific integrity checks are documented.
- Error handling is established.
- Logging and reporting requirements are complete.
- Acceptance criteria are satisfied.

Only after successful validation shall datasets enter the preprocessing pipeline.
