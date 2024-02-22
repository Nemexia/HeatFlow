import matplotlib.pyplot as plt
import numpy as np

import models
import plotter


model = models.Model()
plot = plotter.plot


plt.imshow(model.mode, cmap='binary')
plt.show()

while True:
    plot(model.temperature)
    model.step()
