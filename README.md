# query-cost-predictor

Predict the **runtime** and **cost** of SQL queries *before* you run them. Catch expensive queries early, in development, code review or CI, instead of finding out from the cloud bill.

> ⚠️ Status: early development. Edit the sections below to match what the project actually does.

## Why?

One careless `SELECT *`, a missing filter or an accidental cross join can scan terabytes and cost real money. `query-cost-predictor` estimates how heavy a query will be so you can fix it before it runs.

## Features

- Estimate execution time, rows scanned and compute cost for a SQL query
- Feature extraction from query text (joins, aggregations, subqueries, window functions, `SELECT *`, missing `WHERE`)
- Optional use of `EXPLAIN` plans for more accurate estimates
- ML model trained on your own query history (train, evaluate, predict)
- Cost thresholds: warn or fail when a query is predicted to be too expensive
- Output as console text or JSON
- Works with multiple databases / warehouses (e.g. PostgreSQL, BigQuery, Snowflake)

## Installation

```bash
git clone https://github.com/amoltathesoftwareengineer/query-cost-predictor.git
cd query-cost-predictor
pip install -r requirements.txt
```

## Quick start

```bash
# 1. Train a model on your past query logs
python -m query_cost_predictor train --data query_history.csv --out model.pkl

# 2. Predict the cost of a new query
python -m query_cost_predictor predict --model model.pkl --sql "SELECT * FROM orders o JOIN customers c ON o.customer_id = c.id"
```

Example output:

```
Estimated runtime : 42.7 s
Estimated rows    : 18.4 M
Estimated cost    : $1.85
Risk              : HIGH

Hints:
  - SELECT * reads all columns, select only what you need
  - No WHERE clause on orders, consider filtering by date
```

## Usage

```bash
# Predict from a SQL file
python -m query_cost_predictor predict --model model.pkl --file query.sql

# JSON output
python -m query_cost_predictor predict --model model.pkl --file query.sql --format json

# Fail (non-zero exit) if predicted cost is above a limit
python -m query_cost_predictor predict --model model.pkl --file query.sql --max-cost 5.00

# Evaluate the model
python -m query_cost_predictor evaluate --model model.pkl --data test_queries.csv
```

### As a library

```python
from query_cost_predictor import load_model

model = load_model("model.pkl")
result = model.predict("SELECT user_id, COUNT(*) FROM events GROUP BY user_id")

print(result.runtime_seconds, result.estimated_cost)
```

### Training data format

| column | description |
|---|---|
| `sql` | the query text |
| `runtime_seconds` | actual execution time |
| `bytes_scanned` | data processed (optional) |
| `cost` | actual cost (optional) |

## Project structure

```
query-cost-predictor/
├── query_cost_predictor/   # core package (features, model, CLI)
├── tests/                  # unit tests
├── examples/               # sample queries and training data
├── requirements.txt
└── README.md
```

## Roadmap

- [ ] SQL feature extraction
- [ ] Baseline runtime prediction model
- [ ] `EXPLAIN` plan features
- [ ] Cost estimation per warehouse pricing
- [ ] CLI and JSON output
- [ ] GitHub Action for pull requests

## Contributing

Contributions are welcome.

1. Fork the repo
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit your changes
4. Open a pull request

## License

MIT License. See [LICENSE](https://github.com/amoltathesoftwareengineer/query-cost-predictor/blob/main/LICENSE).

## Author

Amol Tathe · [LinkedIn](https://linkedin.com/in/amoltathesoftwareengineer) · [GitHub](https://github.com/amoltathesoftwareengineer)
