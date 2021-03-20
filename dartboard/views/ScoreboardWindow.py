##################
# ScoreboardWindow
##################

import sys
from views.Scoreboard import Ui_Scoreboard
from PySide2.QtWidgets import QApplication, QMainWindow
from backend.dartboard_api import *

class ScoreboardWindow(QMainWindow):
    def __init__(self, hub):
        super(ScoreboardWindow, self).__init__()

        self.hub = hub
        self.ui = Ui_Scoreboard()
        self.ui.setupUi(self)

    def enter_match_id(self, match_id):
        self.match = get_match_by_id(match_id)
        self.players = get_players_by_match_id(match_id)
        self.update()

    def update(self):
        self.ui.player_1_name.setText(self.players[0].player.full_name)
        self.ui.player_2_name.setText(self.players[1].player.full_name)

