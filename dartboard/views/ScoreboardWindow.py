from views.Scoreboard import Ui_Scoreboard
from PySide2.QtWidgets import QApplication, QMainWindow
import sys

class ScoreboardWindow(QMainWindow):
    def __init__(self, hub):
        super(ScoreboardWindow, self).__init__()

        self.hub = hub

        self.ui = Ui_Scoreboard()
        self.ui.setupUi(self)
