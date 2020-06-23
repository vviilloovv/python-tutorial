import math

while True:
    x = input("Input positive integer: 'end' is end: ")

    if(x == "end"):
        print("bye.")
        break

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

    rnew = x
    diff = abs(rnew - x / rnew)
    while(1.0E-6 < diff):
        r1 = rnew
        r2 = x / r1
        rnew = (r1 + r2) / 2
        print(r1, rnew, r2)
        diff = abs(r1 - r2)
    print("----------")
