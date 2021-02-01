import numpy as np
import cv2
import time
import random

class Rule90:

    def __init__(self):
        self.celNum = 100
        self.screen = np.zeros((1000, 1000, 3), np.uint8)
        self.cells = np.zeros(self.celNum, bool)
        random.seed(time.time())
        self.cells[10] = 1

        return

    def random_condition(self):
        for j in range(random.randrange(500)):
            self.cells[random.randrange(500)] = 1

    def update_screen(self, x, y):
        self.screen[x*10:(x+1)*10][y*10:(y+1)*10] = (255, 255, 255)
        return

    def show_screen(self):
        cv2.imshow("Screen", self.screen)
        return

    def update_state(self, y):
        next_cells = np.zeros(self.celNum, bool)
        for x in range(len(self.cells)-1):
            next_cells[x] = ((self.cells[x+1] or not self.cells[x]) and (self.cells[x+1] or self.cells[x]))
            if next_cells[x]:
                self.update_screen(y, x)

        self.cells = next_cells
        return


exe = Rule90()

#exe.random_condition()

for i in range(100):
    exe.update_state(i)
    exe.show_screen()

cv2.waitKey(0)