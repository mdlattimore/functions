
import tkinter as tk
from tkinter import ttk


def square_value():
    answer = entry_value.get() ** 2
    entry_value.set(answer)


def cube_value():
    answer = entry_value.get() ** 3
    entry_value.set(answer)


def sqrt_value():
    answer = entry_value.get() ** (1/2)
    entry_value.set(answer)


def cubert_value():
    answer = entry_value.get() ** (1/3)
    entry_value.set(answer)


def bin_convert():
    converted = str(entry_value.get())
    bin_num = [char for char in converted][::-1]
    result = []
    for index, digit in enumerate(bin_num):
        x = int(digit) * (2 ** index)
        result.append(x)
    entry_value.set(sum(result))


def dec_convert():
    number = entry_value.get()
    entry_value.set(str(bin(number)[2:]))



root = tk.Tk()
root.title("Simple Calculator")

mainframe = ttk.Frame(root)
mainframe.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

entry_value = tk.IntVar()
entry_value.set('')
entry_field = ttk.Entry(mainframe, width=20, textvariable=entry_value)
entry_field.grid(row=0, column=0, columnspan=2, ipadx=10, ipady=10)
entry_field.focus()

button_frame = ttk.Frame(mainframe)
button_frame.grid(row=1, column=0)
xsqr = ttk.Button(button_frame, text="x ** 2", command=square_value)
xsqr.grid(row=0, column=0, sticky="ew")
xcube = ttk.Button(button_frame, text="x ** 3", command=cube_value)
xcube.grid(row=0, column=1, sticky="ew")
xsqrt = ttk.Button(button_frame, text="x ** 1/2", command=sqrt_value)
xsqrt.grid(row=1, column=0, sticky="ew")
xcubert = ttk.Button(button_frame, text="x ** 1/3", command=cubert_value)
xcubert.grid(row=1, column=1, sticky="ew")
bin_to_dec = ttk.Button(button_frame, text="bin -> dec", command=bin_convert)
bin_to_dec.grid(row=2, column=0, sticky="ew")
dec_to_bin = ttk.Button(button_frame, text="dec -> bin", command=dec_convert)
dec_to_bin.grid(row=2, column=1, sticky="ew")

root.mainloop()