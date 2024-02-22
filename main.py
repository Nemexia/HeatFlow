import matplotlib.pyplot as plt
import numpy as np

import models

model = models.Model()

plt.imshow(model.mode, cmap='binary')
plt.show()

while True:
    model.plot_temp()
    model.step()
