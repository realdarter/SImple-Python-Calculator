import tkinter as tk

amount = 0

root = tk.Tk()
root.title("Calculator")
root.resizable(width=False, height=False)


entry = tk.Entry(root, width=15)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
result_label = tk.Label(root, width=10, text="Output")
result_label.grid(row=0, column=2, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def add():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + "+")
def subtract():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + "-")

def multiply():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + "*")

def divide():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + "/")

def dot():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + ".")

def percent():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + "%")

def equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0,tk.END)
        result_label.config(text="Result: " + str(result))
    except:
        entry.delete(0, tk.END)
        result_label.config(text="Error")


button_0 = tk.Button(root, text="0",padx=20,pady=10,command=lambda: button_click(0))
button_1 = tk.Button(root, text="1",padx=20,pady=10,command=lambda: button_click(1))
button_2 = tk.Button(root, text="2",padx=20,pady=10,command=lambda: button_click(2))
button_3 = tk.Button(root, text="3",padx=20,pady=10,command=lambda: button_click(3))
button_4 = tk.Button(root, text="4",padx=20,pady=10,command=lambda: button_click(4))
button_5 = tk.Button(root, text="5",padx=20,pady=10,command=lambda: button_click(5))
button_6 = tk.Button(root, text="6",padx=20,pady=10,command=lambda: button_click(6))
button_7 = tk.Button(root, text="7",padx=20,pady=10,command=lambda: button_click(7))
button_8 = tk.Button(root, text="8",padx=20,pady=10,command=lambda: button_click(8))
button_9 = tk.Button(root, text="9",padx=20,pady=10,command=lambda: button_click(9))
button_plus = tk.Button(root, text="+",padx=20,pady=10,command=add)
button_minus = tk.Button(root, text="-",padx=20,pady=10,command=subtract)
button_multiply = tk.Button(root, text="*",padx=20,pady=10,command=multiply)
button_divide = tk.Button(root, text="/",padx=20,pady=10,command=divide)
button_dot = tk.Button(root, text=".",padx=20,pady=10,command=dot)
button_percent = tk.Button(root, text="%",padx=20,pady=10,command=percent)

button_equal = tk.Button(root, text="=",padx=20,pady=10,command=equal)

button_1.grid(row=1, column = 0)
button_2.grid(row=2, column = 0)
button_3.grid(row=3, column = 0)
button_4.grid(row=1, column = 1)
button_5.grid(row=2, column = 1)
button_6.grid(row=3, column = 1)
button_7.grid(row=1, column = 2)
button_8.grid(row=2, column = 2)
button_9.grid(row=3, column = 2)
button_0.grid(row=4, column = 1)
button_plus.grid(row=1, column = 3)
button_minus.grid(row=2, column = 3)
button_multiply.grid(row=3, column = 3)
button_divide.grid(row=4, column = 3)
button_dot.grid(row=4, column = 0)
button_percent.grid(row=4, column = 2)

button_equal.grid(row=5, column = 3)

root.mainloop()
