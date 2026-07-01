# Model Evaluation

**Project:** Fill in the Frames Seamlessly – Enhancing Temporal Resolution of Satellite Imagery using AI/ML based Optical Flow

**Document Version:** 1.0

**Status:** Approved

**Owner:** AI Evaluation Team

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

**Next Document**

15_INSAT_Inference.md

---

# 1. Purpose

The purpose of this module is to quantitatively and qualitatively evaluate the trained Frame Interpolation model.

Evaluation determines whether the generated intermediate satellite frame is scientifically meaningful and sufficiently similar to the actual ground-truth observation.

The evaluation results shall be used to:

- Select the best model
- Compare candidate architectures
- Validate interpolation quality
- Generate benchmark reports
- Support deployment decisions

---

# 2. Objectives

The evaluation module shall

✔ Compare prediction with ground truth

✔ Compute image quality metrics

✔ Evaluate cloud movement preservation

✔ Detect interpolation artifacts

✔ Measure inference speed

✔ Generate reports

✔ Rank trained models

✔ Produce publication-quality graphs

---

# 3. Evaluation Workflow

Ground Truth Frame

↓

Generated Frame

↓

Metric Computation

↓

Visualization

↓

Comparison Report

↓

Model Ranking

↓

Deployment Decision

---

# 4. Evaluation Inputs

Required Inputs

Ground Truth Frame

Generated Frame

Model Checkpoint

Metadata

Experiment Configuration

---

# 5. Expected Outputs

Outputs

Evaluation Report

CSV Metrics

Plots

Comparison Images

Difference Maps

Heatmaps

Performance Summary

Leaderboard

---

# 6. Quantitative Metrics

Mandatory Metrics

SSIM

Structural Similarity Index

Measures structural similarity.

Higher is better.

---

PSNR

Peak Signal-to-Noise Ratio

Measures reconstruction quality.

Higher is better.

---

MSE

Mean Squared Error

Measures pixel-wise error.

Lower is better.

---

FSIM

Feature Similarity Index

Captures perceptual similarity.

Higher is better.

---

# 7. Optional Metrics

LPIPS

Perceptual Similarity

Optical Flow Consistency

Temporal Consistency

Cloud Boundary Error

Inference Time

GPU Memory Usage

Model Size

---

# 8. Scientific Evaluation

Evaluate

Cloud Shape Preservation

Storm Rotation

Cyclone Structure

Temperature Continuity

Atmospheric Motion

Cloud Boundary Accuracy

This ensures scientific usefulness beyond simple pixel similarity.

---

# 9. Difference Maps

Generate

Prediction − Ground Truth

Visualize

Absolute Error

Relative Error

Temperature Difference

Difference maps assist in identifying systematic interpolation errors.

---

# 10. Heatmaps

Generate heatmaps for

SSIM

MSE

Prediction Error

Cloud Motion Error

These visualizations help locate regions where the model performs well or poorly.

---

# 11. Temporal Consistency

Evaluate consistency across consecutive interpolated frames.

Check

Frame Flickering

Abrupt Motion

Temporal Noise

Cloud Continuity

---

# 12. Benchmark Generation

For every evaluated model generate

Metrics Table

Comparison Images

Evaluation Plots

Summary Report

Final Ranking

---

# 13. Model Comparison

Automatically generate comparison tables.

Example

| Model | SSIM | PSNR | MSE | FSIM | Time |
|-------|------|------|------|------|------|
| RIFE | 0.95 | 39.8 | 18.2 | 0.97 | 0.05s |
| IFRNet | ... | ... | ... | ... | ... |

Values shown above are examples only. Actual values must come from measured evaluation results.

---

# 14. Performance Evaluation

Measure

Inference Time

GPU Usage

CPU Usage

Memory Consumption

Batch Throughput

Frames Per Second

---

# 15. Visualization

Generate

Ground Truth

↓

Prediction

↓

Difference Map

↓

Heatmap

↓

Metric Table

↓

Summary Report

These visualizations shall be displayed in the dashboard.

---

# 16. Automatic Report Generation

Generate

evaluation_report.pdf

evaluation.csv

evaluation.json

comparison.png

metrics.png

leaderboard.csv

The report shall summarize

Model

Dataset

Metrics

Hardware

Training Configuration

Evaluation Time

---

# 17. Logging

Record

Timestamp

Model Name

Checkpoint

Dataset

Inference Time

Metrics

Warnings

Errors

---

# 18. Error Handling

Recoverable

Missing optional metric

Visualization failure

Temporary I/O issue

Retry

↓

Continue

Critical

Ground Truth Missing

Prediction Missing

Dimension Mismatch

Invalid Tensor

Stop evaluation.

Generate diagnostics.

---

# 19. AI Agent Responsibilities

The AI Agent shall

Load model

Load checkpoint

Run inference

Compare with ground truth

Compute metrics

Generate plots

Generate reports

Update PROJECT_STATUS.md

Store evaluation outputs

---

# 20. Folder Structure

evaluation/

metrics.py

compare.py

visualize.py

reports.py

leaderboard.py

configs/

utils/

outputs/

---

# 21. Validation Checklist

Before accepting evaluation

✔ Ground truth available

✔ Prediction generated

✔ Metrics computed

✔ Difference maps generated

✔ Reports created

✔ Logs created

✔ Dashboard visualizations generated

---

# 22. Acceptance Criteria

Evaluation is complete when

✓ All mandatory metrics computed.

✓ Comparison images generated.

✓ Reports generated.

✓ Leaderboard created.

✓ Visualizations available.

✓ Logs generated.

✓ Best model identified using measured results.

---

# 23. Future Enhancements

Cloud-specific evaluation metrics

Meteorological feature tracking

Region-wise evaluation

Real-time benchmark dashboard

Multi-satellite evaluation

Automatic model ranking website

Continuous evaluation pipeline

---

# 24. Definition of Done

This document is complete when

- Quantitative evaluation is implemented.
- Scientific evaluation is completed.
- Reports and plots are automatically generated.
- The best-performing model is selected based on measured evidence.
- Results are ready for visualization and deployment.

Only after successful evaluation shall the project proceed to applying the selected model on INSAT-3DS/3DR datasets for inference.
