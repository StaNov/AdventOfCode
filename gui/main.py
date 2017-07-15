from tkinter import *
from problems.day01.main import DayCalculator

top = Tk()
top.wm_title("Advent of Code 2016, by StaNov")
top.geometry('500x100')

top.grid_columnconfigure(1, weight=1)

L1 = Label(top, text="Result 1:")
L1.grid(row=1)

L2 = Label(top, text="Result 2:")
L2.grid(row=2)

Result1 = Entry(top)
Result1.grid(row=1, column=1, sticky="EW")
Result1.insert(0, "Click Calculate!")

Result2 = Entry(top)
Result2.grid(row=2, column=1, sticky="EW")
Result2.insert(0, "Click Calculate!")


def calculate():
    calculator = DayCalculator()
    Result1.delete(0, len(Result1.get()))
    Result2.delete(0, len(Result2.get()))
    Result1.insert(0, calculator.calculate_part_1())
    Result2.insert(0, calculator.calculate_part_2())

B = Button(top, text="Calculate Day 1", command=calculate)
B.grid(row=0, sticky=W+E)

top.mainloop()
