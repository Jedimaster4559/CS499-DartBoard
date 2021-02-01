from StartGameConfiguration import Ui_StartGameConfiguration
from PySide2.QtWidgets import QApplication, QMainWindow
import sys

class StartGameConfigurationWindow(QMainWindow):
    def __init__(self, hub):
        super(StartGameConfigurationWindow, self).__init__()

        self.hub = hub

        self.ui = Ui_StartGameConfiguration()
        self.ui.setupUi(self)

        self.ui.start_game_button.clicked.connect(self.start_game)

    def start_game(self):
        print("{}".format(self.ui.player_one_line_edit.text()))
        self.hide()
        self.hub.navigate_to_view("scorer")
        
