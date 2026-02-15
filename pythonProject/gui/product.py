
from abc import ABC, abstractmethod

class AButton(ABC):
    def draw(self): raise NotImplemented



class AWindow(ABC):

    def draw(self): raise NotImplemented


class ACombobox(ABC):
    def draw(self): raise NotImplemented

# _________________________________________________________________________________________________
class WhiteButton(AButton):
    def draw(self):
        pass

class BlueButton(AButton):
    def draw(self):
        pass


class WhiteWindow(AWindow):

    def draw_main(self):
        pass

    def draw_other(self):
        pass

class BlueWindow(AWindow):

    def draw_main(self):
        pass

    def draw_other(self):
        pass

class WhiteCombobox(ACombobox):

    def draw(self):
        pass

class BlueCombobox(ACombobox):

    def draw(self):
        pass
