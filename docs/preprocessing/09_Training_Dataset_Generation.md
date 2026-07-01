# Training Dataset Generation

**Project:** Fill in the Frames Seamlessly – Enhancing Temporal Resolution of Satellite Imagery using AI/ML based Optical Flow

**Document Version:** 1.0

**Status:** Approved

**Owner:** Machine Learning Engineering Team

**Depends On:**

- 01_Project_Mission.md
- 02_Repository_Architecture.md
- 03_System_Architecture.md
- 04_Data_Flow.md
- 05_API_Architecture.md
- 06_Dataset_Acquisition.md
- 07_Dataset_Validation.md
- 08_Preprocessing.md

**Next Document:**

10_Model_Selection.md

---

# 1. Purpose

This document defines how AI-ready training datasets shall be generated from preprocessed satellite observations.

The objective is to transform chronological satellite images into supervised learning samples suitable for frame interpolation.

The generated dataset must preserve:

- Temporal continuity
- Spatial consistency
- Scientific metadata
- Dataset integrity

---

# 2. Objectives

The training dataset generator shall:

✔ Read preprocessed datasets

✔ Generate temporal triplets

✔ Create train/validation/test datasets

✔ Preserve metadata

✔ Remove invalid sequences

✔ Generate dataset manifests

✔ Support configurable temporal intervals

✔ Produce AI-ready datasets

---

# 3. Input

Input source:

processed/

GOES/

INSAT/

Himawari/

Input format:

Tensor files

Metadata files

Validation reports

---

# 4. Output

Generated datasets:

train/

validation/

test/

Each sample shall include:

Input Frames

Ground Truth Frame

Metadata

Manifest Entry

---

# 5. Temporal Triplet Strategy

The interpolation model shall learn using three consecutive frames.

Example:

Frame A (00:00)

↓

Frame B (00:10)

↓

Frame C (00:20)

Training Input:

Frame A

Frame C

Ground Truth:

Frame B

This teaches the model to reconstruct the missing intermediate observation.

---

# 6. Sliding Window Generation

Given a sequence:

F1

F2

F3

F4

F5

Generate:

(F1,F2,F3)

(F2,F3,F4)

(F3,F4,F5)

Continue until the sequence ends.

---

# 7. Configurable Temporal Interval

Support:

10-minute interval

15-minute interval

20-minute interval

30-minute interval

Interval selection shall be configurable.

---

# 8. Sequence Validation

Before creating a training sample verify:

Frames exist

Chronological order correct

No duplicate timestamps

Matching dimensions

Matching metadata

Matching channels

Invalid sequences shall be discarded.

---

# 9. Metadata Preservation

Each sample shall retain:

Satellite Name

Sensor

Timestamp

Projection

Latitude Grid

Longitude Grid

Channel

Resolution

Units

Metadata accompanies every training sample.

---

# 10. Dataset Splitting

Default split:

Training

70%

Validation

15%

Testing

15%

The split ratio shall be configurable.

---

# 11. Randomization

Shuffle training samples only.

Validation and testing shall preserve chronological order where appropriate.

Use deterministic random seeds to ensure reproducibility.

---

# 12. Dataset Manifest

Generate:

train_manifest.csv

validation_manifest.csv

test_manifest.csv

Each entry shall contain:

Sample ID

Input Frame A

Ground Truth Frame

Input Frame C

Timestamp

Dataset

Metadata File

Validation Status

---

# 13. Sample Naming Convention

Example:

sample_000001.pt

sample_000002.pt

sample_000003.pt

Metadata:

sample_000001.json

---

# 14. Storage Layout

training_dataset/

train/

validation/

test/

manifests/

logs/

cache/

---

# 15. Dataset Balancing

Ensure:

Equal representation across time periods where practical.

Avoid excessive duplication.

Provide configurable sampling strategies if dataset distribution is uneven.

---

# 16. Cache Strategy

Cache generated samples.

If source files have not changed:

Reuse cache.

Avoid regenerating identical samples.

---

# 17. Batch Optimization

Generate samples in batches.

Support:

Sequential generation

Parallel generation

Multi-processing

Configurable worker count.

---

# 18. Memory Management

Avoid loading the entire dataset into memory.

Use streaming or lazy loading where practical.

Release unused memory after batch generation.

---

# 19. Logging

Every generated sample shall record:

Timestamp

Sample ID

Input Files

Ground Truth

Output Path

Processing Time

Status

Warnings

Errors

---

# 20. Error Handling

Recoverable Errors

Missing optional metadata

Corrupted sample

Unreadable tensor

Action:

Skip sample

Continue processing

Critical Errors

Missing required frame

Chronological inconsistency

Dimension mismatch

Action:

Reject sequence

Log issue

Continue remaining sequences

---

# 21. AI Agent Responsibilities

The AI agent shall:

Generate temporal triplets

Validate sequences

Split datasets

Generate manifests

Preserve metadata

Optimize storage

Generate logs

Validate outputs

---

# 22. Folder Structure

training_dataset/

train/

validation/

test/

cache/

logs/

manifests/

metadata/

---

# 23. Dataset Quality Metrics

Generate summary statistics:

Number of samples

Number of rejected samples

Average interval

Dataset size

Missing frame count

Channel distribution

Temporal coverage

---

# 24. Validation Checklist

Before model training verify:

✔ Triplets generated

✔ Metadata preserved

✔ Dataset split complete

✔ Manifests generated

✔ Cache created

✔ Logs generated

✔ Validation passed

---

# 25. Acceptance Criteria

The training dataset generation phase is complete when:

✓ Training samples successfully generated.

✓ Validation dataset created.

✓ Testing dataset created.

✓ Metadata preserved.

✓ Dataset manifests generated.

✓ Logs available.

✓ Validation successful.

---

# 26. Future Enhancements

Potential improvements:

Adaptive temporal sampling

Cloud storage support

Distributed generation

Automatic imbalance correction

Sequence quality scoring

Curriculum learning dataset creation

Dynamic interval generation

---

# 27. Definition of Done

This document is considered complete when:

- AI-ready temporal triplets have been generated.
- Dataset splitting is complete.
- Metadata preservation is verified.
- Validation has passed.
- Manifests and logs have been created.

Only after this stage may the project proceed to AI model selection and experimentation.
