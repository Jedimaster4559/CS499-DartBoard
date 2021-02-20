from views.Scorer import Ui_Scorer
from PySide2.QtWidgets import QApplication, QMainWindow
from backend.dartboard_api import get_match_by_id
import sys

class ScorerWindow(QMainWindow):
    def __init__(self, hub):
        super(ScorerWindow, self).__init__()

        self.hub = hub

        self.ui = Ui_Scorer()
        self.ui.setupUi(self)

    def enter_match_id(self, match_id):
        match = get_match_by_id(match_id)

        number_of_sets = match.best_of_sets_number
        print(number_of_sets)

        # set names
        self.ui.tabWidget.setTabText(0, "Player 1 Name")
        self.ui.tabWidget.setTabText(1, "Player 2 Name")

    def set_leg_number_label(self):
        self.ui.LegNumberLabel.setText("")

        

        
    
