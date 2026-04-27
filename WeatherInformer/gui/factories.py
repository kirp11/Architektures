
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
    def __init__(self, parent):
        super().__init__(parent)

    def create_button(self):
        return WhiteButton().draw()

    def create_window(self):
        return WhiteWindow(self).draw_main()

    def create_combobox(self):
        return WhiteCombobox().draw()


class BlueWidgetFactory(AWidgetFactory):
    def __init__(self, parent):
        super().__init__(parent)

    def create_button(self):
        return BlueButton().draw()

    def create_window(self):
        return BlueWindow(self).draw_main()

    def create_combobox(self):
        return BlueCombobox().draw()
