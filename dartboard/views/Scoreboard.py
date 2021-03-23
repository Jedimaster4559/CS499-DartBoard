# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Scoreboard.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DartboardViewer import DartboardViewer


class Ui_Scoreboard(object):
    def setupUi(self, Scoreboard):
        if not Scoreboard.objectName():
            Scoreboard.setObjectName(u"Scoreboard")
        Scoreboard.resize(1486, 838)
        self.centralwidget = QWidget(Scoreboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.player_2_name = QLabel(self.centralwidget)
        self.player_2_name.setObjectName(u"player_2_name")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_2_name.sizePolicy().hasHeightForWidth())
        self.player_2_name.setSizePolicy(sizePolicy)
        self.player_2_name.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.player_2_name.setFont(font)
        self.player_2_name.setLayoutDirection(Qt.LeftToRight)
        self.player_2_name.setStyleSheet(u"")
        self.player_2_name.setFrameShape(QFrame.StyledPanel)
        self.player_2_name.setFrameShadow(QFrame.Plain)
        self.player_2_name.setLineWidth(5)
        self.player_2_name.setMidLineWidth(1)
        self.player_2_name.setTextFormat(Qt.AutoText)
        self.player_2_name.setScaledContents(True)
        self.player_2_name.setAlignment(Qt.AlignCenter)
        self.player_2_name.setWordWrap(False)

        self.gridLayout.addWidget(self.player_2_name, 1, 4, 1, 1, Qt.AlignHCenter)

        self.player_1_score_table = QTableWidget(self.centralwidget)
        if (self.player_1_score_table.columnCount() < 3):
            self.player_1_score_table.setColumnCount(3)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.player_1_score_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setStyleStrategy(QFont.PreferAntialias)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.player_1_score_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.player_1_score_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.player_1_score_table.rowCount() < 4):
            self.player_1_score_table.setRowCount(4)
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setWeight(50)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        __qtablewidgetitem3.setBackground(QColor(161, 161, 161));
        self.player_1_score_table.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.player_1_score_table.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.player_1_score_table.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.player_1_score_table.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.player_1_score_table.setItem(1, 0, __qtablewidgetitem7)
        self.player_1_score_table.setObjectName(u"player_1_score_table")
        self.player_1_score_table.setMinimumSize(QSize(400, 0))
        self.player_1_score_table.setMaximumSize(QSize(200, 10000))
        self.player_1_score_table.setStyleSheet(u"gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.player_1_score_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.player_1_score_table.setAlternatingRowColors(True)
        self.player_1_score_table.setShowGrid(True)
        self.player_1_score_table.setGridStyle(Qt.SolidLine)
        self.player_1_score_table.horizontalHeader().setVisible(True)
        self.player_1_score_table.horizontalHeader().setCascadingSectionResizes(True)
        self.player_1_score_table.horizontalHeader().setMinimumSectionSize(100)
        self.player_1_score_table.horizontalHeader().setDefaultSectionSize(100)
        self.player_1_score_table.horizontalHeader().setHighlightSections(True)
        self.player_1_score_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.player_1_score_table.horizontalHeader().setStretchLastSection(False)
        self.player_1_score_table.verticalHeader().setVisible(False)
        self.player_1_score_table.verticalHeader().setCascadingSectionResizes(True)

        self.gridLayout.addWidget(self.player_1_score_table, 2, 0, 1, 1)

        self.player_1_score = QLCDNumber(self.centralwidget)
        self.player_1_score.setObjectName(u"player_1_score")
        font4 = QFont()
        font4.setPointSize(9)
        self.player_1_score.setFont(font4)
        self.player_1_score.setFrameShape(QFrame.StyledPanel)
        self.player_1_score.setFrameShadow(QFrame.Plain)
        self.player_1_score.setSmallDecimalPoint(False)
        self.player_1_score.setDigitCount(5)
        self.player_1_score.setMode(QLCDNumber.Dec)
        self.player_1_score.setSegmentStyle(QLCDNumber.Filled)
        self.player_1_score.setProperty("value", 501.000000000000000)

        self.gridLayout.addWidget(self.player_1_score, 3, 1, 1, 1)

        self.current_score = QLabel(self.centralwidget)
        self.current_score.setObjectName(u"current_score")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.current_score.sizePolicy().hasHeightForWidth())
        self.current_score.setSizePolicy(sizePolicy1)
        self.current_score.setMinimumSize(QSize(102, 100))
        self.current_score.setFont(font)
        self.current_score.setStyleSheet(u"")
        self.current_score.setFrameShape(QFrame.StyledPanel)
        self.current_score.setFrameShadow(QFrame.Plain)
        self.current_score.setLineWidth(5)
        self.current_score.setMidLineWidth(1)
        self.current_score.setTextFormat(Qt.AutoText)
        self.current_score.setScaledContents(True)
        self.current_score.setAlignment(Qt.AlignCenter)
        self.current_score.setWordWrap(False)

        self.gridLayout.addWidget(self.current_score, 3, 2, 1, 1)

        self.player_2_score = QLCDNumber(self.centralwidget)
        self.player_2_score.setObjectName(u"player_2_score")
        self.player_2_score.setFont(font4)
        self.player_2_score.setFrameShape(QFrame.StyledPanel)
        self.player_2_score.setFrameShadow(QFrame.Plain)
        self.player_2_score.setSmallDecimalPoint(False)
        self.player_2_score.setDigitCount(5)
        self.player_2_score.setMode(QLCDNumber.Dec)
        self.player_2_score.setSegmentStyle(QLCDNumber.Filled)
        self.player_2_score.setProperty("value", 501.000000000000000)

        self.gridLayout.addWidget(self.player_2_score, 3, 3, 1, 1)

        self.player_1_name = QLabel(self.centralwidget)
        self.player_1_name.setObjectName(u"player_1_name")
        sizePolicy1.setHeightForWidth(self.player_1_name.sizePolicy().hasHeightForWidth())
        self.player_1_name.setSizePolicy(sizePolicy1)
        self.player_1_name.setMaximumSize(QSize(200, 16777215))
        self.player_1_name.setFont(font)
        self.player_1_name.setLayoutDirection(Qt.LeftToRight)
        self.player_1_name.setStyleSheet(u"")
        self.player_1_name.setFrameShape(QFrame.StyledPanel)
        self.player_1_name.setFrameShadow(QFrame.Plain)
        self.player_1_name.setLineWidth(5)
        self.player_1_name.setMidLineWidth(1)
        self.player_1_name.setTextFormat(Qt.AutoText)
        self.player_1_name.setScaledContents(True)
        self.player_1_name.setAlignment(Qt.AlignCenter)
        self.player_1_name.setWordWrap(False)

        self.gridLayout.addWidget(self.player_1_name, 1, 0, 1, 1, Qt.AlignHCenter)

        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)
        self.title.setMinimumSize(QSize(380, 75))
        self.title.setFont(font)
        self.title.setStyleSheet(u"")
        self.title.setFrameShape(QFrame.StyledPanel)
        self.title.setFrameShadow(QFrame.Plain)
        self.title.setLineWidth(5)
        self.title.setMidLineWidth(1)
        self.title.setTextFormat(Qt.AutoText)
        self.title.setScaledContents(True)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(False)

        self.gridLayout.addWidget(self.title, 1, 2, 1, 1)

        self.player_1_score_table_2 = QTableWidget(self.centralwidget)
        if (self.player_1_score_table_2.columnCount() < 3):
            self.player_1_score_table_2.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.player_1_score_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
        self.player_1_score_table_2.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.player_1_score_table_2.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        if (self.player_1_score_table_2.rowCount() < 4):
            self.player_1_score_table_2.setRowCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font3);
        __qtablewidgetitem11.setBackground(QColor(161, 161, 161));
        self.player_1_score_table_2.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.player_1_score_table_2.setVerticalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.player_1_score_table_2.setVerticalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.player_1_score_table_2.setVerticalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.player_1_score_table_2.setItem(1, 0, __qtablewidgetitem15)
        self.player_1_score_table_2.setObjectName(u"player_1_score_table_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.player_1_score_table_2.sizePolicy().hasHeightForWidth())
        self.player_1_score_table_2.setSizePolicy(sizePolicy2)
        self.player_1_score_table_2.setMinimumSize(QSize(400, 0))
        self.player_1_score_table_2.setMaximumSize(QSize(400, 16777215))
        self.player_1_score_table_2.setLayoutDirection(Qt.LeftToRight)
        self.player_1_score_table_2.setStyleSheet(u"gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.player_1_score_table_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.player_1_score_table_2.setAlternatingRowColors(True)
        self.player_1_score_table_2.setShowGrid(True)
        self.player_1_score_table_2.setGridStyle(Qt.SolidLine)
        self.player_1_score_table_2.horizontalHeader().setVisible(True)
        self.player_1_score_table_2.horizontalHeader().setCascadingSectionResizes(True)
        self.player_1_score_table_2.horizontalHeader().setMinimumSectionSize(100)
        self.player_1_score_table_2.horizontalHeader().setDefaultSectionSize(100)
        self.player_1_score_table_2.horizontalHeader().setHighlightSections(True)
        self.player_1_score_table_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.player_1_score_table_2.horizontalHeader().setStretchLastSection(False)
        self.player_1_score_table_2.verticalHeader().setVisible(False)
        self.player_1_score_table_2.verticalHeader().setCascadingSectionResizes(True)
        self.player_1_score_table_2.verticalHeader().setMinimumSectionSize(23)
        self.player_1_score_table_2.verticalHeader().setDefaultSectionSize(30)
        self.player_1_score_table_2.verticalHeader().setProperty("showSortIndicator", False)

        self.gridLayout.addWidget(self.player_1_score_table_2, 2, 4, 1, 1)

        self.graphicsView = DartboardViewer(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 2, 1, 1, 3)

        Scoreboard.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Scoreboard)
        self.statusbar.setObjectName(u"statusbar")
        Scoreboard.setStatusBar(self.statusbar)

        self.retranslateUi(Scoreboard)

        QMetaObject.connectSlotsByName(Scoreboard)
    # setupUi

    def retranslateUi(self, Scoreboard):
        Scoreboard.setWindowTitle(QCoreApplication.translate("Scoreboard", u"MainWindow", None))
        self.player_2_name.setText(QCoreApplication.translate("Scoreboard", u"<Player 2 Name>", None))
        ___qtablewidgetitem = self.player_1_score_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Scoreboard", u"Dart #", None));
        ___qtablewidgetitem1 = self.player_1_score_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Scoreboard", u"Points", None));
        ___qtablewidgetitem2 = self.player_1_score_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Scoreboard", u"BKF", None));
        ___qtablewidgetitem3 = self.player_1_score_table.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Scoreboard", u"1", None));
        ___qtablewidgetitem4 = self.player_1_score_table.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Scoreboard", u"2", None));
        ___qtablewidgetitem5 = self.player_1_score_table.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Scoreboard", u"3", None));
        ___qtablewidgetitem6 = self.player_1_score_table.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Scoreboard", u"4", None));

        __sortingEnabled = self.player_1_score_table.isSortingEnabled()
        self.player_1_score_table.setSortingEnabled(False)
        self.player_1_score_table.setSortingEnabled(__sortingEnabled)

        self.current_score.setText(QCoreApplication.translate("Scoreboard", u"Current Score", None))
        self.player_1_name.setText(QCoreApplication.translate("Scoreboard", u"<Player 1 Name>", None))
        self.title.setText(QCoreApplication.translate("Scoreboard", u"English Premier Dart League", None))
        ___qtablewidgetitem7 = self.player_1_score_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Scoreboard", u"Dart #", None));
        ___qtablewidgetitem8 = self.player_1_score_table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Scoreboard", u"Points", None));
        ___qtablewidgetitem9 = self.player_1_score_table_2.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Scoreboard", u"BKF", None));
        ___qtablewidgetitem10 = self.player_1_score_table_2.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Scoreboard", u"1", None));
        ___qtablewidgetitem11 = self.player_1_score_table_2.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Scoreboard", u"2", None));
        ___qtablewidgetitem12 = self.player_1_score_table_2.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Scoreboard", u"3", None));
        ___qtablewidgetitem13 = self.player_1_score_table_2.verticalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Scoreboard", u"4", None));

        __sortingEnabled1 = self.player_1_score_table_2.isSortingEnabled()
        self.player_1_score_table_2.setSortingEnabled(False)
        self.player_1_score_table_2.setSortingEnabled(__sortingEnabled1)

    # retranslateUi

