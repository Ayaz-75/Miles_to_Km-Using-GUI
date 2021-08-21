from tkinter import *

windows = Tk()
windows.minsize(300, 200)
windows.title("Mile to Kilometers Converter")
windows.config(padx=50, pady=50)


entry_input = Entry(width=10)
entry_input.grid(column=1, row=0)


miles_label = Label(text="Miles", font=("Arial", 10, "normal"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)


is_equal_label = Label(text="is equal to", font=("Arial", 10, "normal"))
is_equal_label.grid(column=0, row=1)


km_label = Label(text="Km", font=("Arial", 10, "normal"))
km_label.grid(column=2, row=1)


to_km_cover_label = Label(text="0", font=("Arial", 10, "normal"))
to_km_cover_label.grid(column=1, row=1)


def calc_km():
    miles = entry_input.get()
    km = float(miles) * 1.609
    to_km_cover_label.config(text=f"{km}")


button = Button(text="Calculate", command=calc_km)
button.grid(column=1, row=2)


windows.mainloop()
