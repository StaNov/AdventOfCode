from tkinter import *
from tkinter import ttk

import problems

top = Tk()
top.wm_title("Advent of Code 2016, by StaNov")
top.geometry('600x300')

days_box = ttk.Combobox(top, state="readonly")
days_box.grid(row=0)

days_box['values'] = tuple(problems.get_available_days())
days_box.set(days_box['values'][0])


def calculate():
    day_number = int(days_box.get())
    calculator = problems.get_day_calculator(day_number)
    Result1.config(state=NORMAL)
    Result2.config(state=NORMAL)
    Result1.delete(1.0, END)
    Result2.delete(1.0, END)
    Result1.insert(END, calculator.calculate_part_1())
    Result2.insert(END, calculator.calculate_part_2())
    Result1.config(state=DISABLED)
    Result2.config(state=DISABLED)


B = Button(top, text="Calculate!", command=calculate)
B.grid(row=0, column=1, sticky=W+E)

L1 = Label(top, text="Result 1:")
L1.grid(row=1)

L2 = Label(top, text="Result 2:")
L2.grid(row=2)

Result1 = Text(top)
Result1.grid(row=1, column=1, sticky="EW")
Result1.insert(END, "Click Calculate!")
Result1.config(state=DISABLED)

Result2 = Text(top)
Result2.grid(row=2, column=1, sticky="EW")
Result2.insert(END, "Click Calculate!")
Result2.config(state=DISABLED)

top.grid_columnconfigure(1, weight=1)
top.grid_rowconfigure(1, weight=1)
top.grid_rowconfigure(2, weight=1)

top.mainloop()
