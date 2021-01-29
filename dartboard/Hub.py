from ScorerWindow import ScorerWindow
from StartMenuWindow import StartMenuWindow
from PySide2.QtWidgets import QApplication, QMainWindow
import sys

class Hub():
    def __init__(self):


        self.start_menu = StartMenuWindow(self)
        self.start_menu.show()

        self.scorer = ScorerWindow(self)
        #self.scorer.show()

    #add functions and high level things here
