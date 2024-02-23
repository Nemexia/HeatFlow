import models

model = models.Model()
# model.plot_mode()
# model.plot_conductivity()
# model.plot_capacity()

while True:
    if model.steps % 100 == 0:
        model.plot_temp(0.001)
        # model.plot_energy()
    model.step(0.01)
