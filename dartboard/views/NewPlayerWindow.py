from views.NewPlayer import Ui_NewPlayer
from PySide2.QtWidgets import QMainWindow
import sys

class NewPlayerWindow(QMainWindow):
    def __init__(self, manage_players):
        super(NewPlayerWindow, self).__init__()

        self.manage_players = manage_players

        self.ui = Ui_NewPlayer()
        self.ui.setupUi(self)

        self.ui.accept_button.clicked.connect(self.accept)
        self.ui.reject_button.clicked.connect(self.reject)


    def accept(self):
        self.manage_players.add_player_to_list(self.ui.first_name_line_edit.text(), self.ui.last_name_line_edit.text())
        self.close()

    def reject(self):
        self.close()
