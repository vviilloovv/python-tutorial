from turtle import *
import random

is_stopped = False

def click(x, y):
    global is_stopped
    is_stopped = True

onscreenclick(click)

speed(0)
while(not is_stopped):
    left(random.randint(-90, 90))
    forward(10)

    # 原点から200以上離れたら戻る
    if(position()[0] ** 2 + position()[1] ** 2 > 200 ** 2):
        forward(-10)
