from ScorerWindow import ScorerWindow
from StartMenuWindow import StartMenuWindow
from StartGameConfigurationWindow import StartGameConfigurationWindow
from PySide2.QtWidgets import QApplication, QMainWindow
import sys

class Hub():
    def __init__(self):


        self.start_menu = StartMenuWindow(self)
        self.start_menu.show()

        self.scorer = ScorerWindow(self)
        #self.scorer.show()

        self.start_game_configuration = StartGameConfigurationWindow(self)
        #self.start_game_configuration.show()

    #add functions and high level things here

    def navigate_to_view(self, name):
        if (name == "start_menu"):
            self.start_menu.show()
        elif (name == "start_game_configuration"):
            self.start_game_configuration.show()
        elif (name == "scorer"):
            self.scorer.show()
