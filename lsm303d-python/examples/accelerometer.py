#!/usr/bin/env python

import time
from lsm303d import LSM303D

lsm = LSM303D(0x1d)  # Change to 0x1e if you have soldered the address jumper

from matrix11x7 import Matrix11x7

matrix11x7 = Matrix11x7()

# Avoid retina-searage!
matrix11x7.set_brightness(0.5)

curvel = [0,0]
curpos = [5,3]
curposint=[5,3]

while True:
    xyz = lsm.accelerometer()
    xin = xyz[0]
    yin = -xyz[1]
    if curposint[0]<=0:
        curposint[0]=0
        xin = max(xin,0)
        curvel[0]=0
    elif curposint[0]>=10:
        curposint[0]=10
        xin = min(xin,0)
        curvel[0]=0
        
    if curposint[1]<=0:
        curposint[1]=0
        yin = max(yin,0)
        curvel[1]=0
    elif curposint[1]>=6:
        curposint[1]=6
        yin = min(yin,0)
        curvel[1]=0
        
    curacc=[xin,yin]
    print(("{:+06.2f}g : {:+06.2f}g : {:+06.2f}g").format(*xyz))
    
    curvel = [curvel[i]+curacc[i] for i in range(2)]
    curpos = [curpos[i]+curvel[i] for i in range(2)]
    curposint = [int(curpos[i]+0.5) for i in range(2)]
    matrix11x7.clear()
    matrix11x7.set_pixel(curposint[0],curposint[1], 0.6)
    matrix11x7.show()

    time.sleep(1.0/20)
