from views.StartGameConfiguration import Ui_StartGameConfiguration
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
        print("{}".format(self.ui.player_two_line_edit.text()))
        print("{}".format(self.ui.location_line_edit.text()))
        print("{}".format(self.ui.date_edit.text()))
        print("{}".format(self.ui.number_of_legs_spin_box.value()))
        print("{}".format(self.ui.number_of_sets_spin_box.value()))
        print("{}".format(self.ui.leg_value_801_radio_button.isChecked()))
        print("{}".format(self.ui.leg_value_501_radio_button.isChecked()))
        print("{}".format(self.ui.leg_value_301_radio_button.isChecked()))
        print("{}".format(self.ui.league_rank_checkbox.checkState()))
        print("{}".format(self.ui.last_match_win_checkbox.checkState()))
        print("{}".format(self.ui.last_champ_win_checkbox.checkState()))
        print("{}".format(self.ui.season_avg_checkbox.checkState()))
        print("{}".format(self.ui.lifetime_avg_checkbox.checkState()))
        print("{}".format(self.ui.season_180s_checkbox.checkState()))

        #get player object through player name

        
        
        self.hide()
        self.hub.navigate_to_view("scorer")
        self.hub.navigate_to_view("scoreboard")
        self.hub.send_match_id(match_id)
        
