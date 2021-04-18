##################
# ScoreboardWindow
##################

import sys

from backend.fewest_darts import *
from views.Scoreboard import Ui_Scoreboard
from PySide2.QtWidgets import QApplication, QMainWindow, QCheckBox, QTableWidgetItem, QWidget, QHBoxLayout, QHeaderView, QPushButton
from PySide2.QtCore import Qt
from backend.dartboard_api import *


class ScoreboardWindow(QMainWindow):
    def __init__(self, hub):
        super(ScoreboardWindow, self).__init__()

        self.hub = hub
        self.ui = Ui_Scoreboard()
        self.ui.setupUi(self)
        self.tables = [self.ui.Player1DartsTable, self.ui.Player2DartsTable]

        self.current_set = 1
        self.current_leg = 1
        self.ui.player_one_additional_stats.hide()
        self.ui.player_two_additional_stats.hide()
        self.ui.fewest_darts_player_one_label.hide()
        self.ui.fewest_darts_player_two_label.hide()


    def enter_match_id(self, match_id):
        self.match = get_match_by_id(match_id)
        self.players = get_players_by_match_id(match_id)
        leg = get_leg_by_number(match_id=match_id, set_number=1, leg_number=1)
        
    def clear_scoreboard(self):
        while self.ui.Player1DartsTable.rowCount() > 0:
            self.ui.Player1DartsTable.removeRow(0)
        while self.ui.Player2DartsTable.rowCount() > 0:
            self.ui.Player2DartsTable.removeRow(0)

    def set_additional_game_statistics(self,stat):
        if stat:
            self.ui.player_one_additional_stats.show()
            self.ui.player_two_additional_stats.show()
            self.ui.player_one_additional_stats.setText(stat)
            self.ui.player_two_additional_stats.setText(stat)

    def update(self, turn_1, turn_2):
        #update is called in ScorerWindow remove_dart_throw, enter_match_id, and dart_thrown
        self.clear_scoreboard()
        hits_player_1 = get_hits(turn_1)
        hits_player_2 = get_hits(turn_2)
        first, second, third = "", "-1", ""

        #get checkouts for player 1 if applicable
        if (get_turn_score_remaining(turn_1) <= 170):
            # we can call checkout function
            if hits_player_1.count() == 0:
                first, second, third = check_outs.initial_sum(get_turn_score_remaining(turn_1))
            elif hits_player_1.count() == 1:
                first, second, third = check_outs.first_sum(get_turn_score_remaining(turn_1), hits_player_1[hits_player_1.count()-1])
            elif hits_player_1.count() == 2:
                first, second, third = check_outs.second_sum(get_turn_score_remaining(turn_1), hits_player_1[hits_player_1.count() - 2], hits_player_1[hits_player_1.count()-1])
            if first != "":
                self.ui.player_one_checkouts_label.setText("{} | {} | {}".format(first, second, third))
                self.ui.player_one_checkouts_label.show()
            else:
                self.ui.player_one_checkouts_label.hide()
            
        else:
            self.ui.player_one_checkouts_label.hide()

        #get checkouts for player 2 if applicable
        if (get_turn_score_remaining(turn_2) <= 170):
            # we can call checkout function
            if hits_player_2.count() == 0:
                first, second, third = check_outs.initial_sum(get_turn_score_remaining(turn_2))
            elif hits_player_2.count() == 1:
                first, second, third = check_outs.first_sum(get_turn_score_remaining(turn_2), hits_player_2[hits_player_2.count()-1])
            elif hits_player_2.count() == 2:
                first, second, third = check_outs.second_sum(get_turn_score_remaining(turn_2), hits_player_2[hits_player_2.count() - 2], hits_player_2[hits_player_2.count()-1])
            if first != "":
                self.ui.player_two_checkouts_label.setText("{} | {} | {}".format(first, second, third))
                self.ui.player_two_checkouts_label.show()
            else:
                self.ui.player_two_checkouts_label.hide()

        else:
            self.ui.player_two_checkouts_label.hide()

        print(turn_1.game.leg_number)
        print(turn_1.player.player.first_name)


        print(fewestdartschecker(get_all_hits_in_leg(turn_1.game, turn_1.player), first, second, third, get_leg_value(turn_1)))
        if(fewestdartschecker(get_all_hits_in_leg(turn_1.game, turn_1.player), first, second, third, get_leg_value(turn_1))):
            self.ui.fewest_darts_player_one_label.show()
        else:
            self.ui.fewest_darts_player_one_label.hide()

        print(fewestdartschecker(get_all_hits_in_leg(turn_2.game, turn_2.player), first, second, third, get_leg_value(turn_2)))
        if(fewestdartschecker(get_all_hits_in_leg(turn_1.game, turn_1.player), first, second, third, get_leg_value(turn_1))):
            self.ui.fewest_darts_player_two_label.show()
        else:
            self.ui.fewest_darts_player_two_label.hide()


        index = 0

        for hit in hits_player_1:
            self.addpopulaterow(
                self.tables[0], hit.score, hit.is_bounce_out, hit.is_knock_out, hit.is_foul, index)
            index = index+1

        index = 0

        for hit in hits_player_2:
            self.addpopulaterow(
                self.tables[1], hit.score, hit.is_bounce_out, hit.is_knock_out, hit.is_foul, index)
            index = index+1

        # Set Players Name
        self.ui.player_1_name.setText(self.players[0].player.full_name)
        self.ui.player_2_name.setText(self.players[1].player.full_name)

        # Set the players remaining scores
        self.ui.player_1_score.display(str(get_score_remaining(turn_1)))
        self.ui.player_2_score.display(str(get_score_remaining(turn_2)))

    def addpopulaterow(self, table, value, bounce, knock, foul, index):
        rowPosition = table.rowCount()
        table.insertRow(rowPosition)

        score = QTableWidgetItem()
        score.setTextAlignment(Qt.AlignCenter)
        score.setText(str(value))
        table.setItem(rowPosition, 0, score)

        cell_widget = QWidget()
        chk_bx = QCheckBox()
        if (bounce):
            chk_bx.setCheckState(Qt.Checked)
        else:
            chk_bx.setCheckState(Qt.Unchecked)
        layout = QHBoxLayout(cell_widget)
        layout.addWidget(chk_bx)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(layout)
        table.setCellWidget(rowPosition, 1, cell_widget)

        cell_widget = QWidget()
        chk_bx = QCheckBox()
        if (knock):
            chk_bx.setCheckState(Qt.Checked)
        else:
            chk_bx.setCheckState(Qt.Unchecked)
        layout = QHBoxLayout(cell_widget)
        layout.addWidget(chk_bx)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(layout)
        table.setCellWidget(rowPosition, 2, cell_widget)

        cell_widget = QWidget()
        chk_bx = QCheckBox()
        if (foul):
            chk_bx.setCheckState(Qt.Checked)
        else:
            chk_bx.setCheckState(Qt.Unchecked)
        layout = QHBoxLayout(cell_widget)
        layout.addWidget(chk_bx)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(layout)
        table.setCellWidget(rowPosition, 3, cell_widget)

    def dart_thrown(self, region, score, index):
        self.addpopulaterow(self.tables[0], str(score), False, False, False, index)
