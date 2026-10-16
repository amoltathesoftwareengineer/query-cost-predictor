# SQL Query Cost Predictor

A Python-based prototype that analyzes SQL query patterns, identifies potential query risks, and predicts approximate runtime using a machine learning model.

## Overview

The SQL Query Cost Predictor helps developers inspect SQL queries before execution. It combines rule-based risk checks, SQL feature extraction, and a Random Forest regression model trained on sample query data.

**Project status:** Working prototype — predictions are experimental and require validation against real database workloads.

## Features

- Extract basic features from SQL query text.
- Detect potentially risky patterns, such as `SELECT *` and missing `WHERE` clauses.
- Generate rule-based query risk assessments.
- Train a Random Forest model using sample SQL runtime data.
- Predict approximate runtime based on the trained model.
- Provide a simple interactive command-line interface.
- Demonstrate basic illustrative cost-estimation calculations.

## Technology Stack

- Python
- pandas-compatible CSV training data
- scikit-learn
- Random Forest Regression
- SQL pattern analysis

## Repository Structure

```text
query-cost-predictor/
├── cost_estimator.py
├── features.py
├── main.py
├── model.py
├── predictor.py
├── requirements.txt
├── training_data.csv
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/amoltathesoftwareengineer/query-cost-predictor.git
cd query-cost-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python -c "from model import train_model; print(train_model('training_data.csv'))"
```

This trains the model using the included sample dataset and creates a local `model.pkl` file.

### 4. Run the application

```bash
python main.py
```

Enter a SQL query when prompted to see the prototype's analysis.

## Training Data

The included `training_data.csv` file contains sample SQL queries and associated runtime values. The dataset is small and synthetic, intended for development and demonstration.

## Limitations

- Runtime predictions are not validated against production database workloads.
- Risk checks are basic pattern-based heuristics, not a full SQL parser.
- The current prototype does not integrate with a live database or execute `EXPLAIN` plans.
- Cost calculations are illustrative and are not connected to actual cloud billing.
- Support for JSON output, automated CI checks, and multiple database integrations is not yet implemented.

## Future Improvements

- Add SQL parsing and database-specific query-plan analysis.
- Evaluate predictions using larger, real-world datasets.
- Add unit tests and automated testing workflows.
- Implement structured JSON output and CI integration.
- Improve database-specific cost estimation.

## Author

**Amol Tathe**

- GitHub: https://github.com/amoltathesoftwareengineer
- LinkedIn: https://linkedin.com/in/amoltathesoftwareengineer

---

*This project is an educational prototype for SQL analysis and machine learning experimentation.*
