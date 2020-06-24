import tkinter as tk

current_number = 0
first_term = 0
second_term = 0
result = 0

def do_plus():
    global current_number
    global first_term

    first_term = current_number
    current_number = 0

def do_equal():
    global current_number
    global second_term
    global result

    second_term = current_number
    result = first_term + second_term
    current_number = 0

def key(n):
    global current_number
    current_number = current_number * 10 + n
    show_number(current_number)

def clear():
    global current_number
    current_number = 0
    show_number(current_number)

def plus():
    do_plus()
    show_number(current_number)

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

# ウィジェット作成
b1 = tk.Button(f,text='1', command = lambda: key(1), font=("Helvetica", 14))
b2 = tk.Button(f,text='2', command = lambda: key(2), font=("Helvetica", 14))
b3 = tk.Button(f,text='3', command = lambda: key(3), font=("Helvetica", 14))
b4 = tk.Button(f,text='4', command = lambda: key(4), font=("Helvetica", 14))
b5 = tk.Button(f,text='5', command = lambda: key(5), font=("Helvetica", 14))
b6 = tk.Button(f,text='6', command = lambda: key(6), font=("Helvetica", 14))
b7 = tk.Button(f,text='7', command = lambda: key(7), font=("Helvetica", 14))
b8 = tk.Button(f,text='8', command = lambda: key(8), font=("Helvetica", 14))
b9 = tk.Button(f,text='9', command = lambda: key(9), font=("Helvetica", 14))
b0 = tk.Button(f,text='0', command = lambda: key(0), font=("Helvetica", 14))
bc = tk.Button(f,text='C', command = clear, font=("Helvetica", 14))
bp = tk.Button(f,text='+', command = plus, font=("Helvetica", 14))
be = tk.Button(f,text="=", command = equal, font=("Helvetica", 14))

# グリッドによるウィジェットの割付
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=0)
bc.grid(row=1,column=3)
be.grid(row=4,column=3)
bp.grid(row=2,column=3)

# 数値表示ウィジェット
e = tk.Entry(f)
e.grid(row=0,column=0,columnspan=4)
clear()

# GUIスタート
root.mainloop()
