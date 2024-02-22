import matplotlib.pyplot as plt
import numpy as np

import models

model = models.Model()
model.plot_mode()

while True:
    if model.steps %10 == 0:
        model.plot_temp(0.1)
    model.step(0.1)
