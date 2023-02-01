from tkinter import *

window = Tk()
window.minsize(width=570, height=600)
window.resizable(False, False)
window.title("Kalkulačka")
window.config(bg="#17161b")

# Proměnné
bg_color = "#2a2d36"
equation = ""

# Funkce
def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)

# Základní tlačítko
class BasicButton:

    def __init__(self, txt, row, column):
        myButton = Button(window, text=txt, font=("Arial", 30, "bold"), fg="#fff", bg=bg_color, width=5, height=1, relief="raised",borderwidth=3, command=lambda: show(txt))
        myButton.grid(row=row, column=column, padx=5, pady=5)

# Specialní tlačítko
class SpecialButton:
    def __init__(self, txt, color, fce, row, column, rwspan, colspan, sticky):
        myButton = Button(window, text=txt, font=("Arial", 30, "bold"), fg="#fff", bg=color, width=5, height=1, relief="raised", borderwidth=3, command=fce)
        myButton.grid(row=row, column=column, rowspan=rwspan, columnspan=colspan, sticky=sticky, padx=5, pady=5)

# Label
label_result = Label(window, width=25, height=2, text="", font=("Arial", 30), bg="#cddad9", borderwidth=5, relief="sunken", justify=RIGHT, anchor=E)
label_result.grid(row=0, column=0, columnspan=4, pady=18, padx=10)

# Speciální tlačítka
c_button = SpecialButton("C", "#e76f51", clear, 1, 0, 1, 1, "")
rslt_button = SpecialButton("=", "#2a9d8f", calculate, 5, 2, 1, 2, EW)

# Standardní tlačítka
button_div = BasicButton("/", 1, 1)
button_pro = BasicButton("(", 1, 2)
button_prc = BasicButton(")", 1, 3)

button_mlt = BasicButton("*", 2, 3)
button_7 = BasicButton("7", 2, 0)
button_8 = BasicButton("8", 2, 1)
button_9 = BasicButton("9", 2, 2)

button_min = BasicButton("-", 3, 3)
button_4 = BasicButton("4", 3, 0)
button_5 = BasicButton("5", 3, 1)
button_6 = BasicButton("6", 3, 2)

button_pls = BasicButton("+", 4, 3)
button_1 = BasicButton("1", 4, 0)
button_2 = BasicButton("2", 4, 1)
button_3 = BasicButton("3", 4, 2)

button_0 = BasicButton("0", 5, 0)
button_com = BasicButton(".", 5, 1)


window.mainloop()