
from features import extract_features
from model import predict_runtime
from predictor import analyze_query


def main():
    print("=" * 45)
    print("       SQL QUERY COST PREDICTOR")
    print("=" * 45)

    sql = input("\nEnter your SQL query: ").strip()

    if not sql:
        print("Error: Please enter a SQL query.")
        return

    try:
        features = extract_features(sql)
        analysis = analyze_query(sql)
        runtime = predict_runtime(sql)

        print("\n--- Query Analysis ---")
        print("Risk level:", analysis["risk"])
        print("Risk score:", analysis["risk_score"])
        print("Predicted runtime:", round(runtime, 3), "seconds")

        print("\n--- Query Features ---")
        for name, value in features.items():
            print(f"{name}: {value}")

        print("\n--- Recommendations ---")
        if analysis["hints"]:
            for hint in analysis["hints"]:
                print("-", hint)
        else:
            print("No basic risk patterns detected.")

    except FileNotFoundError:
        print("Error: model.pkl not found. Train the model first.")
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
