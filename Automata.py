import numpy as np
import cv2
import time
import random
import math


class Automata:
    def __init__(self):
        self.screen_height = 1920
        self.screen_width = 1080
        self.screen = np.zeros((self.screen_width, self.screen_height, 3), np.uint8)
        self.cell_types = [
                [  # cell type Alpha
                    (0, 0, 255),  # RED
                    2  # Force
                ],
                [  # cell type Beta
                    (0, 255, 0),  # GREEN
                    3  # Force
                ],
                [  # cell type Gamma
                    (255, 0, 0),  # BLUE
                    2  # Force
                ],
                [  # cell type Delta
                    (0, 255, 255),  # YELLOW
                    5
                ]
            ]
        self.cell_num = 500
        # self.cells = [[[250, 250], 0, [0, 0]], [[200, 200], 1, [0, 0]]]
        self.cells = []
        self.create_cells()

    def create_cells(self):
        random.seed(time.time())
        for i in range(self.cell_num):
            self.cells += [
                [
                    [random.randrange(0, self.screen_height), random.randrange(0, self.screen_width)],  # position x, y
                    random.randrange(0, 4),  # cell type
                    [0, 0]  # force vector x, y
                ],
            ]

    def clear_screen(self):
        self.screen[:] = (0, 0, 0)

    def draw_cells(self):
        for cell in range(self.cell_num):
            cv2.circle(self.screen, tuple([int(self.cells[cell][0][0]), int(self.cells[cell][0][1])]), 5, self.cell_types[self.cells[cell][1]][0], -1)

    def draw_vectors(self):
        for cell in range(self.cell_num):
            cv2.line(self.screen, tuple([int(self.cells[cell][0][0]), int(self.cells[cell][0][1])]), tuple([int(self.cells[cell][2][0] + self.cells[cell][0][0]), int(self.cells[cell][2][1] + self.cells[cell][0][1])]), (255, 0, 255), 1)

    def update_cells_vectors(self):
        for cell in range(self.cell_num):
            self.cells[cell][2] = [0, 0]

        for cell in range(self.cell_num):  # go trough all the cells
            for i in range(self.cell_num):  # go trough the other cells
                if i == cell:  # skips itself
                    continue
                if self.cells[i][0][0] - self.cells[cell][0][0] == 0:  # if the vector is vertical
                    if self.cells[i][0][1] - self.cells[cell][0][1] > 0:  # if the vector goes up
                        arg = 1.5708
                    elif self.cells[i][0][1] - self.cells[cell][0][1] < 0:  # else if the vector goes down
                        arg = 4.71239
                else:
                    arg = math.atan2(self.cells[i][0][1] - self.cells[cell][0][1], self.cells[i][0][0] - self.cells[cell][0][0])  # calculate the force vector argument

                dx = self.cells[cell][0][0] - self.cells[i][0][0]
                dy = self.cells[cell][0][1] - self.cells[i][0][1]
                distance = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))

                if distance == 0:
                    distance = 1

                #print(cell, arg)
                if self.cells[cell][1] == 0:  # if the cell in a Alpha cell
                    if self.cells[i][1] == 2:  # if there's a Gamma cell
                        self.cells[i][2][0] += (-7 / (distance / 2)) * math.cos(arg)  # calculate the force vector x coordinate
                        self.cells[i][2][1] += (-7 / (distance / 2)) * math.sin(arg)  # calculate the force vector y coordinate
                    if self.cells[i][1] == 1:  # if there's a Beta cell
                        self.cells[i][2][0] += (3 / (distance / 2)) * math.cos(arg)  # calculate the force vector x coordinate
                        self.cells[i][2][1] += (3 / (distance / 2)) * math.sin(arg)  # calculate the force vector y coordinate
                    if self.cells[i][1] == 0:  # if there's a Alpha cell
                        self.cells[i][2][0] += (10 / (distance / 2)) * math.cos(arg)  # calculate the force vector x coordinate
                        self.cells[i][2][1] += (10 / (distance / 2)) * math.sin(arg)  # calculate the force vector y coordinate

                if self.cells[cell][1] == 1:  # if the cell in a Beta cell
                    if self.cells[i][1] == 0:  # if there's a Alpha cell
                        self.cells[i][2][0] += (-5 / (distance / 2)) * math.cos(arg)  # calculate the force vector x coordinate
                        self.cells[i][2][1] += (-5 / (distance / 2)) * math.sin(arg)  # calculate the force vector y coordinate
                    if self.cells[i][1] == 2:  # if there's a Gamma cell
                        self.cells[i][2][0] += (6 / (distance / 2)) * math.cos(arg)  # calculate the force vector x coordinate
                        self.cells[i][2][1] += (6 / (distance / 2)) * math.sin(arg)  # calculate the force vector y coordinate
                    if self.cells[i][1] == 1:  # if there's a Beta cell
                        self.cells[i][2][0] += (2 / (distance / 2)) * math.cos(arg)  # calculate the force vector x coordinate
                        self.cells[i][2][1] += (2 / (distance / 2)) * math.sin(arg)  # calculate the force vector y coordinate

                if self.cells[cell][1] == 2:  # if the cell is a Gamma cell
                    if self.cells[i][1] == 0:  # if there's a Alpha cell
                        self.cells[i][2][0] += (8 / (distance / 2)) * math.cos(arg)  # calculate the force vector x coordinate
                        self.cells[i][2][1] += (8 / (distance / 2)) * math.sin(arg)  # calculate the force vector y coordinate
                    if self.cells[i][1] == 1:  # if there's a Beta cell
                        self.cells[i][2][0] += (-3 / (distance / 2)) * math.cos(arg)  # calculate the force vector x coordinate
                        self.cells[i][2][1] += (-3 / (distance / 2)) * math.sin(arg)  # calculate the force vector y coordinate
                    if self.cells[i][1] == 2:  # if there's a Gamma cell
                        self.cells[i][2][0] += (-8 / (distance / 2)) * math.cos(arg)  # calculate the force vector x coordinate
                        self.cells[i][2][1] += (-8 / (distance / 2)) * math.sin(arg)  # calculate the force vector y coordinate

                if self.cells[cell][1] == 3:  # if the cell is a Delta cell
                    if self.cells[i][1] != 3:
                        self.cells[i][2][0] += (-10 / (distance / 2)) * math.cos(arg)  # calculate the force vector x coordinate
                        self.cells[i][2][1] += (-10 / (distance / 2)) * math.sin(arg)  # calculate the force vector y coordinate
                    else:
                        self.cells[i][2][0] += (1 / (distance / 2)) * math.cos(arg)  # calculate the force vector x coordinate
                        self.cells[i][2][1] += (1 / (distance / 2)) * math.sin(arg)  # calculate the force vector y coordinate

    def get_movement(self, cell):
        return math.sqrt(math.pow(self.cells[cell][2][0], 2) + math.pow(self.cells[cell][2][1], 2))

    def check_collision(self, cell):
        for i in range(self.cell_num):
            if i == cell:
                continue
            dx = self.cells[cell][0][0] - self.cells[i][0][0]
            dy = self.cells[cell][0][1] - self.cells[i][0][1]
            distance = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))

            if distance <= 15 + self.get_movement(cell):
                return True
            else:
                return False

    def update_cell_position(self):

        for cell in range(self.cell_num):  # go trough all the cells

            if int(self.cells[cell][2][0]) == 0:  # if the vector is vertical

                if self.cells[cell][2][1] < 0:  # if the vector goes down

                    if not self.check_collision(cell):
                        self.cells[cell][0][1] -= self.get_movement(cell)  # decrement the y coordinate

                elif self.cells[cell][2][1] > 0:  # else if the vector goes up

                    if not self.check_collision(cell):
                        self.cells[cell][0][1] += self.get_movement(cell)  # increment the y coordinate

            elif int(self.cells[cell][2][1]) == 0:  # if the vector is horizontal

                if self.cells[cell][2][0] < 0:  # if the vector goes right

                    if not self.check_collision(cell):
                        self.cells[cell][0][0] -= self.get_movement(cell)  # decrement the y coordinate

                elif self.cells[cell][2][0] > 0:  # else if the vector goes left

                    if not self.check_collision(cell):
                        self.cells[cell][0][0] += self.get_movement(cell)  # increment the y coordinate

            else:  # else if the vector is nor vertical nor horizontal

                m = (self.cells[cell][2][1]) / (self.cells[cell][2][0])  # calculate gradient
                q = (((self.cells[cell][0][0] + self.cells[cell][2][0]) * self.cells[cell][0][1]) -
                     (self.cells[cell][0][0] * (self.cells[cell][0][1] + self.cells[cell][2][1]))) \
                    / self.cells[cell][2][0]  # calculate coefficient

                if 1 >= m >= -1:  # if the gradient is between 1 and -1 change the x coordinate and calculate the next y

                    if self.cells[cell][2][0] > 0:  # if the vector goes to the left

                        if not self.check_collision(cell):
                            self.cells[cell][0][0] += self.get_movement(cell)  # increment the x coordinate
                            self.cells[cell][0][1] = (self.cells[cell][0][0] * m) + q  # then calculate ne next y coordinate
                        else:
                            if self.cells[cell][2][1] > 0:
                                self.cells[cell][0][1] += self.get_movement(cell)  # increment the y coordinate
                            elif self.cells[cell][2][1] < 0:
                                self.cells[cell][0][1] -= self.get_movement(cell)  # decrement the y coordinate

                    elif self.cells[cell][2][0] < 0:  # else if the vector goes to the right

                        if not self.check_collision(cell):
                            self.cells[cell][0][0] -= self.get_movement(cell)  # decrement the x coordinate
                            self.cells[cell][0][1] = (self.cells[cell][0][0] * m) + q  # then calculate ne next y coordinate
                        else:
                            if self.cells[cell][2][1] > 0:
                                self.cells[cell][0][1] += self.get_movement(cell)  # increment the y coordinate
                            elif self.cells[cell][2][1] < 0:
                                self.cells[cell][0][1] -= self.get_movement(cell)  # decrement the y coordinate

                else:  # else change the y coordinate and calculate the next x

                    if self.cells[cell][2][1] > 0:  # if the vector goes up

                        if not self.check_collision(cell):
                            self.cells[cell][0][1] += self.get_movement(cell)  # increment the y coordinate
                            self.cells[cell][0][0] = (self.cells[cell][0][1] - q) / m  # then calculate the next x coordinate
                        else:
                            if self.cells[cell][2][0] > 0:
                                self.cells[cell][0][0] += self.get_movement(cell)  # increment the x coordinate
                            elif self.cells[cell][2][0] < 0:
                                self.cells[cell][0][0] -= self.get_movement(cell)  # decrement the x coordinate

                    elif self.cells[cell][2][1] < 0:  # else if the vector goes down

                        if not self.check_collision(cell):
                            self.cells[cell][0][1] -= self.get_movement(cell)  # decrement the y coordinate
                            self.cells[cell][0][0] = (self.cells[cell][0][1] - q) / m  # then calculate the next x coordinate
                        else:
                            if self.cells[cell][2][0] > 0:
                                self.cells[cell][0][0] += self.get_movement(cell)  # increment the x coordinate
                            elif self.cells[cell][2][0] < 0:
                                self.cells[cell][0][0] -= self.get_movement(cell)  # decrement the x coordinate

    def check_boundaries(self):
        for cell in range(self.cell_num):
            if self.cells[cell][0][0] < 5:
                self.cells[cell][0][0] = 5
            if self.cells[cell][0][0] > self.screen_height-5:
                self.cells[cell][0][0] = self.screen_height-5

            if self.cells[cell][0][1] < 5:
                self.cells[cell][0][1] = 5
            if self.cells[cell][0][1] > self.screen_width-5:
                self.cells[cell][0][1] = self.screen_width-5


exe = Automata()

while True:
    exe.clear_screen()
    exe.draw_cells()
    exe.update_cells_vectors()
    # exe.draw_vectors()
    exe.update_cell_position()
    exe.check_boundaries()

    cv2.imshow("Screen", exe.screen)
    cv2.waitKey(1)
