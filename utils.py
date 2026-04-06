import json


def save_results(results, output_path="outputs/results.json"):
    """
    Save fitted parameters to JSON.
    """
    serializable = [list(map(float, r)) for r in results]

    with open(output_path, "w") as f:
        json.dump(serializable, f, indent=4)

    print(f"Results saved to {output_path}")