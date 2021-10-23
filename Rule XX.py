import numpy as np
import cv2
import time
import random


def xor(a, b):
    return (a and (not b)) or ((not a) and b)


class RuleXX:

    def __init__(self):
        self.celNum = 500
        self.img = np.zeros((self.celNum * 10, self.celNum * 10, 3), np.uint8)
        self.screen = np.zeros((self.celNum * 2, self.celNum * 2, 3), np.uint8)
        self.cells = np.zeros((self.celNum, 2), int)

        self.rules = {
            0: 30,
            1: 45,
            2: 73,
            3: 90,
            4: 106,
            5: 110,
            6: 184
        }

        random.seed(time.time())

        # for i in range(self.celNum):
            # self.cells[i][1] = 110
            # self.cells[i][1] = self.rules[random.randint(0, 6)]

        # self.cells[49] = [0, 30]
        # self.cells[50] = [1, 30]
        # self.cells[51] = [0, 30]

        self.cells[249] = [0, 110]
        self.cells[250] = [1, 110]
        self.cells[251] = [0, 110]
        # self.cells[450][0] = 1
        return

    def Rule30(self, x):

        next_cell = [bool, int]

        next_cell[0] = xor(self.cells[x - 1][0], (self.cells[x][0] or self.cells[x + 1][0]))
        next_cell[1] = self.update_rules(x)

        return next_cell

    def Rule45(self, x):

        next_cell = [bool, int]

        if self.cells[x - 1][0] == 1:

            if self.cells[x][0] == 1:

                if self.cells[x + 1][0] == 1:
                    next_cell[0] = 0
                    next_cell[1] = self.update_rules(x)
                else:
                    next_cell[0] = 0
                    next_cell[1] = self.update_rules(x)

            else:

                if self.cells[x + 1][0] == 1:
                    next_cell[0] = 1
                    next_cell[1] = self.update_rules(x)
                else:
                    next_cell[0] = 0
                    next_cell[1] = self.update_rules(x)

        else:

            if self.cells[x][0] == 1:

                if self.cells[x + 1][0] == 1:
                    next_cell[0] = 1
                    next_cell[1] = self.update_rules(x)
                else:
                    next_cell[0] = 1
                    next_cell[1] = self.update_rules(x)

            else:

                if self.cells[x + 1][0] == 1:
                    next_cell[0] = 0
                    next_cell[1] = self.update_rules(x)
                else:
                    next_cell[0] = 1
                    next_cell[1] = self.update_rules(x)

        return next_cell

    def Rule73(self, x):

        next_cell = [bool, int]

        if self.cells[x - 1][0] == 1:

            if self.cells[x][0] == 1:

                if self.cells[x + 1][0] == 1:
                    next_cell[0] = 0
                    next_cell[1] = self.update_rules(x)
                else:
                    next_cell[0] = 1
                    next_cell[1] = self.update_rules(x)

            else:

                if self.cells[x + 1][0] == 1:
                    next_cell[0] = 0
                    next_cell[1] = self.update_rules(x)
                else:
                    next_cell[0] = 0
                    next_cell[1] = self.update_rules(x)

        else:

            if self.cells[x][0] == 1:

                if self.cells[x + 1][0] == 1:
                    next_cell[0] = 1
                    next_cell[1] = self.update_rules(x)
                else:
                    next_cell[0] = 0
                    next_cell[1] = self.update_rules(x)

            else:

                if self.cells[x + 1][0] == 1:
                    next_cell[0] = 0
                    next_cell[1] = self.update_rules(x)
                else:
                    next_cell[0] = 1
                    next_cell[1] = self.update_rules(x)

        return next_cell

    def Rule90(self, x):

        next_cell = [bool, int]

        next_cell[0] = xor(self.cells[x - 1][0], self.cells[x + 1][0])
        next_cell[1] = self.update_rules(x)

        return next_cell

    def Rule106(self, x):

        next_cell = [bool, int]

        if self.cells[x - 1][0] == 1:

            if self.cells[x][0] == 1:

                if self.cells[x + 1][0] == 1:
                    next_cell[0] = 0
                    next_cell[1] = self.update_rules(x)
                else:
                    next_cell[0] = 1
                    next_cell[1] = self.update_rules(x)


            else:

                if self.cells[x + 1][0] == 1:
                    next_cell[0] = 1
                    next_cell[1] = self.update_rules(x)
                else:
                    next_cell[0] = 0
                    next_cell[1] = self.update_rules(x)

        else:

            if self.cells[x][0] == 1:

                if self.cells[x + 1][0] == 1:
                    next_cell[0] = 1
                    next_cell[1] = self.update_rules(x)
                else:
                    next_cell[0] = 0
                    next_cell[1] = self.update_rules(x)

            else:

                if self.cells[x + 1][0] == 1:
                    next_cell[0] = 1
                    next_cell[1] = self.update_rules(x)
                else:
                    next_cell[0] = 0
                    next_cell[1] = self.update_rules(x)

        return next_cell

    def Rule110(self, x):

        next_cell = [bool, int]

        if self.cells[x][0]:
            next_cell[0] = not (self.cells[x - 1][0] and self.cells[x + 1][0])
            next_cell[1] = self.update_rules(x)
        else:
            next_cell[0] = self.cells[x + 1][0]
            next_cell[1] = self.update_rules(x)

        return next_cell

    def Rule184(self, x):

        next_cell = [bool, int]

        if self.cells[x][0] == 0:
            next_cell[0] = self.cells[x + 1][0]
            next_cell[1] = self.update_rules(x)
        else:
            next_cell[0] = self.cells[x - 1][0]
            next_cell[1] = self.update_rules(x)

        return next_cell

    def random_condition(self):
        for j in range(random.randrange(500)):
            self.cells[random.randrange(500)] = [1, 30]

    def update_screen(self, x, y):

        for i in range(10):
            for j in range(10):
                self.img[(y * 10) + i][(x * 10) + j] = (255, 255, 255)

        for i in range(2):
            for j in range(2):
                self.screen[(y * 2) + i][(x * 2) + j] = (255, 255, 255)

        return

    def show_screen(self):
        cv2.imshow("Screen", self.screen)
        return

    def update_rules(self, x):

        if self.cells[x - 1][1] == 0 or self.cells[x + 1][1] == 0:
            return self.cells[x][1]
        else:
            if self.cells[x - 1][1] == self.cells[x][1] == self.cells[x + 1][1]:
                # print("Same rule")
                # print(x, self.cells[x - 1][1], self.cells[x][1], self.cells[x + 1][1])
                return self.cells[x][1]
            elif self.cells[x - 1][1] != self.cells[x][1] == self.cells[x + 1][1]:
                # print("previous rule")
                # print(x, self.cells[x - 1][1], self.cells[x][1], self.cells[x + 1][1])
                # cv2.waitKey(0)
                return self.cells[x - 1][1]
            elif self.cells[x - 1][1] == self.cells[x][1] != self.cells[x + 1][1]:
                # print("next rule")
                # print(x, self.cells[x - 1][1], self.cells[x][1], self.cells[x + 1][1])
                # cv2.waitKey(0)
                return self.cells[x + 1][1]
            else:
                # print("Random rule")
                # print(x, self.cells[x - 1][1], self.cells[x][1], self.cells[x + 1][1])
                # cv2.waitKey(0)
                return self.rules[random.randint(0, 6)]

        return

    def update_state(self, y):

        sort_rule = {
            0: self.Rule30,
            30: self.Rule30,
            45: self.Rule45,
            73: self.Rule73,
            90: self.Rule90,
            106: self.Rule106,
            110: self.Rule110,
            184: self.Rule184
        }

        next_cells = np.zeros((self.celNum, 2), int)

        # for i in range(self.celNum):
            # next_cells[i][1] = 30

        for x in range(10, len(self.cells)-10):
            # print(x, self.cells[x][1])
            next_cells[x] = sort_rule[self.cells[x][1]](x)

            if next_cells[x][0] == 1:
                self.update_screen(x, y)

        self.cells = next_cells

        return


exe = RuleXX()
# exe.random_condition()

for y in range(500):
    exe.update_state(y)
    exe.show_screen()
    cv2.waitKey(100)

cv2.imwrite("Rule110 but is Rule 30.jpg", exe.screen)
print("image written")

cv2.waitKey(0)
