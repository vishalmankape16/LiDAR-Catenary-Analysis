import numpy as np
from scipy.optimize import curve_fit


def catenary(x, a, x0, y0):
    """
    Catenary function.
    """
    return a * np.cosh((x - x0) / a) + y0


def fit_catenary(points):
    """
    Fit catenary curve to a cluster.
    """
    x = points[:, 0]
    z = points[:, 2]

    try:
        params, _ = curve_fit(catenary, x, z, maxfev=10000)
        return params
    except Exception:
        return None