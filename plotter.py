import matplotlib.pyplot as plt
import numpy as np


def plot(space: np.ndarray) -> None:
    """Plot Space as heatmap"""
    plt.imshow(space, cmap='hot')
    plt.colorbar()

    plt.show()
