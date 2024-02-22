import matplotlib.pyplot as plt
import numpy as np

import models

model = models.Model()
model.plot_mode()

while True:
    model.plot_temp()
    model.step()
