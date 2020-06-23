x = 3
rnew = x

for i in range(4):
    r1 = rnew
    r2 = x / r1
    rnew = (r1 + r2) / 2
    print(r1, rnew, r2)
