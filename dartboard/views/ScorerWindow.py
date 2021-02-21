from views.Scorer import Ui_Scorer
from PySide2.QtWidgets import QApplication, QMainWindow, QCheckBox, QTableWidgetItem, QWidget, QHBoxLayout, QHeaderView, QPushButton
from PySide2.QtCore import Qt
from backend.dartboard_api import get_match_by_id, get_players_by_match_id, get_number_of_legs_by_match_id
import sys

class ScorerWindow(QMainWindow):
    def __init__(self, hub):
        super(ScorerWindow, self).__init__()

        self.hub = hub

        self.ui = Ui_Scorer()
        self.ui.setupUi(self)
        self.ui.graphicsView.setup_signal(self)
        self.ui.commit_turn_button.clicked.connect(self.commit_turn)

        header = self.ui.Player1DartsTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QHeaderView.Stretch)

        self.addpopulaterow(self.ui.Player1DartsTable, "50", True, False, False)
        self.addpopulaterow(self.ui.Player1DartsTable, "100", True, False, False)

        
        
    def addpopulaterow(self, table, value, bounce, knock, foul):
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
        button.clicked.connect(lambda: self.remove_dart_throw(rowPosition))

    def remove_dart_throw(self, row):
        print(row)
        

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

    def commit_turn(self):
        print("pressed commit turn")
        

        

        
    
