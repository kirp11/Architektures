
import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
import json

from WeatherInformer.api import MyAPI


class AButton(ABC):
    def __init__(self, command):
        self.command = command
    def draw(self): raise NotImplemented

class AWindow(ABC):
    def __init__(self, parent, root=Tk()):
        self.parent = parent
        self.main_root = root
        self.current_var = tk.StringVar()
        self.X_window = 140


    def draw(self): raise NotImplemented


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

class WhiteMainWindow(AWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.button = WhiteButton(self.create_small_window)
        self.combo = WhiteCombobox(self.current_var)
        self.width_main_window = 700
        self.main_root.title("InfoWeather")


    def draw(self):
        size_window = str(f"{self.width_main_window}x400+300+180")

        self.main_root.geometry(size_window)
        self.main_root.resizable(True, True)
        self.main_root.configure(bg="yellow")

        label_name = ttk.Label(text="Погодный информер", font=("Arial", 18), foreground="black", background="yellow")
        label_name.place(x=30, y=30, anchor=W)
        label_theme = ttk.Label(text="Тема", font=("Arial", 18), foreground="black", background="yellow")
        label_theme.place(x=430, y=30, anchor=W)

        label_name2 = ttk.Label(text="Выбрать и добавить из списка городов:", font=("Arial", 14), foreground="black", background="yellow")
        label_name2.place(x=30, y=80, anchor=W)
        light_button = Button( text="Желтая", command=lambda: self.switch_theme(self.parent, "yellow"), bg="white")
        light_button.place(anchor=NW, x=530, y=20, height=30)
        dark_button = Button(text="Синяя", command=lambda: self.switch_theme(self.parent, "blue"), bg="grey")
        dark_button.place(anchor=NW, x=610, y=20, height=30)
        self.button.draw()
        self.combo.draw()
        self.main_root.mainloop()

    def switch_theme(self, window, color):
        window.switch_factory(new_gui_factory=None, color=color)

    def create_small_window(self):
        window = WhiteSmallWindow(self)
        window.draw()
        self.change_main_window()


    def change_main_window(self):

        if self.main_root.winfo_width()+300 < self.X_window+200:
            self.width_main_window +=200
            new_main_size = str(f"{self.width_main_window}x400+300+180")
            self.main_root.geometry(new_main_size)

class BlueMainWindow(AWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.button = BlueButton(self.create_small_window)
        self.combo = BlueCombobox(self.current_var)
        self.width_main_window = 800


    def draw(self):
        size_window = str(f"{self.width_main_window}x400+300+180")

        self.main_root.geometry(size_window)
        self.main_root.resizable(True, True)
        self.main_root.configure(bg="blue")

        label_name = ttk.Label(text="Погодный информер", font=("Arial", 18), foreground="black", background="blue")
        label_name.place(x=30, y=30, anchor=W)

        label_name2 = ttk.Label(text="Выбрать и добавить из списка городов:", font=("Arial", 14), foreground="black", background="blue")
        label_name2.place(x=30, y=80, anchor=W)
        light_button = Button(text="Желтая", command=lambda: self.switch_theme(self.parent, "yellow"), bg="white")
        light_button.place(anchor=NW, x=530, y=20, height=30)
        dark_button = Button(text="Синяя", command=lambda: self.switch_theme(self.parent, "blue"), bg="grey")
        dark_button.place(anchor=NW, x=610, y=20, height=30)
        self.button.draw()
        self.combo.draw()
        self.main_root.mainloop()

    def switch_theme(self, window, color):
        window.switch_factory(new_gui_factory=None, color=color)

    def create_small_window(self):
        window = BlueSmallWindow(self)
        window.draw()
        self.change_main_window()

    def change_main_window(self):

        if self.main_root.winfo_width()+300 < self.X_window+200:
            self.width_main_window +=200
            new_main_size = str(f"{self.width_main_window}x400+300+180")
            self.main_root.geometry(new_main_size)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class WhiteSmallWindow(AWindow):
    def __init__(self, parent):
        super().__init__(parent)

    def draw(self):
        self.parent.X_window += 200

        root = tk.Toplevel(master=self.main_root, background='white')
        root.title(self.parent.current_var.get())

        size = str(f"200x200+{self.parent.X_window}+310")
        root.geometry(size)
        root.resizable(True, True)

        datas = MyAPI(self.parent.current_var.get())

        label_city = ttk.Label(master=root, text=f"Город: ", font=("Arial", 10), foreground="black", background="yellow")
        label_city.place(x=20, y=20, anchor=W)
        label_name = ttk.Label(master=root, text=self.parent.current_var.get(), font=("Arial", 10), foreground="black", background="yellow")
        label_name.place(x=180, y=20, anchor=E)
        label_temperature = ttk.Label(master=root, text=f"Температура: {datas.temp} ^C", font=("Arial", 10), foreground="black", background="yellow")
        label_temperature.place(x=20, y=50, anchor=W)
        label_humidity = ttk.Label(master=root, text=f"Влажность: {datas.hum} %", font=("Arial", 10), foreground="black",
                                      background="yellow")
        label_humidity.place(x=20, y=80, anchor=W)
        label_pressure = ttk.Label(master=root, text=f"Давление: {datas.press} мм.рт.ст", font=("Arial", 10), foreground="black",
                                      background="yellow")
        label_pressure.place(x=20, y=110, anchor=W)
        label_windSpeed = ttk.Label(master=root, text=f"Скорость ветра: {datas.wind} м/с", font=("Arial", 10), foreground="black",
                                      background="yellow")
        label_windSpeed.place(x=20, y=140, anchor=W)
        update_button = Button(master=root, text="Обновить", command="", bg="green")
        update_button.place(anchor=CENTER, x=100, y=180, height=30)




class BlueSmallWindow(AWindow):
    def __init__(self, parent):
        super().__init__(parent)
        # self.X_window = self.parent.X_window

    def draw(self):
        self.parent.X_window += 200

        root = tk.Toplevel(master=self.main_root, background='blue')
        root.title(self.parent.current_var.get())

        size = str(f"200x200+{self.parent.X_window}+310")
        root.geometry(size)
        root.resizable(True, True)

        datas = MyAPI(self.parent.current_var.get())

        label_city = ttk.Label(master=root, text=f"Город: ", font=("Arial", 10), foreground="black", background="white")
        label_city.place(x=20, y=20, anchor=W)
        label_name = ttk.Label(master=root, text=self.parent.current_var.get(), font=("Arial", 10), foreground="black", background="white")
        label_name.place(x=180, y=20, anchor=E)
        label_temperature = ttk.Label(master=root, text=f"Температура: {datas.temp} ^C", font=("Arial", 10), foreground="black", background="white")
        label_temperature.place(x=20, y=50, anchor=W)
        label_humidity = ttk.Label(master=root, text=f"Влажность: {datas.hum} %", font=("Arial", 10), foreground="black",
                                      background="white")
        label_humidity.place(x=20, y=80, anchor=W)
        label_pressure = ttk.Label(master=root, text=f"Давление: {datas.press} мм.рт.ст", font=("Arial", 10), foreground="black",
                                      background="white")
        label_pressure.place(x=20, y=110, anchor=W)
        label_windSpeed = ttk.Label(master=root, text=f"Скорость ветра: {datas.wind} м/с", font=("Arial", 10), foreground="black",
                                      background="white")
        label_windSpeed.place(x=20, y=140, anchor=W)
        update_button = Button(master=root, text="Обновить", command="", bg="yellow")
        update_button.place(anchor=CENTER, x=100, y=180, height=30)



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class WhiteButton(AButton):
    def draw(self):
        choose_button = Button(text="Добавить", command=self.command, bg="red")
        choose_button.place(anchor=NW, x=530, y=70, height=30)


class BlueButton(AButton):
    def draw(self):
        choose_button = Button(text="Добавить", command=self.command, bg="green")
        choose_button.place(anchor=NW, x=530, y=70, height=30)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class WhiteCombobox(ACombobox):

    def draw(self):
        combobox = ttk.Combobox(values=self.cities, state="readonly", background="red", foreground="white", textvariable=self.current_var)
        combobox.place(anchor=NE, x=530, y=70, height=30)

class BlueCombobox(ACombobox):

    def draw(self):
        combobox = ttk.Combobox(values=self.cities, state="readonly", background="blue", foreground="green", textvariable=self.current_var)
        combobox.place(anchor=NE, x=530, y=70, height=30)

