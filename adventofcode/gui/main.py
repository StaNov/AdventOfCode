from tkinter import *
from tkinter import ttk

from adventofcode import problems


def run_gui():
    top = Tk()
    top.wm_title("Advent of Code, by StaNov")
    top.geometry('600x300')

    days_box = ttk.Combobox(top, state="readonly")
    days_box.grid(row=0)

    days_box['values'] = tuple(problems.get_available_days())
    days_box.set(days_box['values'][0])

    def calculate():
        day_number = int(days_box.get())
        calculator = problems.get_day_calculator(day_number)
        result_text_1.config(state=NORMAL)
        result_text_2.config(state=NORMAL)
        result_text_1.delete(1.0, END)
        result_text_2.delete(1.0, END)
        result_text_1.insert(END, calculator.calculate_part_1())
        result_text_2.insert(END, calculator.calculate_part_2())
        result_text_1.config(state=DISABLED)
        result_text_2.config(state=DISABLED)

    calculate_button = Button(top, text="Calculate!", command=calculate)
    calculate_button.grid(row=0, column=1, sticky=W+E)

    result_label_1 = Label(top, text="Result 1:")
    result_label_1.grid(row=1)

    result_label_2 = Label(top, text="Result 2:")
    result_label_2.grid(row=2)

    result_text_1 = Text(top)
    result_text_1.grid(row=1, column=1, sticky="EW")
    result_text_1.insert(END, "Click Calculate!")
    result_text_1.config(state=DISABLED)

    result_text_2 = Text(top)
    result_text_2.grid(row=2, column=1, sticky="EW")
    result_text_2.insert(END, "Click Calculate!")
    result_text_2.config(state=DISABLED)

    top.grid_columnconfigure(1, weight=1)
    top.grid_rowconfigure(1, weight=1)
    top.grid_rowconfigure(2, weight=1)

    top.mainloop()


if __name__ == "__main__":
    run_gui()
