

from product import *

class AWidgetFactory:

    def create_button(self):
        pass

    def create_window(self):
        pass

    def create_combobox(self):
        pass

# _________________________________________

class WhiteWidgetFactory(AWidgetFactory):

    def create_button(self):
        return WhiteButton()

    def create_window(self):
        return WhiteWindow()

    def create_combobox(self):
        return WhiteCombobox()


class BlueWidgetFactory(AWidgetFactory):

    def create_button(self):
        return BlueButton()

    def create_window(self):
        return BlueWindow()

    def create_combobox(self):
        return BlueCombobox()
