from views.Scorer import Ui_Scorer
from PySide2.QtWidgets import QApplication, QMainWindow
import sys

class ScorerWindow(QMainWindow):
    def __init__(self, hub):
        super(ScorerWindow, self).__init__()

        self.hub = hub

        self.ui = Ui_Scorer()
        self.ui.setupUi(self)

    def enter_match_id(self, match_id):
        print(match_id)
        print("got it")
    
