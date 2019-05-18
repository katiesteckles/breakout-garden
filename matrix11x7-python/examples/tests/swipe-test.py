#!/usr/bin/env python

import time
from matrix11x7 import Matrix11x7

matrix11x7 = Matrix11x7()

# Avoid retina-searage!
matrix11x7.set_brightness(0.5)

while True:
    for y in range(7):
        for x in range(11):
            matrix11x7.set_pixel(x, y, 1)
        matrix11x7.show()
        time.sleep(0.1)
    time.sleep(0.2)
    for y in range(7):
        for x in range(11):
            matrix11x7.set_pixel(x, 6 - y, 0)
        matrix11x7.show()
        time.sleep(0.1)

    for x in range(11):
        for y in range(7):
            matrix11x7.set_pixel(x, y, 1)
        matrix11x7.show()
        time.sleep(0.1)
    time.sleep(0.2)
    for x in range(11):
        for y in range(7):
            matrix11x7.set_pixel(x, 6 - y, 0)
        matrix11x7.show()
        time.sleep(0.1)
