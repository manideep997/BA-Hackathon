
# Optical Flow

**Project:** Fill in the Frames Seamlessly – Enhancing Temporal Resolution of Satellite Imagery using AI/ML based Optical Flow

**Document Version:** 1.0

**Status:** Approved

**Owner:** Computer Vision Engineering Team

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

**Next Document**

12_Frame_Interpolation.md

---

# 1. Purpose

The objective of this module is to estimate the motion between two consecutive satellite images.

The estimated motion field (Optical Flow) is later used by the Frame Interpolation Model to synthesize an intermediate satellite frame.

Since satellite imagery contains continuous cloud movement, storm evolution, cyclone rotation, atmospheric convection and large-scale weather dynamics, precise optical flow estimation is the foundation of the entire project.

---

# 2. Objectives

The Optical Flow module shall:

✔ Estimate pixel-wise motion.

✔ Preserve cloud structures.

✔ Detect atmospheric movement.

✔ Handle occlusions.

✔ Handle newly appearing clouds.

✔ Produce dense motion vectors.

✔ Integrate seamlessly with Frame Interpolation.

✔ Support visualization.

---

# 3. Why Optical Flow?

Without Optical Flow,

the interpolation model has no understanding of

- where clouds move

- how fast they move

- direction of motion

- object deformation

- appearance/disappearance

Instead of simply blending two images,

Optical Flow estimates

Motion(A → B)

which allows the interpolation network to create realistic intermediate frames.

---

# 4. Optical Flow Pipeline

Frame A

↓

Preprocessing

↓

Feature Extraction

↓

Motion Estimation

↓

Flow Refinement

↓

Occlusion Detection

↓

Dense Flow Map

↓

Frame Interpolation Module

---

# 5. Optical Flow Types

### Sparse Optical Flow

Tracks selected feature points.

Advantages

Fast.

Disadvantages

Insufficient for satellite imagery.

Not recommended.

---

### Dense Optical Flow

Computes motion for every pixel.

Advantages

Captures cloud movement.

Produces continuous flow fields.

Recommended.

---

# 6. Candidate Optical Flow Models

Evaluate:

RAFT

GMFlow

FlowFormer

PWC-Net

LiteFlowNet

SpyNet

The implementation shall benchmark multiple methods and select the most suitable one for the project.

---

# 7. Recommended Model

RAFT

Reasons

Excellent accuracy.

Strong generalization.

Dense motion estimation.

Widely adopted.

Supports fine-tuning.

Strong research support.

---

# 8. Input

Frame A

Frame B

Both shall have

same resolution

same channel

same projection

same preprocessing

---

# 9. Output

Dense Optical Flow

Dimensions

Height × Width × 2

Channel 1

Horizontal Motion (u)

Channel 2

Vertical Motion (v)

---

# 10. Motion Vector Estimation

For every pixel

Estimate

Δx

Δy

These represent

Horizontal motion

Vertical motion

Store flow using float precision.

---

# 11. Multi-Scale Estimation

Estimate motion

Coarse Scale

↓

Medium Scale

↓

Fine Scale

This improves

Large cloud movement

Small cloud movement

Storm boundaries

---

# 12. Occlusion Handling

Clouds may

Disappear

Appear

Merge

Split

The Optical Flow module shall estimate

Occlusion Masks

to prevent artifacts.

---

# 13. Warping

Using the estimated flow,

warp Frame A

towards

Frame B.

The warped frame serves as an intermediate representation for the interpolation model.

---

# 14. Flow Refinement

Refine motion estimates using

Residual Networks

Attention

Context Aggregation

Iterative Updates

Reduce

Noise

Motion discontinuities

Artifacts

---

# 15. Loss Functions

Possible losses

Endpoint Error (EPE)

Photometric Loss

Smoothness Loss

Occlusion Loss

Charbonnier Loss

The exact combination shall be selected experimentally and documented.

---

# 16. Visualization

Generate

Color Flow Maps

Arrow Vector Fields

Magnitude Maps

Direction Maps

These visualizations assist in debugging and qualitative evaluation.

---

# 17. Performance Optimization

Support

Mixed Precision

GPU Acceleration

Batch Processing

Memory Optimization

Parallel Inference

---

# 18. Logging

Record

Timestamp

Input Frames

Flow Computation Time

GPU Usage

Memory Usage

Model Used

Warnings

Errors

---

# 19. Error Handling

Recoverable

Small corrupted region

Temporary GPU OOM

Missing cache

Retry

↓

Continue

Critical

Unreadable image

Invalid tensor

Dimension mismatch

Stop current sample

Continue remaining batch

---

# 20. AI Agent Responsibilities

The AI Agent shall

Load Optical Flow model.

Estimate dense motion.

Generate occlusion masks.

Visualize flow.

Validate outputs.

Generate logs.

Export flow tensors.

Store intermediate files.

---

# 21. Folder Structure

models/

optical_flow/

RAFT/

FlowFormer/

GMFlow/

utils/

visualization/

losses/

configs/

---

# 22. Validation

Verify

Flow dimensions

No NaN

Correct tensor type

Correct resolution

Flow continuity

Reasonable motion magnitude

Visualization generated

---

# 23. Acceptance Criteria

The Optical Flow module is accepted when

✓ Motion estimated correctly.

✓ Dense flow generated.

✓ Occlusion handled.

✓ Logs created.

✓ Visualization available.

✓ Validation passed.

✓ Compatible with Frame Interpolation module.

---

# 24. Future Enhancements

Possible improvements

Transformer-based flow estimation

Self-supervised optical flow

Multi-frame optical flow

3D atmospheric motion estimation

Cloud-aware flow refinement

Real-time optimization

Distributed inference

---

# 25. Definition of Done

This document is complete when

- Dense optical flow estimation is implemented.

- Motion vectors are validated.

- Occlusion masks are generated.

- Flow visualizations are produced.

- Outputs integrate directly with the Frame Interpolation module.

Only after successful Optical Flow estimation shall the project proceed to Frame Interpolation.
