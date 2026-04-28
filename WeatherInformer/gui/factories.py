
from WeatherInformer.gui.product import *




class AWidgetFactory:

    def __init__(self, parent):
        self.parent = parent
    def create_button(self):
        pass

    def create_window(self):
        pass

    def create_combobox(self):
        pass

# _________________________________________

class WhiteWidgetFactory(AWidgetFactory):

    def create_button(self):
        return WhiteButton().draw()

    def create_window(self):
        WhiteMainWindow(self.parent).draw()

    def create_combobox(self):
        return WhiteCombobox().draw()


class BlueWidgetFactory(AWidgetFactory):

    def create_button(self):
        return BlueButton().draw()

    def create_window(self):
        BlueMainWindow(self.parent).draw()

    def create_combobox(self):
        return BlueCombobox().draw()
