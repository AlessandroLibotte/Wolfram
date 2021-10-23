import numpy as np
import cv2
import time
import random


class Conway:
    def __init__(self):
        self.timer = 0
        self.totCells = 100
        self.scale = 5
        self.screen = np.zeros((self.totCells*self.scale, self.totCells*self.scale, 3), np.uint8)
        self.cells = np.zeros((self.totCells, self.totCells, 2), int)
        self.random_start(1000)

    def start(self):
        while True:
            self.run()

    def run(self):
        self.clear_screen()
        # self..draw_grid()
        self.print_cells()
        self.count_neigh()
        self.update_state()
        print_timer()
        cv2.imshow("screen", self.screen)
        cv2.waitKey(200)
        self.timer += 200

    def random_start(self, cellnum):
        random.seed(time.time())
        for i in range(cellnum):
            self.cells[random.randint(0, self.totCells-1)][random.randint(0, self.totCells-1)][0] = 1

    def draw_grid(self):
        for i in range(self.totCells):
            cv2.line(self.screen, (i * self.scale, 0), (i * self.scale, self.totCells * self.scale), (100, 100, 100))
        for i in range(self.totCells):
            cv2.line(self.screen, (0, i * self.scale), (self.totCells * self.scale, i * self.scale), (100, 100, 100))

    def print_cells(self):
        for y in range(self.totCells):
            for x in range(self.totCells):
                if self.cells[x][y][0]:
                    self.screen[x*self.scale:(x+1)*self.scale, y*self.scale:(y+1)*self.scale] = (255, 255, 255)

    def clear_screen(self):
        self.screen = np.zeros((self.totCells*self.scale, self.totCells*self.scale, 3), np.uint8)

    def print_neigh(self, x, y):
        if self.cells[x][y][1] > 0 or self.cells[x][y][0]:
            cv2.putText(self.screen, str(self.cells[x][y][1]), (y * self.scale, ((x + 1) * self.scale) - 1), cv2.FONT_HERSHEY_SIMPLEX,
                        0.4, (0, 0, 255), 1)

    def count_neigh(self):
        for y in range(self.totCells):
            for x in range(self.totCells):
                counter = 0
                for j in range(3):
                    if (y-1)+j < 0 or (y-1)+j > self.totCells-1:
                        continue
                    for g in range(3):
                        if (x-1)+g < 0 or (x-1)+g > self.totCells-1:
                            continue
                        if (y-1)+j == y and (x-1)+g == x:
                            continue
                        elif self.cells[(x-1)+g][(y-1)+j][0]:
                            counter += 1
                self.cells[x][y][1] = counter

    def update_state(self):
        for y in range(self.totCells):
            for x in range(self.totCells):
                if self.cells[x][y][0]:
                    if self.cells[x][y][1] < 2 or self.cells[x][y][1] > 3:
                        self.cells[x][y][0] = 0
                elif self.cells[x][y][1] == 3 and self.cells[x][y][0] == 0:
                    self.cells[x][y][0] = 1


t_start = time.time()
m = h = 0


def print_timer():
    global t_start, m, h
    s = int(time.time() - t_start)
    if s > 59:
        m += 1
        t_start = time.time()
    if m > 59:
        h += 1
    cv2.putText(con.screen, str(h) + ":" + str(m) + ":" + str(s), (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


con = Conway()
con.start()
