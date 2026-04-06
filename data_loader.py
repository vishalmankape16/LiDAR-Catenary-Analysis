import pandas as pd


def load_data(file_path):
    """
    Load LiDAR point cloud from parquet file.

    Returns:
        numpy array of shape (N, 3)
    """
    print(f"Loading data from: {file_path}")
    df = pd.read_parquet(file_path)

    points = df[['x', 'y', 'z']].values
    print(f"Dataset shape: {points.shape}")

    return points