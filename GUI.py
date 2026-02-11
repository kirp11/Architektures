

from __future__ import annotations
from itertools import chain
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Погодный информер")
root.geometry("700x400")
root.resizable(True, True)
currency = ["USD", "RUB", "EUR", "GBP"]
courses = [90,1,100,150]

def selected_1(event):
    val_2 = courses[currency.index(text2.get())]
    amount_currency_2 = float(entry_currency2.get())
    val_1 = courses[currency.index(text1.get())]
    amount_currency_1 = ((val_2 * amount_currency_2) / val_1)
    text_entry1.set(str(amount_currency_1))
    entry_currency1.configure(textvariable=text_entry1)


label_name = ttk.Label(text="Погодный информер", font = ("Arial", 18), foreground="black")
label_name.place(x=30, y=30, anchor=W)

label_name2 = ttk.Label(text="Выбрать и добавить из списка городов", font = ("Arial", 14), foreground="blue")
label_name2.place(x=30, y=80, anchor=W)

choose_button = Button(text="Добавить")
choose_button.place(anchor=NW, x=180, y= 100, height=30)

text1 = StringVar()

combobox1 = ttk.Combobox(textvariable=text1, values=currency, state="readonly")
combobox1.place(anchor=NE, x=180, y= 100, height=30)
combobox1.bind("<<ComboboxSelected>>",selected_1)


root.mainloop()


class WeatherWindow:
