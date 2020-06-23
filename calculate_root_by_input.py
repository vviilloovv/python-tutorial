import math

def get_positive_numeral():
    "自然数を標準入力"

    while True:
        x = input("Input positive integer: 'end' is end: ")

        if(x == "end"):
            print("bye.")
            return x

        try:
            x = float(x)
        except ValueError:
            print(x, "is not number!")
            continue
        except:
            print("bad error.")
            continue

        if(x <= 0):
            print(x, "is not positive!")
            continue

        return x

def square_root(x):
    "引数xの平方根を求める"

    rnew = x

    diff = abs(rnew - x / rnew)
    while(1.0E-6 < diff):
        r1 = rnew
        r2 = x / r1
        rnew = (r1 + r2) / 2
        print(r1, rnew, r2)
        diff = abs(r1 - r2)

    return rnew

while True:
    x = get_positive_numeral()

    if(x == "end"):
        break

    print(square_root(x))
    print("----------")
