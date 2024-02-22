import matplotlib.pyplot as plt
import numpy as np


def plot(space: np.ndarray) -> None:
    """Plot Space as heatmap"""
    space = space[1:-1, 1:-1]
    plt.figure(1)
    plt.clf()
    num = int((space.max() - space.min()) / 10) if int((space.max() - space.min()) / 10) < 10 else 10
    plt.imshow(space, cmap='plasma')
    plt.colorbar()
    plt.contour(space, levels=num, colors=['black'], linewidths=0.5)
    plt.pause(0.1)
