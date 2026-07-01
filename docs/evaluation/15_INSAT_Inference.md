# INSAT Inference

**Project:** Fill in the Frames Seamlessly – Enhancing Temporal Resolution of Satellite Imagery using AI/ML based Optical Flow

**Document Version:** 1.0

**Status:** Approved

**Owner:** AI Inference Engineering Team

**Depends On:**

- 01_Project_Mission.md
- 02_Repository_Architecture.md
- 03_System_Architecture.md
- 04_Data_Flow.md
- 05_API_Architecture.md
- 06_Dataset_Acquisition.md
- 07_Dataset_Validation.md
- 08_Preprocessing.md
- 09_Training_Dataset_Generation.md
- 10_Model_Selection.md
- 11_Optical_Flow.md
- 12_Frame_Interpolation.md
- 13_Model_Training.md
- 14_Model_Evaluation.md

**Next Document**

16_Backend.md

---

# 1. Purpose

The objective of this module is to deploy the trained Frame Interpolation model on real INSAT-3DS/3DR Thermal Infrared imagery and generate scientifically consistent intermediate frames.

This is the final AI inference stage of the project.

The generated frames shall increase the apparent temporal resolution of INSAT imagery from

30 minutes

↓

15 minutes

↓

(Optional Future)

7.5 minutes

without modifying the original observations.

---

# 2. Objectives

The inference pipeline shall

✔ Read INSAT datasets

✔ Preserve metadata

✔ Generate intermediate frames

✔ Restore scientific format

✔ Export NetCDF

✔ Produce visualization outputs

✔ Generate reports

✔ Compute evaluation metrics (where ground truth exists)

---

# 3. Input

Supported inputs

NetCDF (.nc)

HDF5 (.h5)

Dataset

INSAT-3DS

INSAT-3DR

Required Channel

TIR1

---

# 4. Output

Generated outputs

Interpolated NetCDF

Interpolated PNG

Animation GIF

MP4

Evaluation Report

Comparison Images

Dashboard Files

Logs

---

# 5. Inference Workflow

INSAT Dataset

↓

Read NetCDF

↓

Read Metadata

↓

Extract TIR1

↓

Preprocessing

↓

Load Trained Model

↓

Generate Optical Flow

↓

Frame Interpolation

↓

Metadata Restoration

↓

NetCDF Writer

↓

Evaluation

↓

Dashboard

---

# 6. Metadata Preservation

The following metadata shall be preserved.

Satellite Name

Sensor

Acquisition Time

Projection

Latitude

Longitude

Resolution

Units

Channel Information

Processing History

No metadata shall be discarded during inference.

---

# 7. Model Loading

Load

Best Checkpoint

↓

Verify Compatibility

↓

Load Configuration

↓

Initialize GPU

↓

Ready for Inference

---

# 8. Batch Inference

Support

Single Pair

Folder

Recursive Processing

Entire Day

Entire Month

Entire Dataset

Batch size shall be configurable.

---

# 9. Intermediate Timestamp Generation

Example

00:00

↓

AI

↓

00:15

↓

00:30

Future Extension

00:00

↓

00:07:30

↓

00:15

↓

00:22:30

↓

00:30

Interpolation factor shall be configurable.

---

# 10. NetCDF Reconstruction

Generated tensor

↓

Convert Image

↓

Restore Metadata

↓

Restore Variables

↓

Write NetCDF

↓

Validate File

Generated files should preserve compatibility with downstream scientific tools where feasible.

---

# 11. Output Directory

outputs/

INSAT/

netcdf/

animations/

comparison/

reports/

metrics/

logs/

---

# 12. Evaluation

When corresponding observations are available

Compare

Generated Frame

↓

Ground Truth

Compute

SSIM

PSNR

MSE

FSIM

Generate reports.

If no ground truth exists, clearly indicate that only qualitative evaluation is possible.

---

# 13. Visualization

Generate

Original Animation

Interpolated Animation

Side-by-Side Comparison

Difference Maps

Heatmaps

Timeline Playback

These shall be integrated into the dashboard.

---

# 14. Performance Optimization

Support

Mixed Precision

GPU Inference

Batch Processing

Tensor Caching

Memory Optimization

Asynchronous File Loading

---

# 15. Logging

Record

Timestamp

Input File

Output File

Model Version

Inference Time

GPU Usage

Memory Usage

Metrics

Warnings

Errors

---

# 16. Error Handling

Recoverable

GPU OOM

Missing cache

Temporary file access issue

Retry

↓

Continue

Critical

Corrupted NetCDF

Missing metadata

Checkpoint failure

Invalid tensor

Stop current inference.

Generate diagnostics.

Continue remaining files if appropriate.

---

# 17. AI Agent Responsibilities

The AI Agent shall

Load INSAT dataset

Validate input

Run preprocessing

Load trained model

Generate intermediate frames

Restore metadata

Export NetCDF

Generate visualizations

Generate evaluation reports

Update PROJECT_STATUS.md

---

# 18. Folder Structure

inference/

infer.py

netcdf_writer.py

metadata.py

batch.py

export.py

visualization.py

configs/

utils/

---

# 19. Validation Checklist

Before accepting inference

✔ Input dataset validated

✔ Metadata preserved

✔ Intermediate frame generated

✔ NetCDF exported

✔ Reports generated

✔ Animations generated

✔ Logs created

✔ Dashboard compatible

---

# 20. Acceptance Criteria

Inference is complete when

✓ INSAT datasets processed.

✓ Intermediate frames generated.

✓ Metadata preserved.

✓ NetCDF exported.

✓ Evaluation completed (where possible).

✓ Dashboard visualizations generated.

✓ Logs stored.

---

# 21. Future Enhancements

Support INSAT-3D

Support additional spectral channels

Near real-time inference

Cloud deployment

Multi-GPU inference

Streaming satellite feeds

Physics-informed post-processing

---

# 22. Definition of Done

This document is complete when

- The trained model successfully generates intermediate INSAT frames.
- Scientific metadata is preserved.
- Output NetCDF files are generated.
- Animations and reports are available.
- Outputs are compatible with the dashboard.

Only after successful INSAT inference shall the project proceed to Backend API implementation.
