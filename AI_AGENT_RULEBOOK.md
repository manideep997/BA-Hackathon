# AI Agent Rulebook

**Project:** Fill in the Frames Seamlessly – Enhancing Temporal Resolution of Satellite Imagery using AI/ML based Optical Flow

Version: 1.0

Status: Mandatory

---

# Purpose

This document defines the mandatory engineering rules that every AI coding agent working inside this repository shall follow.

These rules override assumptions.

Every implementation must comply with this rulebook.

---

# Primary Objective

Develop a production-ready AI-powered satellite frame interpolation system using Deep Learning and Optical Flow.

The final solution must

- Train successfully
- Perform inference successfully
- Generate scientifically meaningful intermediate satellite frames
- Preserve scientific metadata
- Deploy successfully
- Be fully documented
- Be reproducible

---

# Repository Architecture

Never change the repository structure unless absolutely necessary.

Always follow

README.md

↓

PROJECT_STATUS.md

↓

Documentation inside docs/

↓

Implementation

Documentation is the source of truth.

---

# Implementation Workflow

Every feature shall follow

Understand

↓

Plan

↓

Implement

↓

Test

↓

Validate

↓

Document

↓

Commit

↓

Push

↓

Update PROJECT_STATUS.md

↓

Proceed

Never skip validation.

---

# Coding Standards

Python

- PEP-8
- Type hints
- Docstrings
- Modular architecture
- Reusable code
- Clear naming
- Small functions
- Avoid duplicate logic

TypeScript

- Strict typing
- ESLint compliant
- Prettier compatible
- Reusable React components
- Functional components
- Hooks where appropriate

---

# Documentation Rules

Whenever code changes

Update documentation.

Every module shall contain

Purpose

Inputs

Outputs

Dependencies

Workflow

Configuration

Example Usage

Notes

Limitations

---

# Dataset Rules

Support

GOES-19

INSAT-3DS

INSAT-3DR

Himawari-8

Supported formats

NetCDF

HDF5

Never modify

Original datasets

Metadata

Projection

Latitude

Longitude

Units

Timestamps

Always preserve scientific metadata.

---

# AI Model Rules

Never

Fake metrics

Invent benchmark values

Use placeholder checkpoints

Skip validation

Every model shall

Train

Validate

Evaluate

Export checkpoint

Generate reports

Store logs

---

# Optical Flow Rules

Estimate dense optical flow.

Support

RAFT

GMFlow

or another documented model.

Generate

Flow tensors

Flow visualization

Occlusion masks

Validate outputs before frame interpolation.

---

# Frame Interpolation Rules

Evaluate multiple candidate models.

Choose the final model based on measured evaluation results.

Support

Intermediate frame generation

Ground truth comparison

NetCDF reconstruction

Metadata preservation

---

# Backend Rules

Framework

FastAPI

Every endpoint shall

Validate input

Return meaningful responses

Generate logs

Handle exceptions

Support async processing

Provide OpenAPI documentation

---

# Frontend Rules

Framework

Next.js

TypeScript

TailwindCSS

shadcn/ui

Requirements

Responsive

Accessible

Modern

Smooth

NASA/ISRO-inspired design language (original implementation)

Use

Three.js

Framer Motion

Recharts

---

# Dashboard Rules

Dashboard shall

Display

Original frames

Generated frames

Ground truth

Difference maps

Heatmaps

Evaluation metrics

Playback timeline

Interactive charts

Downloads

Never freeze during inference.

---

# Logging Rules

Every module shall generate logs.

Include

Timestamp

Module

Action

Execution Time

Warnings

Errors

Status

Store logs under

logs/

---

# Error Handling

Never suppress exceptions.

Every exception shall

Be logged

Contain meaningful diagnostics

Provide recovery when possible

Critical failures shall stop the current task and be reported.

---

# Testing Rules

Every module requires

Unit tests

Integration tests

Validation tests

Run tests before marking the task complete.

---

# Deployment Rules

Frontend

Deploy to Vercel

Backend

Deploy using FastAPI

Support Docker

Support Docker Compose

Verify deployment after completion.

---

# Git Rules

Use meaningful commit messages.

Examples

feat: implement preprocessing pipeline

feat: add RIFE inference

fix: preserve NetCDF metadata

docs: update dashboard guide

Push progress regularly.

---

# Security Rules

Never hardcode

Secrets

Passwords

API Keys

Tokens

Use

Environment Variables

Validate uploads.

Reject unsupported formats.

---

# Performance Rules

Optimize

GPU memory

CPU usage

Inference speed

Dataset loading

Caching

Batch processing

Avoid unnecessary recomputation.

---

# Validation Gate

Before moving to the next module verify

✓ Code implemented

✓ Tests passed

✓ Documentation updated

✓ Logs generated

✓ Validation passed

✓ PROJECT_STATUS.md updated

If any check fails,

do not proceed.

---

# AI Agent Responsibilities

The AI Agent shall

Read documentation first

Implement incrementally

Maintain repository architecture

Write production-quality code

Generate tests

Generate reports

Generate logs

Update documentation

Commit changes

Push changes

Update PROJECT_STATUS.md

Maintain reproducibility

---

# Forbidden Actions

Never

Delete documentation

Overwrite raw datasets

Invent evaluation metrics

Skip testing

Skip validation

Leave TODO comments

Leave placeholder implementations

Break repository structure

Hardcode configuration

Modify scientific metadata without reason

---

# Definition of Done

A task is complete only when

✓ Code implemented

✓ Validation passed

✓ Tests passed

✓ Documentation updated

✓ Logs generated

✓ Reports generated (where applicable)

✓ Git committed

✓ PROJECT_STATUS.md updated

Only then may the AI proceed to the next task.

---

END OF RULEBOOK
