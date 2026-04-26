import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
import json

class AButton(ABC):
    def __init__(self, command):
        self.command = command
    def draw(self): raise NotImplemented

class AWindow(ABC):
    def __init__(self):
        self.main_root = Tk()
        self.main_root.title("InfoWeather")
        self.current_var = tk.StringVar()
        self.X_window = 140
        self.width_main_window = 700



    def draw_main(self): raise NotImplemented

    def draw_other(self): raise NotImplemented

class ACombobox(ABC):
    def __init__(self, current_var):
        self.cities = []
        with open('russian-cities.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        for i in data:
            self.cities.append(i["name"])

        self.current_var = current_var
    def draw(self): raise NotImplemented

# _________________________________________________________________________________________________

class WhiteWindow(AWindow):
    def __init__(self):
        super().__init__()
        self.current_vari = tk.StringVar()
        self.button = WhiteButton(self.draw_other)
        self.combo = WhiteCombobox(self.current_vari)


    def draw_main(self):
        size_window = str(f"{self.width_main_window}x400+300+180")

        self.main_root.geometry(size_window)
        self.main_root.resizable(True, True)
        self.main_root.configure(bg="yellow")

        label_name = ttk.Label(text="Погодный информер", font=("Arial", 18), foreground="black", background="yellow")
        label_name.place(x=30, y=30, anchor=W)

        label_name2 = ttk.Label(text="Выбрать и добавить из списка городов:", font=("Arial", 14), foreground="black", background="yellow")
        label_name2.place(x=30, y=80, anchor=W)
        self.button.draw()
        self.combo.draw()
        self.main_root.mainloop()

    def draw_other(self):
        self.X_window += 200
        root = tk.Toplevel(master=self.main_root)
        root.title(self.current_vari.get())
        size = str(f"200x200+{self.X_window}+310")
        root.geometry(size)
        root.resizable(True, True)
        self.change_main_window()

    def change_main_window(self):

        if self.main_root.winfo_width()+300 < self.X_window+200:
            self.width_main_window +=200
            new_main_size = str(f"{self.width_main_window}x400+300+180")
            self.main_root.geometry(new_main_size)
            self.main_root.mainloop()

class BlueWindow(AWindow):
    def __init__(self):
        super().__init__()
        self.current_vari = tk.StringVar()
        self.button = BlueButton(self.draw_other)
        self.combo = BlueCombobox(self.current_vari)


    def draw_main(self):
        size_window = str(f"{self.width_main_window}x400+300+180")

        self.main_root.geometry(size_window)
        self.main_root.resizable(True, True)
        self.main_root.configure(bg="blue")

        label_name = ttk.Label(text="Погодный информер", font=("Arial", 18), foreground="black", background="blue")
        label_name.place(x=30, y=30, anchor=W)

        label_name2 = ttk.Label(text="Выбрать и добавить из списка городов:", font=("Arial", 14), foreground="black", background="blue")
        label_name2.place(x=30, y=80, anchor=W)
        self.button.draw()
        self.combo.draw()
        self.main_root.mainloop()

    def draw_other(self):
        self.X_window += 200
        root = tk.Toplevel(master=self.main_root)
        root.title(self.current_vari.get())
        print(self.current_var, self.combo.current_var)
        size = str(f"200x200+{self.X_window}+310")
        root.geometry(size)
        root.resizable(True, True)
        self.change_main_window()

    def change_main_window(self):

        if self.main_root.winfo_width()+300 < self.X_window+200:
            self.width_main_window +=200
            new_main_size = str(f"{self.width_main_window}x400+300+180")
            self.main_root.geometry(new_main_size)
            self.main_root.mainloop()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class WhiteButton(AButton):
    def draw(self):
        choose_button = Button(text="Добавить", command=self.command,
                               bg="black")
        choose_button.place(anchor=NW, x=530, y=70, height=30)

class BlueButton(AButton):
    def draw(self):
        choose_button = Button(text="Добавить", command=self.command,
                               bg="blue")
        choose_button.place(anchor=NW, x=530, y=70, height=30)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class WhiteCombobox(ACombobox):

    def draw(self):
        combobox = ttk.Combobox(values=self.cities, state="readonly",
                                background="red",
                                foreground="white", textvariable=self.current_var)
        combobox.place(anchor=NE, x=530, y=70, height=30)

class BlueCombobox(ACombobox):

    def draw(self):

        combobox = ttk.Combobox(values=self.cities, state="readonly",
                                background="blue",
                                foreground="green", textvariable=self.current_var)
        combobox.place(anchor=NE, x=530, y=70, height=30)

