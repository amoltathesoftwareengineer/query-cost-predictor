
import csv
import pickle
from pathlib import Path

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from features import extract_features


def train_model(data_file, model_file="model.pkl"):
    rows = []

    with open(data_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        required = {"sql", "runtime_seconds"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError(
                "CSV must contain sql and runtime_seconds columns."
            )

        for row in reader:
            sql = row["sql"].strip()
            runtime = float(row["runtime_seconds"])

            if not sql or runtime < 0:
                raise ValueError("SQL must not be empty and runtime must be non-negative.")

            rows.append((extract_features(sql), runtime))

    if len(rows) < 5:
        raise ValueError("Please provide at least 5 training examples.")

    feature_names = list(rows[0][0].keys())
    X = [[item[0][name] for name in feature_names] for item in rows]
    y = [item[1] for item in rows]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    with open(model_file, "wb") as file:
        pickle.dump(
            {"model": model, "feature_names": feature_names},
            file,
        )

    return {"model_file": model_file, "mae_seconds": round(mae, 3)}


def predict_runtime(sql, model_file="model.pkl"):
    with open(model_file, "rb") as file:
        saved = pickle.load(file)

    features = extract_features(sql)
    X = [[features[name] for name in saved["feature_names"]]]
    prediction = saved["model"].predict(X)[0]

    return max(0.0, float(prediction))


if __name__ == "__main__":
    print("Runtime prediction model module is ready.")
