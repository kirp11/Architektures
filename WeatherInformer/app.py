
from gui.factories import AWidgetFactory, WhiteWidgetFactory, BlueWidgetFactory


class App:

    def __init__(self, gui_factory: AWidgetFactory = None):
        self.gui_factory = gui_factory
        self.factories = {"yellow": WhiteWidgetFactory,
                          "blue": BlueWidgetFactory}

    def draw_ui(self):
        self.gui_factory.create_window()


    def switch_factory(self, new_gui_factory, color):
        if color:
            col = self.factories.get(color)
            self.gui_factory = col(self)
            self.draw_ui()
            return
        self.gui_factory = new_gui_factory
        self.draw_ui()
