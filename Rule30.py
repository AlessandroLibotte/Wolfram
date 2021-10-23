import numpy as np
import cv2
import time
import random


def xor(a, b):
    return (a and (not b)) or ((not a) and b)


class Rule30:

    def __init__(self):
        self.celNum = 500
        self.screen = np.zeros((self.celNum*10, self.celNum*10, 3), np.uint8)
        self.cells = np.zeros(self.celNum, bool)
        random.seed(time.time())
        #self.cells[10] = 1
        #self.cells[250] = 1
        #self.cells[490] = 1
        return

    def random_condition(self):
        for j in range(random.randrange(500)):
            self.cells[random.randrange(500)] = 1

    def update_screen(self, x, y):
        for i in range(10):
            for j in range(10):
                self.screen[(y * 10) + i][(x * 10) + j] = (255, 255, 255)
        return

    def show_screen(self):
        # cv2.imshow("Screen", self.screen)
        return

    def update_state(self, y):
        next_cells = np.zeros(self.celNum, bool)
        for x in range(len(self.cells)-1):
            next_cells[x] = xor(self.cells[x-1], (self.cells[x] or self.cells[x+1]))
            if next_cells[x]:
                self.update_screen(x, y)

        self.cells = next_cells
        return


exe = Rule30()
exe.random_condition()

for i in range(500):
    exe.update_state(i)
    exe.show_screen()

cv2.imwrite("Rule30.jpg", exe.screen)
print("image written")

cv2.waitKey(0)