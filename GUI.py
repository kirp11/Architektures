

from __future__ import annotations
from itertools import chain
from tkinter import *
from tkinter import ttk

X_window = 140
width_main_window = 700
size_window = str(f"{width_main_window}x400+300+180")
main_root = Tk()
main_root.title("Погодный информер")
main_root.geometry(size_window)
main_root.resizable(True, True)
currency = ["USD", "RUB", "EUR", "GBP"]
courses = [90,1,100,150]

def selected_1(event):
    # val_1 = courses[currency.index(text2.get())]
    # amount_currency_2 = float(entry_currency2.get())
    # val_1 = courses[currency.index(text1.get())]
    # amount_currency_1 = ((val_2 * amount_currency_2) / val_1)
    # text_entry1.set(str(amount_currency_1))
    # entry_currency1.configure(textvariable=text_entry1)
    pass

def create_window():
    global X_window
    X_window += 200
    root = Tk()
    text_title = combobox1.get()
    root.title(text_title)
    size = str(f"200x200+{X_window}+310")
    root.geometry(size)
    root.resizable(False, False)
    change_main_window()
    root.mainloop()


def change_main_window():
    global X_window, width_main_window
    print(main_root.winfo_width())
    if main_root.winfo_width()+300 < X_window+200:
        width_main_window +=200
        new_main_size = str(f"{width_main_window}x400+300+180")
        main_root.geometry(new_main_size)
        main_root.mainloop()


label_name = ttk.Label(text="Погодный информер", font = ("Arial", 18), foreground="black")
label_name.place(x=30, y=30, anchor=W)

label_name2 = ttk.Label(text="Выбрать и добавить из списка городов:", font = ("Arial", 14), foreground="blue")
label_name2.place(x=30, y=80, anchor=W)

choose_button = Button(text="Добавить", command=create_window)
choose_button.place(anchor=NW, x=530, y= 70, height=30)

text1 = StringVar()

combobox1 = ttk.Combobox(textvariable=text1, values=currency, state="readonly")
combobox1.place(anchor=NE, x=530, y= 70, height=30)
combobox1.bind("<<ComboboxSelected>>",selected_1)


main_root.mainloop()


# class WeatherWindow:
