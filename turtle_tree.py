from turtle import *

def tree(n):
    if n <= 1:
        forward(5)
    else:
        forward(5 * (1.1 ** n))

        # 現在位置を記録
        xx = pos()
        h = heading()

        # ツリーを書く
        left(30)
        tree(n - 2)
        up()

        # 原点に戻って書く
        setpos(xx)
        setheading(h)
        down()
        right(15)
        tree(n - 1)

        # 戻る
        up()
        setpos(xx)
        setheading(h)
        down()

# 描画速度を高速化
speed(0)

# 大きさ12
tree(12)
