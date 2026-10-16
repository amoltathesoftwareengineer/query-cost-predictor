
import re


def analyze_query(sql):
    """Analyze a SQL query and return a basic rule-based risk report."""

    if not isinstance(sql, str) or not sql.strip():
        raise ValueError("SQL query cannot be empty.")

    query = re.sub(r"/\*.*?\*/|--[^\n]*", " ", sql, flags=re.S)
    query = query.lower()

    score = 0
    hints = []

    if re.search(r"\bselect\s+\*", query):
        score += 2
        hints.append("Avoid SELECT *; select only the columns you need.")

    if not re.search(r"\bwhere\b", query) and re.search(r"\bselect\b", query):
        score += 2
        hints.append("Consider whether a WHERE filter is needed.")

    joins = len(re.findall(r"\bjoin\b", query))
    if joins >= 3:
        score += 2
        hints.append("Review multiple JOINs and check the execution plan.")

    if re.search(r"\bcross\s+join\b", query):
        score += 3
        hints.append("Review CROSS JOIN; it can produce many rows.")

    if re.search(r"\border\s+by\b", query):
        score += 1
        hints.append("ORDER BY may require sorting.")

    if score >= 4:
        risk = "HIGH"
    elif score >= 2:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "risk": risk,
        "risk_score": score,
        "hints": hints,
    }


if __name__ == "__main__":
    sample_sql = "SELECT * FROM orders"
    print(analyze_query(sample_sql))
