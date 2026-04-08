import matplotlib.pyplot as plt
import numpy as np


def plot_clusters(clusters):
    """
    3D visualization of detected wires.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i, cluster in enumerate(clusters):
        ax.scatter(
            cluster[:, 0],
            cluster[:, 1],
            cluster[:, 2],
            s=5,
            label=f"Wire {i}"
        )

    ax.set_title("Detected Wires")
    ax.legend()
    plt.show()


def plot_catenary(cluster, params):
    """
    Plot fitted curve vs actual points.
    """
    x = cluster[:, 0]
    z = cluster[:, 2]

    a, x0, y0 = params

    x_line = np.linspace(min(x), max(x), 100)
    z_line = a * np.cosh((x_line - x0) / a) + y0

    plt.scatter(x, z, s=5, label="Data")
    plt.plot(x_line, z_line, linewidth=2, label="Fit")

    plt.title("Catenary Fit")
    plt.legend()
    plt.show()