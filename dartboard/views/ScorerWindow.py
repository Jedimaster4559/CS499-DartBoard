from views.Scorer import Ui_Scorer
from PySide2.QtWidgets import QApplication, QMainWindow
from backend.dartboard_api import get_match_by_id, get_players_by_match_id, get_number_of_legs_by_match_id
import sys

class ScorerWindow(QMainWindow):
    def __init__(self, hub):
        super(ScorerWindow, self).__init__()

        self.hub = hub

        self.ui = Ui_Scorer()
        self.ui.setupUi(self)
        self.ui.graphicsView.setup_signal(self)

    def enter_match_id(self, match_id):
        self.match = get_match_by_id(match_id)

        self.number_of_sets = self.match.best_of_sets_number
        self.number_of_legs = get_number_of_legs_by_match_id(match_id)

        players = get_players_by_match_id(match_id)

        # set names
        self.ui.tabWidget.setTabText(0, players[0].player.full_name)
        self.ui.tabWidget.setTabText(1, players[1].player.full_name)

        self.change_set_number_label(1)
        self.change_leg_number_label(1)

    def change_set_number_label(self, current_set):
        result = str(current_set) + "/" + str(self.number_of_sets)
        self.ui.SetNumberLabel.setText(result)

    def change_leg_number_label(self, current_leg):
        result = str(current_leg) + "/" + str(self.number_of_legs)
        self.ui.LegNumberLabel.setText(result)

    def dart_thrown(self, msg):
        print("Coming from Scorer: {}".format(msg))
        

        

        
    
