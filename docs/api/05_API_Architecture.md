
# API Architecture

**Project:** Fill in the Frames Seamlessly – Enhancing Temporal Resolution of Satellite Imagery using AI/ML based Optical Flow

**Document Version:** 1.0

**Status:** Approved

**Owner:** Backend Engineering Team

**Depends On:**
- 01_Project_Mission.md
- 02_Repository_Architecture.md
- 03_System_Architecture.md
- 04_Data_Flow.md

**Next Document:**
06_Dataset_Acquisition.md

---

# 1. Purpose

This document defines the complete REST API architecture.

The backend exposes services for:

- Dataset upload
- Dataset management
- Model inference
- Evaluation
- Downloading outputs
- Dashboard interaction
- Health monitoring

Every API shall follow REST principles and automatically generate OpenAPI (Swagger) documentation.

---

# 2. Backend Technology

Framework:

FastAPI

Advantages

- Automatic Swagger UI
- High performance
- Async support
- Native Pydantic validation
- Excellent ML integration

---

# 3. API Versioning

All endpoints begin with:

/api/v1/

Example

/api/v1/upload

Future versions:

/api/v2/

---

# 4. Authentication

For development:

Authentication optional.

For production:

Support:

- API Key
- JWT (optional)
- Role-based access (future)

---

# 5. Standard Response Format

Successful Response

```json
{
  "success": true,
  "message": "Operation completed successfully.",
  "data": {},
  "timestamp": "ISO-8601"
}
```

Error Response

```json
{
  "success": false,
  "error": {
    "code": "INVALID_FILE",
    "message": "Uploaded file is not supported."
  },
  "timestamp": "ISO-8601"
}
```

---

# 6. Upload API

POST

/api/v1/upload

Purpose

Upload:

- .nc
- .h5

Validation

- File type
- File size
- Readability
- Required metadata

Response

File ID

Metadata

Status

---

# 7. Dataset API

GET

/api/v1/datasets

Returns

Available datasets

Example

GOES

INSAT

Himawari

Sample datasets

---

# 8. Dataset Details

GET

/api/v1/datasets/{dataset_id}

Returns

Metadata

Timestamp

Resolution

Satellite

Channel

Dimensions

---

# 9. Model List

GET

/api/v1/models

Returns

Installed models

Current default

Supported checkpoints

---

# 10. Run Inference

POST

/api/v1/inference

Input

Dataset ID

Model Name

Parameters

Output

Job ID

Estimated time

---

# 11. Inference Status

GET

/api/v1/inference/{job_id}

Returns

Queued

Running

Completed

Failed

Progress %

---

# 12. Retrieve Result

GET

/api/v1/results/{job_id}

Returns

Generated files

Metrics

Download links

---

# 13. Evaluation API

GET

/api/v1/evaluation/{job_id}

Returns

SSIM

PSNR

MSE

FSIM

Inference Time

---

# 14. Download API

GET

/api/v1/download/{job_id}

Downloads

NetCDF

GIF

MP4

CSV

Report

---

# 15. Dashboard APIs

Provide

Current jobs

History

Metrics

System status

Available datasets

Available models

---

# 16. Health Check

GET

/api/v1/health

Returns

API status

GPU status

Model status

Disk usage

Memory usage

Version

---

# 17. Logs API

GET

/api/v1/logs

Purpose

Development diagnostics

Should be restricted in production.

---

# 18. Configuration API

GET

/api/v1/config

Returns

Current configuration

Model

Dataset

GPU

Batch size

Read-only by default.

---

# 19. API Validation

Every endpoint shall validate:

- Request schema
- File types
- Parameter ranges
- Required fields
- Resource existence

Invalid requests return appropriate HTTP status codes.

---

# 20. HTTP Status Codes

200 OK

201 Created

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

409 Conflict

413 Payload Too Large

422 Validation Error

429 Too Many Requests

500 Internal Server Error

503 Service Unavailable

---

# 21. File Upload Constraints

Supported

.nc

.h5

Maximum upload size shall be configurable.

Reject unsupported formats.

---

# 22. Async Jobs

Long-running operations such as inference shall execute asynchronously.

Client workflow:

Submit job

↓

Receive Job ID

↓

Poll Status

↓

Retrieve Results

---

# 23. OpenAPI Documentation

The backend shall expose:

/docs

Swagger UI

/redoc

ReDoc Documentation

Both generated automatically by FastAPI.

---

# 24. Security

Validate uploads.

Prevent directory traversal.

Sanitize filenames.

Limit upload sizes.

Restrict dangerous file types.

Protect sensitive configuration.

---

# 25. Logging

Every request shall log:

Timestamp

Endpoint

Method

Duration

Status Code

Client IP (where appropriate)

Errors

---

# 26. Acceptance Criteria

The API architecture is accepted when:

- Endpoints are documented.
- Validation rules are defined.
- Standard responses are used.
- Error handling is specified.
- OpenAPI documentation is available.
- Backend and frontend can communicate through stable contracts.
