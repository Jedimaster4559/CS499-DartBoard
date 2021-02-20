from views.ManagePlayers import Ui_ManagePlayers
from views.NewPlayerWindow import NewPlayerWindow
from PySide2.QtWidgets import QMainWindow
import sys

class ManagePlayersWindow(QMainWindow):
    def __init__(self, hub):
        super(ManagePlayersWindow, self).__init__()

        self.hub = hub

        self.ui = Ui_ManagePlayers()
        self.ui.setupUi(self)

        self.ui.new_player_button.clicked.connect(self.open_new_player_dialog)


    def open_new_player_dialog(self):
        self.new_player_dialog = NewPlayerWindow(self)
        self.new_player_dialog.show()

    def add_player_to_list(self, first, last):
        print("add player with first name of : {} and last name of {}".format(first.text(), last.text()))
