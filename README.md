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

## Design Considerations

1. Modular structure for readability and reuse
2. Simple pipeline for clarity and maintainability
3. Uses standard libraries (NumPy, SciPy, scikit-learn)

## Limitations

1. Some datasets have very small sag, making the catenary appear nearly linear
2. Clustering parameters may require tuning for different datasets
3. Merge logic is heuristic and can be improved

## Future Improvements

1. Fit catenary in a local coordinate system (full 3D plane)
2. Improve cluster merging using geometric constraints
3. Add robust fitting to handle noise
4. Optimize for large-scale datasets

## How to Run

```bash
pip install -r requirements.txt
python main.py
