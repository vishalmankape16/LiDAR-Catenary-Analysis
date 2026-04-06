import numpy as np


def remove_outliers(points, z_thresh=3):
    """
    Simple Z-score filtering to remove noise.
    """
    mean = np.mean(points, axis=0)
    std = np.std(points, axis=0)

    z_scores = (points - mean) / std
    mask = np.abs(z_scores) < z_thresh

    return points[np.all(mask, axis=1)]


def extract_high_points(points):
    """
    Keep top 50% instead of 30% (less aggressive).
    """
    z_threshold = np.percentile(points[:, 2], 50)
    return points[points[:, 2] > z_threshold]