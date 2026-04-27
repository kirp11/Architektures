from app import App

from WeatherInformer.gui.factories import *

main_app = App()
main_app.switch_factory(BlueWidgetFactory(main_app))

main_app.draw_ui()
