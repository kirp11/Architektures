

from gui.factories import AWidgetFactory

class App:

    def __init__(self, gui_factory: AWidgetFactory):
        self.gui_factory = gui_factory

    def draw_ui(self):
        self.gui_factory.create_window()
        self.gui_factory.create_button()
        self.gui_factory.create_combobox()

    def switch_factory(self, new_gui_factory):
        self.gui_factory = new_gui_factory
        self.draw_ui()