# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Scorer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DartboardView import DartboardView


class Ui_Scorer(object):
    def setupUi(self, Scorer):
        if not Scorer.objectName():
            Scorer.setObjectName(u"Scorer")
        Scorer.resize(723, 527)
        self.actionMatch_Averages = QAction(Scorer)
        self.actionMatch_Averages.setObjectName(u"actionMatch_Averages")
        self.actionMatch_Score_Stats = QAction(Scorer)
        self.actionMatch_Score_Stats.setObjectName(u"actionMatch_Score_Stats")
        self.actionMatch_Highest_Out = QAction(Scorer)
        self.actionMatch_Highest_Out.setObjectName(u"actionMatch_Highest_Out")
        self.action_Match_Statistics = QAction(Scorer)
        self.action_Match_Statistics.setObjectName(u"action_Match_Statistics")
        self.actionMatch_Averages_2 = QAction(Scorer)
        self.actionMatch_Averages_2.setObjectName(u"actionMatch_Averages_2")
        self.actionMatch_Score_Stats_2 = QAction(Scorer)
        self.actionMatch_Score_Stats_2.setObjectName(u"actionMatch_Score_Stats_2")
        self.actionMatch_Highest_Out_2 = QAction(Scorer)
        self.actionMatch_Highest_Out_2.setObjectName(u"actionMatch_Highest_Out_2")
        self.actionMatch_Doubles_Triples = QAction(Scorer)
        self.actionMatch_Doubles_Triples.setObjectName(u"actionMatch_Doubles_Triples")
        self.actionPlayer_Ranks = QAction(Scorer)
        self.actionPlayer_Ranks.setObjectName(u"actionPlayer_Ranks")
        self.actionPlayer_Last_Win = QAction(Scorer)
        self.actionPlayer_Last_Win.setObjectName(u"actionPlayer_Last_Win")
        self.actionPlayer_Averages = QAction(Scorer)
        self.actionPlayer_Averages.setObjectName(u"actionPlayer_Averages")
        self.actionPlayer_Score_Stats = QAction(Scorer)
        self.actionPlayer_Score_Stats.setObjectName(u"actionPlayer_Score_Stats")
        self.centralwidget = QWidget(Scorer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 2, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 5, 2, 1, 3)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.Player1Tab = QWidget()
        self.Player1Tab.setObjectName(u"Player1Tab")
        self.gridLayout_2 = QGridLayout(self.Player1Tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Player1DartsTable = QTableWidget(self.Player1Tab)
        if (self.Player1DartsTable.columnCount() < 5):
            self.Player1DartsTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.Player1DartsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Player1DartsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Player1DartsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Player1DartsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Player1DartsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.Player1DartsTable.setObjectName(u"Player1DartsTable")
        self.Player1DartsTable.setColumnCount(5)
        self.Player1DartsTable.horizontalHeader().setDefaultSectionSize(75)
        self.Player1DartsTable.horizontalHeader().setStretchLastSection(False)
        self.Player1DartsTable.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.Player1DartsTable, 0, 1, 1, 1)

        self.tabWidget.addTab(self.Player1Tab, "")
        self.Player2Tab = QWidget()
        self.Player2Tab.setObjectName(u"Player2Tab")
        self.gridLayout_3 = QGridLayout(self.Player2Tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Player2DartsTable = QTableWidget(self.Player2Tab)
        if (self.Player2DartsTable.columnCount() < 5):
            self.Player2DartsTable.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Player2DartsTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Player2DartsTable.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Player2DartsTable.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Player2DartsTable.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Player2DartsTable.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.Player2DartsTable.setObjectName(u"Player2DartsTable")
        self.Player2DartsTable.setColumnCount(5)
        self.Player2DartsTable.horizontalHeader().setDefaultSectionSize(75)
        self.Player2DartsTable.horizontalHeader().setStretchLastSection(False)
        self.Player2DartsTable.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.Player2DartsTable, 0, 0, 1, 3)

        self.tabWidget.addTab(self.Player2Tab, "")

        self.gridLayout.addWidget(self.tabWidget, 4, 1, 1, 5)

        self.LegNumberLabel = QLabel(self.centralwidget)
        self.LegNumberLabel.setObjectName(u"LegNumberLabel")

        self.gridLayout.addWidget(self.LegNumberLabel, 2, 1, 1, 2, Qt.AlignHCenter)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 2, Qt.AlignHCenter)

        self.graphicsView = DartboardView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(300, 300))

        self.gridLayout.addWidget(self.graphicsView, 0, 0, 6, 1)

        self.SetNumberLabel = QLabel(self.centralwidget)
        self.SetNumberLabel.setObjectName(u"SetNumberLabel")

        self.gridLayout.addWidget(self.SetNumberLabel, 2, 4, 1, 2, Qt.AlignHCenter)

        self.commit_turn_button = QPushButton(self.centralwidget)
        self.commit_turn_button.setObjectName(u"commit_turn_button")

        self.gridLayout.addWidget(self.commit_turn_button, 5, 1, 1, 1)

        self.EndMatchButton = QPushButton(self.centralwidget)
        self.EndMatchButton.setObjectName(u"EndMatchButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.EndMatchButton.sizePolicy().hasHeightForWidth())
        self.EndMatchButton.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.EndMatchButton, 5, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(215, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        Scorer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Scorer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 723, 21))
        self.menuScoreboard_View = QMenu(self.menubar)
        self.menuScoreboard_View.setObjectName(u"menuScoreboard_View")
        Scorer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Scorer)
        self.statusbar.setObjectName(u"statusbar")
        Scorer.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuScoreboard_View.menuAction())
        self.menuScoreboard_View.addAction(self.actionMatch_Averages_2)
        self.menuScoreboard_View.addAction(self.actionMatch_Score_Stats_2)
        self.menuScoreboard_View.addAction(self.actionMatch_Highest_Out_2)
        self.menuScoreboard_View.addAction(self.actionMatch_Doubles_Triples)
        self.menuScoreboard_View.addSeparator()
        self.menuScoreboard_View.addAction(self.actionPlayer_Ranks)
        self.menuScoreboard_View.addAction(self.actionPlayer_Last_Win)
        self.menuScoreboard_View.addAction(self.actionPlayer_Averages)
        self.menuScoreboard_View.addAction(self.actionPlayer_Score_Stats)

        self.retranslateUi(Scorer)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Scorer)
    # setupUi

    def retranslateUi(self, Scorer):
        Scorer.setWindowTitle(QCoreApplication.translate("Scorer", u"MainWindow", None))
        self.actionMatch_Averages.setText(QCoreApplication.translate("Scorer", u"Match Averages", None))
        self.actionMatch_Score_Stats.setText(QCoreApplication.translate("Scorer", u"Match Score Stats", None))
        self.actionMatch_Highest_Out.setText(QCoreApplication.translate("Scorer", u"Match Highest Out", None))
        self.action_Match_Statistics.setText(QCoreApplication.translate("Scorer", u"-- Match Statistics --", None))
        self.actionMatch_Averages_2.setText(QCoreApplication.translate("Scorer", u"Match Averages", None))
        self.actionMatch_Score_Stats_2.setText(QCoreApplication.translate("Scorer", u"Match Score Stats", None))
        self.actionMatch_Highest_Out_2.setText(QCoreApplication.translate("Scorer", u"Match Highest Out", None))
        self.actionMatch_Doubles_Triples.setText(QCoreApplication.translate("Scorer", u"Match Doubles/Triples", None))
        self.actionPlayer_Ranks.setText(QCoreApplication.translate("Scorer", u"Player Ranks", None))
        self.actionPlayer_Last_Win.setText(QCoreApplication.translate("Scorer", u"Player Last Win", None))
        self.actionPlayer_Averages.setText(QCoreApplication.translate("Scorer", u"Player Averages", None))
        self.actionPlayer_Score_Stats.setText(QCoreApplication.translate("Scorer", u"Player Score Stats", None))
        self.label.setText(QCoreApplication.translate("Scorer", u"Legs", None))
        ___qtablewidgetitem = self.Player1DartsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Scorer", u"Score", None));
        ___qtablewidgetitem1 = self.Player1DartsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Scorer", u"Bounce Out", None));
        ___qtablewidgetitem2 = self.Player1DartsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Scorer", u"Knock Out", None));
        ___qtablewidgetitem3 = self.Player1DartsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Scorer", u"Foul", None));
        ___qtablewidgetitem4 = self.Player1DartsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Scorer", u"Remove", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Player1Tab), QCoreApplication.translate("Scorer", u"Player 1", None))
        ___qtablewidgetitem5 = self.Player2DartsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Scorer", u"Score", None));
        ___qtablewidgetitem6 = self.Player2DartsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Scorer", u"Bounce Out", None));
        ___qtablewidgetitem7 = self.Player2DartsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Scorer", u"Knock Out", None));
        ___qtablewidgetitem8 = self.Player2DartsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Scorer", u"Foul", None));
        ___qtablewidgetitem9 = self.Player2DartsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Scorer", u"Remove", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Player2Tab), QCoreApplication.translate("Scorer", u"Player 2", None))
        self.LegNumberLabel.setText(QCoreApplication.translate("Scorer", u"4/14", None))
        self.label_2.setText(QCoreApplication.translate("Scorer", u"Sets", None))
        self.SetNumberLabel.setText(QCoreApplication.translate("Scorer", u"2/4", None))
        self.commit_turn_button.setText(QCoreApplication.translate("Scorer", u"Commit Turn", None))
        self.EndMatchButton.setText(QCoreApplication.translate("Scorer", u"End Match", None))
        self.menuScoreboard_View.setTitle(QCoreApplication.translate("Scorer", u"Scoreboard View", None))
    # retranslateUi

