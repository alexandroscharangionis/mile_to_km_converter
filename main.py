from tkinter import *


def convert():
    result = float(miles_entry.get()) * 1.609
    result_label.config(text=result)


window = Tk()
window.title("Mile to KM converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

miles_entry = Entry(width=6)
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Helvetica", 14))
miles_label.config(padx=5)
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Helvetica", 14))
is_equal_label.config(padx=5)
is_equal_label.grid(column=0, row=1)

result_label = Label(text="0", font=("Helvetica", 14))
result_label.grid(column=1, row=1)

km_label = miles_label = Label(text="KM", font=("Helvetica", 14))
km_label.grid(column=2, row=1)

calculate_btn = Button(text="Calculate", command=convert)
calculate_btn.grid(column=1, row=2)

window.mainloop()
