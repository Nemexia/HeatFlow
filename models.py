import numpy as np

class Model:
    def __init__(self, space_size = (100, 100)) -> None:
        self.space_size = space_size
        
        # temperature definition
        self.temperature = np.ones(self.space_size) * 500
        self.temperature[0, :] = 1000
        self.temperature[self.space_size[0] - 1, :] = 0
        
        
        # mode definition
        # 0:conductor  -1:insulator  1:constant
        self.mode = np.zeros(self.space_size)

        self.mode[0, :] = 1
        self.mode[self.space_size[0] - 1, :] = 1

        self.mode[1:-1, 0] = -1
        self.mode[1:-1, self.space_size[1] - 1] = -1





# for x, r in enumerate(material):
#     for y, t in enumerate(r):
#         material[x, y] = 25




