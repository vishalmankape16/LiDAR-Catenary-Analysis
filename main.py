"""
Main pipeline for LiDAR cable detection and catenary fitting.

This version uses robust path handling so it works from any directory.
"""

import os

from data_loader import load_data
from preprocessing import remove_outliers, extract_high_points
from clustering import cluster_wires
from catenary_fit import fit_catenary
from visualization import plot_clusters, plot_catenary
from utils import save_results


def main():
    # ==============================
    # Robust file path (Option 1)
    # ==============================
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "data", "lidar_cable_points_medium.parquet")

    print("Looking for file at:", file_path)
    print("File exists:", os.path.exists(file_path))
    
    # ==============================
    # Load data
    # ==============================
    points = load_data(file_path)

    # ==============================
    # Preprocessing
    # ==============================
    
    points = remove_outliers(points)
    points = extract_high_points(points)
    print("Points after preprocessing:", len(points))
    # ==============================
    # Clustering (detect wires)
    # ==============================
    clusters = cluster_wires(points)

    from clustering import merge_clusters
    clusters = merge_clusters(clusters)

    # ==============================
    # Visualize clusters
    # ==============================
    plot_clusters(clusters)

    # ==============================
    # Fit catenary curves
    # ==============================
    results = []

    for i, cluster in enumerate(clusters):
        params = fit_catenary(cluster)

        # FIXED NumPy truth error
        if params is not None:
            print(f"Wire {i} params: {params}")
            results.append(params)

            # Plot fitted curve
            plot_catenary(cluster, params)

    # ==============================
    # Save results
    # ==============================
    output_path = os.path.join(BASE_DIR, "outputs", "results.json")

    # Ensure outputs folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    save_results(results, output_path)


if __name__ == "__main__":
    main()