
from WeatherInformer.gui.product import *


class AWidgetFactory:

    def __init__(self, parent):
        self.parent = parent

    def create_window(self):
        pass

# _________________________________________

class WhiteWidgetFactory(AWidgetFactory):


    def create_window(self):
        WhiteMainWindow(self.parent).draw()



class BlueWidgetFactory(AWidgetFactory):


    def create_window(self):
        BlueMainWindow(self.parent).draw()

