# Music Recommender MLOps

A production-oriented music recommendation system built to demonstrate ML engineering and MLOps skills.

## Overview

This project simulates a real-world batch recommendation pipeline:

- ingest listening-history interaction data
- clean and validate raw events
- train recommendation models
- evaluate offline metrics
- serve recommendations via API
- simulate batch retraining with new incoming data

The goal is to showcase practical skills in:

- recommender systems
- data engineering
- software engineering
- MLOps and CI/CD

## Current Features

### Data Loading Pipeline

- loads listening-history CSV/TSV files
- standardizes schema
- converts timestamps to datetime
- drops invalid rows
- creates stable `track_id`

### Engineering Tooling

- unit tests with pytest
- linting and formatting with Ruff
- static type checking with mypy
- pre-commit hooks

## Tech Stack

- Python
- pandas / NumPy
- scikit-learn
- implicit
- FastAPI
- MLflow
- Optuna
- Docker
- GitHub Actions

## Roadmap

- [x] project initialization
- [x] data-loading pipeline
- [ ] popularity baseline recommender
- [ ] collaborative filtering model
- [ ] offline evaluation metrics
- [ ] FastAPI serving endpoint
- [ ] MLflow experiment tracking
- [ ] Optuna hyperparameter tuning
- [ ] batch retraining simulation
- [ ] Dockerized deployment
- [ ] CI/CD pipeline

## Running locally

```bash
pip install -e ".[dev]"
pytest
mypy src
ruff check .
```

## Why this project?

This repository is designed as a portfolio project to demonstrate transferable ML engineering skills through a realistic end-to-end recommendation system.
