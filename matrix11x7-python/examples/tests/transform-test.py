#!/usr/bin/env python

import time
import argparse

from matrix11x7 import Matrix11x7
from matrix11x7.fonts import font3x5

print("""
Matrix 11x7: Transformation Test

Shows a message with arbitrary transformations specified
on the command line. See --help.

Press Ctrl+C to exit!

""")

matrix11x7 = Matrix11x7()

# Avoid retina-searage!
matrix11x7.set_brightness(0.5)

parser = argparse.ArgumentParser(description='Scroll Hat HD transformation test.')

parser.add_argument('-r', '--rotate', metavar='DEGREES', type=int, help='Rotate the display.', default=0)
parser.add_argument('-x', '--flip-x', help='Flip in the X axis.', action='store_true')
parser.add_argument('-y', '--flip-y', help='Flip in the Y axis.', action='store_true')
parser.add_argument('-s', '--scroll-x', metavar='PIXELS', type=int, help='Scroll in the X axis.', default=0)
parser.add_argument('-t', '--scroll-y', metavar='PIXELS', type=int, help='Scroll in the Y axis.', default=0)
parser.add_argument('-m', '--message', metavar='MESSAGE', type=str, help='Message to display.', default='Does it work? ')

args = parser.parse_args()

matrix11x7.clear()
matrix11x7.write_string(args.message, x=0, y=0, font=font3x5)

while True:
    matrix11x7.flip(args.flip_x, args.flip_y)
    matrix11x7.rotate(args.rotate)
    matrix11x7.scroll(args.scroll_x, args.scroll_y)
    matrix11x7.show()
    time.sleep(0.1)
