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


class Ui_Scoreboard(object):
    def setupUi(self, Scoreboard):
        if not Scoreboard.objectName():
            Scoreboard.setObjectName(u"Scoreboard")
        Scoreboard.resize(1543, 838)
        self.centralwidget = QWidget(Scoreboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"")
        self.label_3.setFrameShape(QFrame.StyledPanel)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setLineWidth(5)
        self.label_3.setMidLineWidth(1)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(False)

        self.gridLayout.addWidget(self.label_3, 1, 4, 1, 1, Qt.AlignHCenter)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setStyleStrategy(QFont.PreferAntialias)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setWeight(50)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        __qtablewidgetitem3.setBackground(QColor(161, 161, 161));
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(400, 0))
        self.tableWidget.setMaximumSize(QSize(200, 10000))
        self.tableWidget.setStyleSheet(u"gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)

        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)

        self.lcdNumber_2 = QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        font4 = QFont()
        font4.setPointSize(9)
        self.lcdNumber_2.setFont(font4)
        self.lcdNumber_2.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber_2.setFrameShadow(QFrame.Plain)
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setDigitCount(5)
        self.lcdNumber_2.setMode(QLCDNumber.Dec)
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber_2.setProperty("value", 501.000000000000000)

        self.gridLayout.addWidget(self.lcdNumber_2, 3, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(102, 100))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"")
        self.label_4.setFrameShape(QFrame.StyledPanel)
        self.label_4.setFrameShadow(QFrame.Plain)
        self.label_4.setLineWidth(5)
        self.label_4.setMidLineWidth(1)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(False)

        self.gridLayout.addWidget(self.label_4, 3, 2, 1, 1)

        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setFont(font4)
        self.lcdNumber.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber.setFrameShadow(QFrame.Plain)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setMode(QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 501.000000000000000)

        self.gridLayout.addWidget(self.lcdNumber, 3, 3, 1, 1)

        self.columnView = QColumnView(self.centralwidget)
        self.columnView.setObjectName(u"columnView")
        self.columnView.setMinimumSize(QSize(0, 0))
        self.columnView.setMaximumSize(QSize(1000000, 16777215))

        self.gridLayout.addWidget(self.columnView, 2, 1, 1, 3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(200, 16777215))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"")
        self.label_2.setFrameShape(QFrame.StyledPanel)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setLineWidth(5)
        self.label_2.setMidLineWidth(1)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(380, 75))
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setFrameShape(QFrame.StyledPanel)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setLineWidth(5)
        self.label.setMidLineWidth(1)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        self.tableWidget_2 = QTableWidget(self.centralwidget)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        if (self.tableWidget_2.rowCount() < 4):
            self.tableWidget_2.setRowCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font3);
        __qtablewidgetitem11.setBackground(QColor(161, 161, 161));
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem15)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy2)
        self.tableWidget_2.setMinimumSize(QSize(400, 0))
        self.tableWidget_2.setMaximumSize(QSize(400, 16777215))
        self.tableWidget_2.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_2.setStyleSheet(u"gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", False)

        self.gridLayout.addWidget(self.tableWidget_2, 2, 4, 1, 1)

        Scoreboard.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Scoreboard)
        self.statusbar.setObjectName(u"statusbar")
        Scoreboard.setStatusBar(self.statusbar)

        self.retranslateUi(Scoreboard)

        QMetaObject.connectSlotsByName(Scoreboard)
    # setupUi

    def retranslateUi(self, Scoreboard):
        Scoreboard.setWindowTitle(QCoreApplication.translate("Scoreboard", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("Scoreboard", u"<Player 2 Name>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Scoreboard", u"Dart #", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Scoreboard", u"Points", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Scoreboard", u"BKF", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Scoreboard", u"1", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Scoreboard", u"2", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Scoreboard", u"3", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Scoreboard", u"4", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_4.setText(QCoreApplication.translate("Scoreboard", u"Current Score", None))
        self.label_2.setText(QCoreApplication.translate("Scoreboard", u"<Player 1 Name>", None))
        self.label.setText(QCoreApplication.translate("Scoreboard", u"English Premier Dart League", None))
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Scoreboard", u"Dart #", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Scoreboard", u"Points", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Scoreboard", u"BKF", None));
        ___qtablewidgetitem10 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Scoreboard", u"1", None));
        ___qtablewidgetitem11 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Scoreboard", u"2", None));
        ___qtablewidgetitem12 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Scoreboard", u"3", None));
        ___qtablewidgetitem13 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Scoreboard", u"4", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

    # retranslateUi

