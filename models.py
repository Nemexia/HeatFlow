import numpy as np

# material with its temperature
material = np.ones((10, 50)) * 500

material[0, :] = 1000
material[len(material) - 1, :] = 0

# for x, r in enumerate(material):
#     for y, t in enumerate(r):
#         material[x, y] = 25


# 0:conductor  -1:insulator  1:constant
mode = np.zeros(material.shape)

mode[0, :] = 1
mode[len(mode) - 1, :] = 1

mode[1:-1, 0] = -1
mode[1:-1, len(mode[0]) - 1] = -1
