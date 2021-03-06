from views.Scorer import Ui_Scorer
from PySide2.QtWidgets import QApplication, QMainWindow, QCheckBox, QTableWidgetItem, QWidget, QHBoxLayout, QHeaderView, QPushButton
from PySide2.QtCore import Qt
from backend.dartboard_api import *
import sys

class ScorerWindow(QMainWindow):
    def __init__(self, hub):
        super(ScorerWindow, self).__init__()

        self.hub = hub

        self.ui = Ui_Scorer()
        self.ui.setupUi(self)
        self.ui.graphicsView.setup_signal(self)
        self.ui.commit_turn_button.clicked.connect(self.commit_turn)
        
        self.current_set = 1
        self.current_leg = 1
        self.current_turns = [None, None]
        self.tables = [self.ui.Player1DartsTable, self.ui.Player2DartsTable]

        self.darts_thrown = {

        }
        
        
    def addpopulaterow(self, table, value, bounce, knock, foul, index):
        rowPosition = table.rowCount()
        table.insertRow(rowPosition)

        score = QTableWidgetItem()
        score.setTextAlignment(Qt.AlignCenter)
        score.setText(value)
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
        layout.setContentsMargins(0,0,0,0)
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
        layout.setContentsMargins(0,0,0,0)
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
        layout.setContentsMargins(0,0,0,0)
        cell_widget.setLayout(layout)
        table.setCellWidget(rowPosition, 3, cell_widget)

        cell_widget = QWidget()
        button = QPushButton("X")
        layout = QHBoxLayout(cell_widget)
        layout.addWidget(button)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0,0,0,0)
        cell_widget.setLayout(layout)
        table.setCellWidget(rowPosition, 4, cell_widget)
        button.clicked.connect(lambda: self.remove_dart_throw(score, index))

    def remove_dart_throw(self, item, index):
        self.tables[self.ui.tabWidget.currentIndex()].setCurrentItem(item)
        self.tables[self.ui.tabWidget.currentIndex()].selectRow(self.tables[self.ui.tabWidget.currentIndex()].currentRow())
        self.tables[self.ui.tabWidget.currentIndex()].removeRow(self.tables[self.ui.tabWidget.currentIndex()].currentRow())

        dart = self.darts_thrown.get(index)
        remove_hit(dart)
        
        self.ui.graphicsView.remove_dart(index)
        
    def enter_match_id(self, match_id):
        self.match = get_match_by_id(match_id)

        self.number_of_sets = self.match.best_of_sets_number
        self.number_of_legs = get_number_of_legs_by_match_id(match_id)

        self.players = get_players_by_match_id(match_id)

        # set names
        self.ui.tabWidget.setTabText(0, self.players[0].player.full_name)
        self.ui.tabWidget.setTabText(1, self.players[1].player.full_name)

        self.change_set_number_label(1)
        self.change_leg_number_label(1)

        leg = get_leg_by_number(match_id=match_id, set_number=1, leg_number=1)
        self.current_turns = [start_new_turn(leg, self.players[0]), start_new_turn(leg, self.players[1])]
            

    def change_set_number_label(self, current_set):
        result = str(current_set) + "/" + str(self.number_of_sets)
        self.current_set = current_set
        self.ui.SetNumberLabel.setText(result)

    def change_leg_number_label(self, current_leg):
        result = str(current_leg) + "/" + str(self.number_of_legs)
        self.current_leg = current_leg
        self.ui.LegNumberLabel.setText(result)

    def commit_turn(self):
        print("pressed commit turn")
        current_player_index = self.ui.tabWidget.currentIndex()
        isbust = not commit_turn(self.current_turns[current_player_index])

        if isbust:
            print("Player busted")
        else:
            print("Turn Committed")

        leg = get_leg_by_number(match_id=self.match.id, set_number=self.current_set, leg_number=self.current_leg)
        start_new_turn(leg, self.players[current_player_index])

    def dart_thrown(self, region, score, index):
        # print("Coming from Scorer: {}".format(msg))
        is_double = region == "double"
        is_triple = region == "triple"
        is_bullseye = region == "bullseye"

        current_player_index = self.ui.tabWidget.currentIndex()
        turn = self.current_turns[current_player_index]
        
        self.addpopulaterow(self.tables[current_player_index], str(score), False, False, False, index)

        dart = add_hit(turn=turn, value=score, is_double=is_double, is_triple=is_triple, is_bullseye=is_bullseye)

        self.darts_thrown[index] = dart

    def check_game_win(self):

        current_player_index = self.ui.tabWidget.currentIndex()
        turn = self.current_turns[current_player_index]

        opponent_turn = self.current_turns[(current_player_index+1) % 2]

        if (check_win(turn)):

            # leg is won everytime
            leg = get_leg_by_number(self.match.id, self.current_set, self.current_leg)
            add_leg_win(turn.player, opponent_turn, leg)


            # set is only won when number of legs won == number of legs
            if (turn.player.leg_wins == (self.number_of_legs // 2) + 1):

                set = get_set_by_number(self.match.id, self.current_set)
                add_set_win(turn.player, opponent_turn, set)

                


            if (self.current_set == self.number_of_sets and self.current_leg == self.number_of_legs):
                # add match win
            elif (self.current_set == self.number_of_sets):
                #
            elif (self.current_leg == self.number_of_legs):
                
                
                  
            
            self.current_set = get_set_by_number(self.match.id, self.current_set + 1).set_number
            self.current_leg = get_leg_by_number(self.match_id, self.current_leg + 1).leg_number

        

        

        
    
