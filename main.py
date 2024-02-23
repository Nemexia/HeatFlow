import matplotlib.pyplot as plt
import numpy as np

import models

model = models.Model()
# model.plot_mode()
# model.plot_conductivity()
# model.plot_capacity()

while True:
    if model.steps %20 == 0:
        model.plot_temp(0.1)
        # model.plot_energy()
    model.step(0.1)
