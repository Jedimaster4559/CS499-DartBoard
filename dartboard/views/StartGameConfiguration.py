# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StartGameConfiguration.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StartGameConfiguration(object):
    def setupUi(self, StartGameConfiguration):
        if not StartGameConfiguration.objectName():
            StartGameConfiguration.setObjectName(u"StartGameConfiguration")
        StartGameConfiguration.resize(400, 600)
        self.centralwidget = QWidget(StartGameConfiguration)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 7)

        self.lifetime_avg_checkbox = QCheckBox(self.centralwidget)
        self.lifetime_avg_checkbox.setObjectName(u"lifetime_avg_checkbox")

        self.gridLayout.addWidget(self.lifetime_avg_checkbox, 16, 3, 1, 1, Qt.AlignLeft)

        self.last_champ_win_checkbox = QCheckBox(self.centralwidget)
        self.last_champ_win_checkbox.setObjectName(u"last_champ_win_checkbox")

        self.gridLayout.addWidget(self.last_champ_win_checkbox, 15, 4, 1, 1, Qt.AlignLeft)

        self.league_rank_checkbox = QCheckBox(self.centralwidget)
        self.league_rank_checkbox.setObjectName(u"league_rank_checkbox")

        self.gridLayout.addWidget(self.league_rank_checkbox, 15, 2, 1, 1, Qt.AlignLeft)

        self.last_match_win_checkbox = QCheckBox(self.centralwidget)
        self.last_match_win_checkbox.setObjectName(u"last_match_win_checkbox")

        self.gridLayout.addWidget(self.last_match_win_checkbox, 15, 3, 1, 1, Qt.AlignLeft)

        self.season_180s_checkbox = QCheckBox(self.centralwidget)
        self.season_180s_checkbox.setObjectName(u"season_180s_checkbox")

        self.gridLayout.addWidget(self.season_180s_checkbox, 16, 4, 1, 1, Qt.AlignLeft)

        self.number_of_sets_spin_box = QSpinBox(self.centralwidget)
        self.number_of_sets_spin_box.setObjectName(u"number_of_sets_spin_box")

        self.gridLayout.addWidget(self.number_of_sets_spin_box, 11, 4, 1, 2)

        self.player_two_combo_box = QComboBox(self.centralwidget)
        self.player_two_combo_box.setObjectName(u"player_two_combo_box")
        self.player_two_combo_box.setEditable(True)

        self.gridLayout.addWidget(self.player_two_combo_box, 3, 0, 1, 7)

        self.leg_value_301_radio_button = QRadioButton(self.centralwidget)
        self.leg_value_301_radio_button.setObjectName(u"leg_value_301_radio_button")

        self.gridLayout.addWidget(self.leg_value_301_radio_button, 13, 4, 1, 1, Qt.AlignHCenter)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_4, 10, 1, 1, 2)

        self.season_avg_checkbox = QCheckBox(self.centralwidget)
        self.season_avg_checkbox.setObjectName(u"season_avg_checkbox")

        self.gridLayout.addWidget(self.season_avg_checkbox, 16, 2, 1, 1, Qt.AlignLeft)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 7)

        self.location_line_edit = QLineEdit(self.centralwidget)
        self.location_line_edit.setObjectName(u"location_line_edit")

        self.gridLayout.addWidget(self.location_line_edit, 7, 0, 1, 7)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_5, 10, 4, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 17, 3, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 7)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 7)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 14, 3, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.player_one_combo_box = QComboBox(self.centralwidget)
        self.player_one_combo_box.setObjectName(u"player_one_combo_box")
        self.player_one_combo_box.setEditable(True)

        self.gridLayout.addWidget(self.player_one_combo_box, 1, 0, 1, 7)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_6, 12, 2, 1, 3)

        self.start_game_button = QPushButton(self.centralwidget)
        self.start_game_button.setObjectName(u"start_game_button")

        self.gridLayout.addWidget(self.start_game_button, 18, 3, 1, 1)

        self.leg_value_801_radio_button = QRadioButton(self.centralwidget)
        self.leg_value_801_radio_button.setObjectName(u"leg_value_801_radio_button")

        self.gridLayout.addWidget(self.leg_value_801_radio_button, 13, 2, 1, 1, Qt.AlignHCenter)

        self.date_edit = QDateEdit(self.centralwidget)
        self.date_edit.setObjectName(u"date_edit")

        self.gridLayout.addWidget(self.date_edit, 9, 0, 1, 7)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 7)

        self.number_of_legs_spin_box = QSpinBox(self.centralwidget)
        self.number_of_legs_spin_box.setObjectName(u"number_of_legs_spin_box")

        self.gridLayout.addWidget(self.number_of_legs_spin_box, 11, 1, 1, 2)

        self.leg_value_501_radio_button = QRadioButton(self.centralwidget)
        self.leg_value_501_radio_button.setObjectName(u"leg_value_501_radio_button")

        self.gridLayout.addWidget(self.leg_value_501_radio_button, 13, 3, 1, 1, Qt.AlignHCenter)

        self.official_names_line_edit = QLineEdit(self.centralwidget)
        self.official_names_line_edit.setObjectName(u"official_names_line_edit")

        self.gridLayout.addWidget(self.official_names_line_edit, 5, 0, 1, 7)

        StartGameConfiguration.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(StartGameConfiguration)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 21))
        StartGameConfiguration.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(StartGameConfiguration)
        self.statusbar.setObjectName(u"statusbar")
        StartGameConfiguration.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.location_line_edit, self.date_edit)
        QWidget.setTabOrder(self.date_edit, self.number_of_legs_spin_box)
        QWidget.setTabOrder(self.number_of_legs_spin_box, self.number_of_sets_spin_box)
        QWidget.setTabOrder(self.number_of_sets_spin_box, self.leg_value_801_radio_button)
        QWidget.setTabOrder(self.leg_value_801_radio_button, self.leg_value_501_radio_button)
        QWidget.setTabOrder(self.leg_value_501_radio_button, self.leg_value_301_radio_button)
        QWidget.setTabOrder(self.leg_value_301_radio_button, self.league_rank_checkbox)
        QWidget.setTabOrder(self.league_rank_checkbox, self.last_match_win_checkbox)
        QWidget.setTabOrder(self.last_match_win_checkbox, self.last_champ_win_checkbox)
        QWidget.setTabOrder(self.last_champ_win_checkbox, self.season_avg_checkbox)
        QWidget.setTabOrder(self.season_avg_checkbox, self.lifetime_avg_checkbox)
        QWidget.setTabOrder(self.lifetime_avg_checkbox, self.season_180s_checkbox)

        self.retranslateUi(StartGameConfiguration)

        QMetaObject.connectSlotsByName(StartGameConfiguration)
    # setupUi

    def retranslateUi(self, StartGameConfiguration):
        StartGameConfiguration.setWindowTitle(QCoreApplication.translate("StartGameConfiguration", u"Start Game Configuration", None))
        self.label_9.setText(QCoreApplication.translate("StartGameConfiguration", u"Official Names", None))
        self.lifetime_avg_checkbox.setText(QCoreApplication.translate("StartGameConfiguration", u"Lifetime Average", None))
        self.last_champ_win_checkbox.setText(QCoreApplication.translate("StartGameConfiguration", u"Last Champ Win", None))
        self.league_rank_checkbox.setText(QCoreApplication.translate("StartGameConfiguration", u"League Rank", None))
        self.last_match_win_checkbox.setText(QCoreApplication.translate("StartGameConfiguration", u"Last Match Win", None))
        self.season_180s_checkbox.setText(QCoreApplication.translate("StartGameConfiguration", u"Season 180s", None))
        self.leg_value_301_radio_button.setText(QCoreApplication.translate("StartGameConfiguration", u"301", None))
        self.label_4.setText(QCoreApplication.translate("StartGameConfiguration", u"Number of Legs", None))
        self.season_avg_checkbox.setText(QCoreApplication.translate("StartGameConfiguration", u"Season Average", None))
        self.label_2.setText(QCoreApplication.translate("StartGameConfiguration", u"Player 2 Name", None))
        self.label_5.setText(QCoreApplication.translate("StartGameConfiguration", u"Number of Matches", None))
        self.label_8.setText(QCoreApplication.translate("StartGameConfiguration", u"Date", None))
        self.label_3.setText(QCoreApplication.translate("StartGameConfiguration", u"Location", None))
        self.label_7.setText(QCoreApplication.translate("StartGameConfiguration", u"Starting Stats Display", None))
        self.label_6.setText(QCoreApplication.translate("StartGameConfiguration", u"Scoring Leg Value", None))
        self.start_game_button.setText(QCoreApplication.translate("StartGameConfiguration", u"Start Game", None))
        self.leg_value_801_radio_button.setText(QCoreApplication.translate("StartGameConfiguration", u"801", None))
        self.label.setText(QCoreApplication.translate("StartGameConfiguration", u"Player 1 Name", None))
        self.leg_value_501_radio_button.setText(QCoreApplication.translate("StartGameConfiguration", u"501", None))
    # retranslateUi

