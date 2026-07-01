
# Repository Architecture

**Project:** Fill in the Frames Seamlessly – Enhancing Temporal Resolution of Satellite Imagery using AI/ML based on Optical Flow

**Document Version:** 1.0

**Status:** Approved

**Owner:** AI Software Engineering Team

**Depends On:** 01_Project_Mission.md

**Next Document:** 03_System_Architecture.md

---

# 1. Purpose

This document defines the complete repository architecture for the project.

Its purpose is to establish a clean, scalable, maintainable, and production-ready project structure that supports:

- AI model development
- Scientific data processing
- Backend services
- Frontend dashboard
- Automated testing
- Continuous Integration
- Deployment
- Future extensibility

Every file created throughout this project shall conform to the architecture defined in this document.

---

# 2. Repository Design Principles

The repository shall follow the following principles:

## 2.1 Modularity

Each module must have one responsibility.

Avoid mixing:

- Data processing
- Model code
- API code
- Dashboard code
- Utility functions

inside the same module.

---

## 2.2 Scalability

The repository should allow adding:

- New satellite datasets
- New AI models
- New evaluation metrics
- New dashboards
- New APIs

without requiring major restructuring.

---

## 2.3 Reproducibility

All experiments must be reproducible.

Every experiment should be reproducible from:

- Configuration files
- Saved checkpoints
- Logged metadata
- Dataset versions

---

## 2.4 Maintainability

The repository should be understandable by a developer who has never seen the project before.

Documentation should explain every major component.

---

## 2.5 Separation of Concerns

Every directory has exactly one responsibility.

Business logic should never be mixed with UI logic.

Training logic should never be mixed with inference logic.

---

# 3. Root Repository Structure

```text
Fill-In-The-Frames-Seamlessly/

│
├── backend/
├── frontend/
├── dashboard/
├── datasets/
├── preprocessing/
├── models/
├── training/
├── inference/
├── evaluation/
├── configs/
├── outputs/
├── checkpoints/
├── logs/
├── scripts/
├── notebooks/
├── tests/
├── docs/
├── docker/
├── .github/
│
├── README.md
├── MASTER_PROMPT.md
├── PROJECT_STATUS.md
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── LICENSE
```

---

# 4. Folder Responsibilities

## backend/

Responsible for:

- FastAPI
- REST APIs
- Authentication
- Model serving
- File upload
- File download
- Job management

Nothing related to ML training should exist here.

---

## frontend/

Contains

- Next.js
- React
- TypeScript

Responsibilities

- UI
- State Management
- Routing
- API communication

No ML code.

---

## dashboard/

Contains visualization logic only.

Responsibilities

- Timeline
- Heatmaps
- Metrics
- Frame comparison
- Playback
- 3D Globe
- Animation

---

## datasets/

Stores

Raw datasets only.

Never modify.

Structure

datasets/

GOES/

INSAT/

Himawari/

Downloaded/

Metadata/

---

## preprocessing/

Responsible for

- Reading NetCDF
- Reading HDF5
- Metadata extraction
- Normalization
- Image generation
- Data cleaning
- Dataset indexing

Outputs processed datasets.

---

## models/

Contains

Every AI model.

Structure

models/

RIFE/

IFRNet/

SuperSloMo/

EMA-VFI/

shared/

Each model exposes:

train()

infer()

load_checkpoint()

save_checkpoint()

evaluate()

---

## training/

Contains

Training pipeline

Responsibilities

- Dataloader
- Trainer
- Scheduler
- Optimizer
- Loss Functions
- Mixed Precision
- Checkpoint Manager

---

## inference/

Contains

Inference pipeline.

Responsibilities

- Load model
- Load checkpoint
- Generate intermediate frame
- Export output
- Batch inference

---

## evaluation/

Contains

Metric computation.

Includes

- SSIM
- PSNR
- MSE
- FSIM

Generate

CSV

Graphs

Reports

---

## configs/

Contains YAML configuration files.

No parameter should be hardcoded.

Example

dataset.yaml

training.yaml

model.yaml

dashboard.yaml

deployment.yaml

---

## outputs/

Contains

Generated results.

Examples

GIFs

MP4s

PNG

NetCDF

CSV

Reports

---

## checkpoints/

Contains

Model checkpoints.

Support:

Resume Training

Best Model

Latest Model

Epoch Checkpoints

---

## logs/

Contains

Training logs

API logs

Dashboard logs

Deployment logs

Error logs

---

## scripts/

Contains

Automation scripts.

download_dataset.py

train.py

evaluate.py

deploy.py

test.py

---

## notebooks/

Research notebooks.

Used only during experimentation.

Production logic should eventually move into reusable modules.

---

## tests/

Mirror the repository.

Example

tests/

backend/

models/

evaluation/

dashboard/

Every important module must have tests.

---

## docs/

Contains

Specifications

Architecture

Guides

API docs

Deployment docs

User guide

---

## docker/

Contains

Dockerfile

Compose

Scripts

Container configuration

---

## .github/

Contains

GitHub Actions

Issue Templates

PR Templates

Automation

---

# 5. Dependency Rules

The dependency direction shall be

Frontend

↓

Backend

↓

Inference

↓

Models

↓

Preprocessing

↓

Datasets

Never reverse this dependency chain.

Avoid circular imports.

---

# 6. Configuration Strategy

Everything configurable shall be stored outside the source code.

Configuration includes

- Dataset paths
- Learning rates
- Batch size
- Model selection
- GPU configuration
- API endpoints
- Deployment settings

Preferred formats

- YAML
- TOML
- Environment Variables

---

# 7. Logging Strategy

Every module shall generate structured logs.

Each log entry should include:

- Timestamp
- Module
- Operation
- Status
- Duration
- Warning/Error Details (if any)

Use consistent logging across the project.

---

# 8. Error Handling

Recoverable errors:

- Retry if appropriate.
- Log the failure.
- Continue when safe.

Critical errors:

- Stop the current phase.
- Record diagnostics.
- Require resolution before proceeding.

---

# 9. Coding Standards

Use:

- Type hints where practical.
- Descriptive names.
- Docstrings for public functions.
- Consistent formatting.
- Small, focused modules.
- Avoid duplicated logic.

---

# 10. Testing Philosophy

Every feature introduced must include corresponding tests.

Testing layers include:

- Unit Tests
- Integration Tests
- End-to-End Tests
- Regression Tests (where practical)

No phase is considered complete until required tests pass.

---

# 11. Documentation Standards

Every major module should document:

- Purpose
- Inputs
- Outputs
- Configuration
- Limitations
- Usage examples

Documentation should evolve with the implementation.

---

# 12. AI Agent Responsibilities

During implementation the AI agent shall:

- Respect this architecture.
- Never place files in incorrect directories.
- Never duplicate functionality unnecessarily.
- Keep documentation synchronized with implementation.
- Validate structural integrity after major changes.
- Maintain a clean and organized repository.

---

# 13. Acceptance Criteria

This document is considered satisfied when:

- Repository follows the defined structure.
- Responsibilities are clearly separated.
- No redundant folders exist.
- Configuration is externalized.
- Logging and testing strategies are adopted.
- Documentation accurately reflects the implementation.
