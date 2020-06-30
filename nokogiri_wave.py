import tkinter as tk
import tkinter.filedialog
import math

root = tk.Tk()
root.withdraw()

# 書き出し用ファイル
filename = tkinter.filedialog.asksaveasfilename()
if filename:
    pass
else:
    print("No file specified")
    exit()

# 正弦波を重ね合わせる
cycles = 2
steps = 1000
harmonics = 5

# ファイルオープン
try:
    with open(filename, "w") as file:
        for i in range(steps):
            angle_in_degree = 360 * cycles * i / steps
            angle = math.radians(angle_in_degree)
            s = str(angle_in_degree)
            w = 0
            for i in range(1, harmonics + 1):
                w += math.sin(angle*(i)) / i
                s = s + ", " + str(w)
            file.write(s + "\n")
        print("Writing to file "+ filename + " is finished")
except IOError:
    print("Unable to open file")
