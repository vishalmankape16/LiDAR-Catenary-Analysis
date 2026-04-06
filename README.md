# LiDAR Cable Detection & Catenary Fitting

## Overview
This project processes LiDAR point cloud data to:
- Detect the number of cables
- Group points belonging to each cable
- Fit a catenary curve to model each cable

## Approach

1. Load LiDAR point cloud from parquet file
2. Apply statistical outlier removal
3. Cluster points using DBSCAN to identify wire segments
4. Merge clusters based on slope similarity to reconstruct full wires
5. Fit catenary curves to each wire using nonlinear optimization
6. Visualize results in 3D and 2D projections
7. Save fitted parameters to JSON

## How to Run

```bash
pip install -r requirements.txt
python main.py