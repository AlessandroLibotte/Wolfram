import numpy as np
import cv2
import time
import random


class Rule110:

    def __init__(self):
        self.celNum = 500
        self.screen = np.zeros((500, 500, 3), np.uint8)
        self.cells = np.zeros(self.celNum, bool)
        random.seed(time.time())
        #self.cells[10] = 1
        #self.cells[250] = 1
        #self.cells[499] = 1
        return

    def random_condition(self):
        for j in range(random.randrange(500)):
            self.cells[random.randrange(500)] = 1

    def update_screen(self, x, y):
        self.screen[x][y] = (255, 255, 255)
        return

    def show_screen(self):
        cv2.imshow("Screen", self.screen)
        return

    def update_state(self, y):
        next_cells = np.zeros(self.celNum, bool)
        for x in range(len(self.cells)-1):
            if self.cells[x]:
                next_cells[x] = not(self.cells[x-1] and self.cells[x+1])
            else:
                next_cells[x] = self.cells[x+1]

            if next_cells[x]:
                self.update_screen(y, x)

        self.cells = next_cells
        return


exe = Rule110()

exe.random_condition()

for i in range(500):
    exe.update_state(i)
    exe.show_screen()

cv2.waitKey(0)