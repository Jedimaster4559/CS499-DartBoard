from views.ManagePlayers import Ui_ManagePlayers
from views.NewPlayerWindow import NewPlayerWindow
from PySide2.QtWidgets import QMainWindow
import sys
from backend.dartboard_api import create_player, get_all_players

class ManagePlayersWindow(QMainWindow):
    def __init__(self, hub):
        super(ManagePlayersWindow, self).__init__()

        self.hub = hub

        self.ui = Ui_ManagePlayers()
        self.ui.setupUi(self)

        self.ui.new_player_button.clicked.connect(self.open_new_player_dialog)
        self.ui.return_button.clicked.connect(self.return_to_menu)
        self.populate_players()

    def return_to_menu(self):
        self.hub.navigate_to_view("start_menu")
        self.hide()

    def open_new_player_dialog(self):
        self.new_player_dialog = NewPlayerWindow(self)
        self.new_player_dialog.show()

    def add_player_to_list(self, first, last):
        print("add player with first name of : {} and last name of {}".format(first, last))
        create_player(first_name=first, last_name=last)
        self.populate_players()

    def populate_players(self):
        self.ui.players_listwidget.clear()
        for x in get_all_players():
            self.ui.players_listwidget.addItem(str(x))
