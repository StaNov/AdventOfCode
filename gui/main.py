from tkinter import *
from tkinter import ttk

import problems

top = Tk()
top.wm_title("Advent of Code 2016, by StaNov")
top.geometry('500x100')

days_box = ttk.Combobox(top, state="readonly")
days_box.grid(row=0)

days_box['values'] = tuple(problems.get_available_days())
days_box.set(days_box['values'][0])


def calculate():
    day_number = int(days_box.get())
    calculator = problems.get_day_calculator(day_number)
    Result1.delete(0, len(Result1.get()))
    Result2.delete(0, len(Result2.get()))
    Result1.insert(0, calculator.calculate_part_1())
    Result2.insert(0, calculator.calculate_part_2())

B = Button(top, text="Calculate Day", command=calculate)
B.grid(row=1, sticky=W+E)

top.grid_columnconfigure(1, weight=1)

L1 = Label(top, text="Result 1:")
L1.grid(row=2)

L2 = Label(top, text="Result 2:")
L2.grid(row=3)

Result1 = Entry(top)
Result1.grid(row=2, column=1, sticky="EW")
Result1.insert(0, "Click Calculate!")

Result2 = Entry(top)
Result2.grid(row=3, column=1, sticky="EW")
Result2.insert(0, "Click Calculate!")

top.mainloop()
