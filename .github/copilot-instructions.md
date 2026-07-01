# GitHub Copilot Repository Instructions

## Project

Fill in the Frames Seamlessly – Enhancing Temporal Resolution of Satellite Imagery using AI/ML based Optical Flow

This repository contains the complete implementation of an AI-powered satellite frame interpolation system developed for the Smart India Hackathon.

The objective is to generate scientifically meaningful intermediate satellite frames using Deep Learning and Optical Flow while preserving the integrity of scientific satellite data.

---

# Purpose

This document provides repository-wide instructions for AI coding assistants such as

- GitHub Copilot
- Claude Code
- Cursor
- Windsurf
- Gemini CLI
- Codex
- Antigravity

These instructions are mandatory for every generated file.

---

# Read Before Coding

Before generating any code always read

README.md

↓

PROJECT_STATUS.md

↓

AI_AGENT_RULEBOOK.md

↓

Every Markdown document inside docs/

Do not begin implementation until the repository documentation has been understood.

The documentation is the primary source of truth.

---

# Repository Goal

Build a production-ready AI platform capable of

- Downloading satellite datasets
- Reading NetCDF and HDF5 files
- Extracting Thermal Infrared channels
- Training a Deep Learning frame interpolation model
- Estimating Optical Flow
- Generating intermediate satellite frames
- Preserving metadata
- Computing evaluation metrics
- Exporting NetCDF outputs
- Serving a modern web dashboard
- Deploying the complete application

---

# Required Technology Stack

## Backend

Python 3.11+

FastAPI

PyTorch

OpenCV

NumPy

xarray

netCDF4

h5py

Pydantic

Uvicorn

---

## Frontend

Next.js

React

TypeScript

TailwindCSS

shadcn/ui

Framer Motion

React Three Fiber

Three.js

Recharts

---

## Deployment

Docker

Docker Compose

Vercel

Linux GPU Server

GitHub Actions

---

# Code Quality

Python

Follow

PEP-8

Use

Type Hints

Docstrings

Reusable Functions

Small Modules

Avoid Global Variables

Avoid Duplicate Code

Never hardcode values that belong in configuration files.

---

TypeScript

Use

Strict Mode

Reusable Components

Functional Components

Hooks

Readable Names

ESLint

Prettier

Modular Architecture

---

# Scientific Data Rules

Support

GOES-19

INSAT-3DS

INSAT-3DR

Himawari-8

Supported formats

NetCDF

HDF5

Preserve

Projection

Latitude

Longitude

Timestamp

Units

Channel Information

Satellite Metadata

Never overwrite original datasets.

Never modify scientific metadata unless explicitly required.

---

# AI Model Development

Support

Training

Validation

Evaluation

Inference

Checkpointing

Resume Training

Mixed Precision

GPU Acceleration

Never fake evaluation metrics.

Never generate synthetic benchmark numbers.

Metrics shall always be computed from actual model outputs.

---

# Optical Flow

Generate

Dense Optical Flow

Motion Vectors

Occlusion Masks

Flow Visualization

Validate motion before frame interpolation.

---

# Frame Interpolation

Support

Intermediate Frame Generation

Ground Truth Comparison

Multiple Candidate Models

Model Benchmarking

Metadata Preservation

NetCDF Reconstruction

Choose the final model based on measured evaluation results.

---

# Backend Requirements

Framework

FastAPI

Implement

REST APIs

Background Tasks

Async Processing

Swagger Documentation

Validation

Logging

Error Handling

Standard JSON Responses

---

# Frontend Requirements

Framework

Next.js

Create

Responsive Layout

Modern Dashboard

Scientific Visualization

Interactive Charts

3D Earth

Smooth Animations

Timeline Player

Frame Comparison

Download Center

Support both light and dark themes if practical.

---

# Dashboard Requirements

Display

Original Frames

Generated Frames

Ground Truth

Difference Maps

Heatmaps

Optical Flow

Evaluation Metrics

Playback Timeline

Progress Indicators

Downloads

The dashboard shall obtain all data from backend APIs and generated outputs.

---

# Testing Requirements

Every module shall include

Unit Tests

Integration Tests

Validation Tests

Run tests before marking any task complete.

Do not ignore failing tests.

---

# Logging

Generate logs for

Dataset Download

Preprocessing

Training

Evaluation

Inference

Deployment

API Requests

Dashboard Events

Include

Timestamp

Module

Action

Duration

Warnings

Errors

Status

---

# Error Handling

Never suppress exceptions.

Generate meaningful error messages.

Log failures.

Recover automatically where possible.

Stop execution if a critical validation step fails.

---

# Git Workflow

Use meaningful commits.

Examples

feat: implement preprocessing pipeline

feat: add optical flow estimation

fix: preserve NetCDF metadata

docs: update dashboard specification

Push completed work regularly.

Keep commits focused and descriptive.

---

# Security

Never hardcode

Passwords

Secrets

API Keys

Tokens

Dataset credentials

Use environment variables.

Validate every uploaded file.

Reject unsupported file formats.

Protect configuration values.

---

# Performance

Optimize

GPU Memory

CPU Usage

Batch Processing

Dataset Loading

Caching

Inference Speed

Frontend Rendering

Avoid unnecessary recomputation.

---

# Documentation

Whenever code changes

Update documentation.

Every module shall include

Purpose

Inputs

Outputs

Dependencies

Configuration

Workflow

Example Usage

Notes

Limitations

Keep documentation synchronized with implementation.

---

# AI Agent Responsibilities

The AI assistant shall

Read documentation first.

Understand dependencies.

Implement incrementally.

Validate every module.

Generate tests.

Generate logs.

Generate reports.

Update PROJECT_STATUS.md.

Maintain repository architecture.

Keep code production-ready.

---

# Forbidden Actions

Never

Invent evaluation metrics

Generate placeholder implementations

Leave TODO comments

Delete documentation

Modify repository architecture without reason

Overwrite raw datasets

Skip validation

Skip testing

Skip documentation updates

Hardcode secrets

Proceed after a critical validation failure

---

# Definition of Done

A module is complete only when

✓ Code implemented

✓ Tests passed

✓ Validation successful

✓ Documentation updated

✓ Logs generated

✓ Reports generated (if applicable)

✓ PROJECT_STATUS.md updated

Only after all conditions are satisfied may implementation continue.

---

# Repository Completion

The repository is considered complete only when

- Every documented module has been implemented.
- AI models have been trained or fine-tuned.
- Intermediate satellite frames are generated.
- Scientific metadata is preserved.
- Evaluation metrics are computed from actual outputs.
- Dashboard is fully functional.
- Frontend is deployed.
- Backend is operational.
- GitHub repository is up to date.
- PROJECT_STATUS.md reports 100% completion.

END OF FILE
