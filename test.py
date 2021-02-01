import numpy as np
import cv2
import time
import random

a = [0,1,0,1,0,1,0,1]
b = [0,0,1,1,0,0,1,1]
c = [0,0,0,0,1,1,1,1]

for i in range(8):
    d = (a[i] or not b[i]) and ( b[i] or c[i])
    print(int(a[i]), int (b[i]), int(c[i]), int(d))