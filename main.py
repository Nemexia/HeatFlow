import matplotlib.pyplot as plt
import numpy as np

import models
import plotter


def step(space, mode):
    next_space = np.copy(space)
    for x, r in enumerate(space):
        for y, t in enumerate(r):
            if mode[x, y] == 0:  # if conductor
                total = 0
                count = 1
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        if mode[i, j] != -1:  # if not insulator
                            total += space[i, j]
                            count += 1
                next_space[x, y] = total / count
    return next_space


model = models.material
mode = models.mode
plot = plotter.plot


plt.imshow(mode, cmap='binary')
plt.show()

while True:
    plot(model)
    model = step(model, mode)
    # input()
