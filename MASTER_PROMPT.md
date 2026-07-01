# MASTER_PROMPT.md

# AI Agent Master Execution Prompt

## Project

**Fill in the Frames Seamlessly – Enhancing Temporal Resolution of Satellite Imagery using AI/ML based Optical Flow**

---

# Purpose

This document defines how the AI coding agent must execute the project from start to finish.

The implementation details are contained in the specification documents located inside the `/docs` directory.

The AI agent must use this document as the primary execution guide and the documents inside `/docs` as the authoritative technical specification.

---

# Mission

Build a complete production-quality AI-powered satellite frame interpolation platform capable of:

* Acquiring official satellite datasets.
* Processing scientific NetCDF and HDF5 data.
* Preserving metadata.
* Training or fine-tuning deep learning frame interpolation models.
* Generating realistic intermediate satellite frames.
* Evaluating generated outputs using scientific metrics.
* Providing a modern web dashboard.
* Deploying the application.
* Producing a reproducible and maintainable software project.

---

# Execution Order

Read the following specification documents sequentially before implementing each phase.

1. 01_Project_Mission.md
2. 02_Repository_Architecture.md
3. 03_Dataset_Acquisition.md
4. 04_Preprocessing.md
5. 05_Dataset_Generation.md
6. 06_Model_Selection.md
7. 07_Training.md
8. 08_Evaluation.md
9. 09_Inference.md
10. 10_Dashboard.md
11. 11_Testing.md
12. 12_Backend.md
13. 13_Frontend.md
14. 14_Deployment.md
15. 15_Final_Verification.md

Never skip a document.

---

# Autonomous Execution Rules

Once the required permissions and credentials have been legitimately provided:

* Continue implementation without asking for unnecessary confirmations.
* Execute the current phase completely before moving to the next.
* Retry recoverable failures automatically.
* Generate logs after every major operation.
* Preserve intermediate outputs.
* Save checkpoints where applicable.
* Produce meaningful Git commits after verified milestones.
* Push changes if Git authentication is already configured.
* Deploy services if deployment credentials are already configured.

Pause only when:

* Required credentials are unavailable.
* Essential user input is missing.
* An external dependency is unavailable.
* Continuing would affect resources outside the agreed project scope.

---

# Engineering Principles

Always prioritize:

* Correctness
* Reproducibility
* Maintainability
* Readability
* Scientific validity
* Modular architecture
* Reliable testing
* Measured evaluation

Do not fabricate results.

Do not fabricate evaluation metrics.

Do not claim successful validation unless the required tests have actually passed.

---

# Development Workflow

For every implementation phase:

1. Read the corresponding specification.
2. Design the implementation.
3. Create required folders.
4. Generate code.
5. Configure dependencies.
6. Run static analysis where appropriate.
7. Execute unit tests.
8. Execute integration tests.
9. Validate outputs.
10. Document the results.
11. Commit verified work.
12. Update project status.

Proceed only after the phase passes all required validation checks.

---

# Model Development Strategy

Evaluate multiple suitable frame interpolation models.

Potential candidates include:

* RIFE
* IFRNet
* Super SloMo
* EMA-VFI

Compare models using measured validation metrics.

Select the best-performing model based on actual results.

Document the reasons for the selection.

---

# Dataset Handling

Download datasets only from official sources specified in the project documentation.

Preserve raw datasets.

Never overwrite original files.

Perform integrity checks after download.

Validate file formats before preprocessing.

Preserve metadata throughout the pipeline.

---

# Testing Strategy

Every module must include appropriate testing.

Validation should include:

* Data validation
* Functional verification
* Unit tests
* Integration tests
* End-to-end verification where appropriate

If a critical validation fails:

1. Record the failure.
2. Diagnose the cause.
3. Apply a fix.
4. Re-run validation.
5. Continue only after successful verification.

---

# Dashboard Goals

Provide a modern interface that allows users to:

* Upload supported datasets.
* Select available models.
* Execute interpolation.
* View original frames.
* View interpolated frames.
* Compare against ground truth (when available).
* Display evaluation metrics.
* Visualize optical flow.
* Download generated outputs.

The interface should be responsive, smooth, and visually polished.

---

# Deployment

When implementation and validation are complete:

* Build production artifacts.
* Deploy the frontend (when authenticated deployment is available).
* Deploy the backend to a suitable Python-compatible hosting platform (when authenticated deployment is available).
* Verify production functionality.
* Perform end-to-end production testing.
* Record deployment results.

---

# Logging Requirements

Maintain logs for:

* Dataset acquisition
* Preprocessing
* Training
* Validation
* Inference
* Evaluation
* Dashboard
* Deployment

Logs should include timestamps, execution status, durations, and error details where applicable.

---

# Documentation Requirements

Ensure documentation remains synchronized with the implementation.

Update relevant documents whenever architecture or behavior changes.

Generate user-facing documentation where appropriate.

---

# Definition of Done

The project is considered complete only when:

* All specified functionality has been implemented.
* Required validation has passed.
* Tests have passed.
* Documentation is current.
* Deployment has completed successfully (when authenticated deployment targets are available).
* The application demonstrates the complete workflow from dataset ingestion through visualization.

---

# Final Deliverables

The completed project should include:

* Modular source code.
* Configuration files.
* Dataset processing pipeline.
* Training pipeline.
* Inference pipeline.
* Evaluation tools.
* Interactive dashboard.
* Automated tests.
* Deployment configuration.
* Documentation.
* Logs and evaluation reports.

The resulting system should be reproducible, maintainable, and suitable for further research and development.
