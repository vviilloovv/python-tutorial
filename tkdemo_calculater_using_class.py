import tkinter as tk

display_number = 0
terms = []
result = 0
FONT_TAPPLE = ("Helvetica", 14)


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

# Frameクラス拡張
class MyFrame(tk.Frame):
    # コンストラクタ
    def __init__(self, master = None):
        super().__init__(master)

        b1 = self.generate_number_button(1)
        b2 = self.generate_number_button(2)
        b3 = self.generate_number_button(3)
        b4 = self.generate_number_button(4)
        b5 = self.generate_number_button(5)
        b6 = self.generate_number_button(6)
        b7 = self.generate_number_button(7)
        b8 = self.generate_number_button(8)
        b9 = self.generate_number_button(9)
        b0 = self.generate_number_button(0)

        bp = self.generate_operator_button("+")
        bmi = self.generate_operator_button("-")
        bmu = self.generate_operator_button("*")
        bd = self.generate_operator_button("/")

        bc = tk.Button(self, text = "C", command = self.clear, font = FONT_TAPPLE, width = 2, highlightbackground = "#ff0000", fg = "#000000")
        be = tk.Button(self, text = "=", command = self.equal, font = FONT_TAPPLE, width = 2, highlightbackground = "#00ff00", fg = "#000000")

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

        self.e = tk.Entry(self, font = FONT_TAPPLE)
        self.e.grid(row = 0, column = 0, columnspan = 4)

    # ウィジェット作成
    def generate_number_button(self, n):
        return tk.Button(self, text = str(n), command = lambda: self.key(n), font = FONT_TAPPLE, width = 2, highlightbackground = "#ffffff", fg = "#000000")

    def generate_operator_button(self, c):
        return tk.Button(self, text = c, command = lambda: self.operator(c), font = FONT_TAPPLE, width = 2, highlightbackground = "#00ff00", fg = "#000000")


    def key(self, n):
        global display_number

        display_number = display_number * 10 + n
        self.show_number(display_number)


    def clear(self):
        global display_number

        display_number = 0
        self.show_number(display_number)

    def operator(self, c):
        global display_number
        global terms

        if c == "/" and display_number == 0:
            return

        terms.append(display_number)
        terms.append(c)
        display_number = 0
        self.show_number(display_number)

    def equal(self):
        do_equal()
        self.show_number(result)

    def show_number(self, num):
        self.e.delete(0, tk.END)
        self.e.insert(0, str(num))


# GUIスタート
root = tk.Tk()
f = MyFrame()
f.pack()
root.mainloop()
