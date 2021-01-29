from Scorer import Ui_Scorer
from PySide2.QtWidgets import QApplication, QMainWindow
import sys

class Hub(QMainWindow):
    def __init__(self):
        super(Hub, self).__init__()
        self.ui = Ui_Scorer()
        self.ui.setupUi(self)

    #add functions and high level things here
