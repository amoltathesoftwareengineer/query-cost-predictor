
import re


def extract_features(sql):
    """Extract basic structural features from a SQL query."""
    query = re.sub(r"/\*.*?\*/|--[^\n]*", " ", sql, flags=re.S)
    query = query.lower()

    return {
        "query_length": len(query),
        "select_star": int(bool(re.search(r"\bselect\s+\*", query))),
        "join_count": len(re.findall(r"\bjoin\b", query)),
        "where_present": int(bool(re.search(r"\bwhere\b", query))),
        "group_by_present": int(bool(re.search(r"\bgroup\s+by\b", query))),
        "order_by_present": int(bool(re.search(r"\border\s+by\b", query))),
        "subquery_count": max(0, query.count("select") - 1),
        "has_aggregation": int(
            bool(re.search(r"\b(count|sum|avg|min|max)\s*\(", query))
        ),
    }


if __name__ == "__main__":
    sample_sql = """
    SELECT *
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    """

    print(extract_features(sample_sql))
