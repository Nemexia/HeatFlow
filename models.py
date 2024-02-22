import numpy as np
import matplotlib.pyplot as plt


class Model:
    def __init__(self, space_size:tuple[int] = (20, 20)) -> None:
        self.space_size:tuple[int] = space_size
        
        # temperature definition
        self.temperature:np.ndarray = np.ones(self.space_size) * 500
        self.temperature[0, :] = 1000
        self.temperature[self.space_size[0] - 1, :] = 0
        
        # mode definition
        # 0:conductor  -1:insulator  1:constant
        self.mode:np.ndarray = np.zeros(self.space_size)

        self.mode[0, :] = 1
        self.mode[self.space_size[0] - 1, :] = 1

        self.mode[1:-1, 0] = -1
        self.mode[1:-1, self.space_size[1] - 1] = -1
    
    def step(self) -> None:
        next_temp:np.ndarray = np.copy(self.temperature)
        for x, r in enumerate(self.temperature):
            for y, t in enumerate(r):
                if self.mode[x, y] == 0:  # if conductor
                    total:int = 0
                    count:int = 1
                    for i in range(x - 1, x + 2):
                        for j in range(y - 1, y + 2):
                            if self.mode[i, j] != -1:  # if not insulator
                                total += self.temperature[i, j]
                                count += 1
                    next_temp[x, y] = total / count
        self.temperature = next_temp
        
    def plot_temp(self) -> None:
        # temp = self.temperature[1:-1, 1:-1]
        temp = self.temperature
        plt.figure(1)
        plt.clf()
        num = int((temp.max() - temp.min()) / 10) if int((temp.max() - temp.min()) / 10) < 10 else 10
        plt.imshow(temp, cmap='plasma')
        plt.colorbar()
        plt.contour(temp, levels=num, colors=['black'], linewidths=0.5)
        plt.pause(0.1)
        
    def plot_mode(self) -> None:
        plt.imshow(self.mode, cmap='binary')
        plt.show()
        