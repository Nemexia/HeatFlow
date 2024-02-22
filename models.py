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
    
    def step(self):
        next_temp = np.copy(self.temperature)
        for x, r in enumerate(self.temperature):
            for y, t in enumerate(r):
                if self.mode[x, y] == 0:  # if conductor
                    total = 0
                    count = 1
                    for i in range(x - 1, x + 2):
                        for j in range(y - 1, y + 2):
                            if self.mode[i, j] != -1:  # if not insulator
                                total += self.temperature[i, j]
                                count += 1
                    next_temp[x, y] = total / count
        self.temperature = next_temp
        