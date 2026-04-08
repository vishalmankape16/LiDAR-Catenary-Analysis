from sklearn.cluster import DBSCAN
import numpy as np


def cluster_wires(points):
    """
    Cluster LiDAR points into wires.
    """

    print("Running DBSCAN clustering...")

    clustering = DBSCAN(eps=0.5, min_samples=3).fit(points)

    labels = clustering.labels_

    unique_labels = set(labels)
    print("Unique labels:", unique_labels)

    clusters = []

    for label in unique_labels:
        if label == -1:
            continue

        cluster = points[labels == label]

        print(f"Cluster {label} size:", len(cluster))

        if len(cluster) > 50:
            clusters.append(cluster)

    print(f"Detected cables: {len(clusters)}")

    return clusters
import numpy as np


def merge_clusters(clusters):
    """
    Merge clusters that belong to the same wire using slope similarity.
    """

    merged = []
    used = set()

    for i, c1 in enumerate(clusters):
        if i in used:
            continue

        group = [c1]
        used.add(i)

        for j, c2 in enumerate(clusters):
            if j in used:
                continue

            # Compare direction (approx slope)
            slope1 = np.polyfit(c1[:, 0], c1[:, 2], 1)[0]
            slope2 = np.polyfit(c2[:, 0], c2[:, 2], 1)[0]

            if abs(slope1 - slope2) < 0.1:
                group.append(c2)
                used.add(j)

        merged_cluster = np.vstack(group)
        merged.append(merged_cluster)

    print(f"Merged cables: {len(merged)}")

    return merged