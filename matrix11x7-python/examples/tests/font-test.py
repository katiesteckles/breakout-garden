#!/usr/bin/env python

import time

from matrix11x7 import Matrix11x7
from matrix11x7.fonts import font5x7 as font5x7

matrix11x7 = Matrix11x7()

# Avoid retina-searage!
matrix11x7.set_brightness(0.5)

# Uncomment the below if your display is upside down
# (e.g. if you're using it in a Pimoroni Scroll Bot)
# matrix11x7.rotate(degrees=180)

for char in range(len(font5x7.data)):
    matrix11x7.draw_char(char * (3 + font5x7.width), 0, char, font=font5x7)

while True:
    matrix11x7.show()
    matrix11x7.scroll()
    time.sleep(0.1)
