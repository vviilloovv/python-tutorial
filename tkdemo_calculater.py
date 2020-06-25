import tkinter as tk

display_number = 0
terms = []
result = 0

def do_equal():
    global display_number
    global terms
    global result

    terms.append(display_number)
    display_number = 0

    while "/" in terms:
        pos = terms.index("/")
        if terms[pos + 1] == 0:
            del terms[pos : pos + 1]
            continue

        terms[pos - 1] = terms[pos - 1] // terms[pos + 1]
        del terms[pos : pos + 1]

    while "*" in terms:
        pos = terms.index("*")
        terms[pos - 1] *= terms[pos + 1]
        del terms[pos : pos + 1]

    while "+" in terms:
        pos = terms.index("+")
        terms[pos - 1] += terms[pos + 1]
        del terms[pos : pos + 1]

    while "-" in terms:
        pos = terms.index("-")
        terms[pos - 1] -= terms[pos + 1]
        del terms[pos : pos + 1]

    result = terms[0]
    terms.clear()

def key(n):
    global display_number

    display_number = display_number * 10 + n
    show_number(display_number)

def operator(c):
    global display_number
    global terms

    if c == "/" and display_number == 0:
        return


    terms.append(display_number)
    terms.append(c)
    display_number = 0
    show_number(display_number)

def clear():
    global display_number

    display_number = 0
    show_number(display_number)

def equal():
    do_equal()
    show_number(result)

def show_number(num):
    e.delete(0, tk.END)
    e.insert(0, str(num))


# 画面構成
root = tk.Tk()
f = tk.Frame(root)
f.grid()
f.highlightbackground = "#ffffc0"

FONT_TAPPLE = ("Helvetica", 14)

# ウィジェット作成
def generate_number_button(n):
    return tk.Button(f, text = str(n), command = lambda: key(n), font = FONT_TAPPLE, width = 2, highlightbackground = "#ffffff", fg = "#000000")

def generate_operator_button(c):
    return tk.Button(f, text = c, command = lambda: operator(c), font = FONT_TAPPLE, width = 2, highlightbackground = "#00ff00", fg = "#000000")

b1 = generate_number_button(1)
b2 = generate_number_button(2)
b3 = generate_number_button(3)
b4 = generate_number_button(4)
b5 = generate_number_button(5)
b6 = generate_number_button(6)
b7 = generate_number_button(7)
b8 = generate_number_button(8)
b9 = generate_number_button(9)
b0 = generate_number_button(0)

bp = generate_operator_button("+")
bmi = generate_operator_button("-")
bmu = generate_operator_button("*")
bd = generate_operator_button("/")

bc = tk.Button(f, text = "C", command = clear, font = FONT_TAPPLE, width = 2, highlightbackground = "#ff0000", fg = "#000000")
be = tk.Button(f, text = "=", command = equal, font = FONT_TAPPLE, width = 2, highlightbackground = "#00ff00", fg = "#000000")

# ボタン割付
b1.grid(row = 3, column = 0)
b2.grid(row = 3, column = 1)
b3.grid(row = 3, column = 2)
b4.grid(row = 2, column = 0)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 2)
b7.grid(row = 1, column = 0)
b8.grid(row = 1, column = 1)
b9.grid(row = 1, column = 2)
bc.grid(row = 4, column = 0)
b0.grid(row = 4, column = 1)
be.grid(row = 4, column = 2)
bp.grid(row = 1, column = 3)
bmi.grid(row = 2, column = 3)
bmu.grid(row = 3, column = 3)
bd.grid(row = 4, column = 3)

# 数値表示
e = tk.Entry(f, font = FONT_TAPPLE)
e.grid(row = 0, column = 0, columnspan = 4)
clear()

# GUIスタート
root.mainloop()
