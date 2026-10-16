
def estimate_cost(bytes_scanned, cost_per_gb):
    """Estimate processing cost using scanned bytes and a price per GB."""

    if bytes_scanned < 0:
        raise ValueError("Bytes scanned cannot be negative.")

    if cost_per_gb < 0:
        raise ValueError("Cost per GB cannot be negative.")

    bytes_per_gb = 1_000_000_000
    estimated_cost = (bytes_scanned / bytes_per_gb) * cost_per_gb

    return round(estimated_cost, 6)


if __name__ == "__main__":
    # Example: 2 GB scanned at $5 per GB
    bytes_scanned = 2_000_000_000
    cost_per_gb = 5.0

    cost = estimate_cost(bytes_scanned, cost_per_gb)
    print(f"Estimated processing cost: ${cost:.2f}")
