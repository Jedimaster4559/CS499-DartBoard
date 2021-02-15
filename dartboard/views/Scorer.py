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
        Scorer.resize(719, 527)
        self.centralwidget = QWidget(Scorer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.NextLegButton = QPushButton(self.centralwidget)
        self.NextLegButton.setObjectName(u"NextLegButton")

        self.gridLayout.addWidget(self.NextLegButton, 3, 2, 1, 1)

        self.PreviousLegButton = QPushButton(self.centralwidget)
        self.PreviousLegButton.setObjectName(u"PreviousLegButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PreviousLegButton.sizePolicy().hasHeightForWidth())
        self.PreviousLegButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.PreviousLegButton, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 3, 1, 1)

        self.NextSetButton = QPushButton(self.centralwidget)
        self.NextSetButton.setObjectName(u"NextSetButton")

        self.gridLayout.addWidget(self.NextSetButton, 3, 5, 1, 1)

        self.EndMatchButton = QPushButton(self.centralwidget)
        self.EndMatchButton.setObjectName(u"EndMatchButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.EndMatchButton.sizePolicy().hasHeightForWidth())
        self.EndMatchButton.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.EndMatchButton, 5, 3, 1, 1)

        self.SetNumberLabel = QLabel(self.centralwidget)
        self.SetNumberLabel.setObjectName(u"SetNumberLabel")

        self.gridLayout.addWidget(self.SetNumberLabel, 2, 4, 1, 2, Qt.AlignHCenter)

        self.LegNumberLabel = QLabel(self.centralwidget)
        self.LegNumberLabel.setObjectName(u"LegNumberLabel")

        self.gridLayout.addWidget(self.LegNumberLabel, 2, 1, 1, 2, Qt.AlignHCenter)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.Player1Tab = QWidget()
        self.Player1Tab.setObjectName(u"Player1Tab")
        self.gridLayout_2 = QGridLayout(self.Player1Tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Player1DartsTable = QTableWidget(self.Player1Tab)
        if (self.Player1DartsTable.columnCount() < 3):
            self.Player1DartsTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.Player1DartsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Player1DartsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Player1DartsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.Player1DartsTable.setObjectName(u"Player1DartsTable")
        self.Player1DartsTable.setColumnCount(3)
        self.Player1DartsTable.horizontalHeader().setStretchLastSection(False)
        self.Player1DartsTable.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.Player1DartsTable, 0, 1, 1, 1)

        self.tabWidget.addTab(self.Player1Tab, "")
        self.Player2Tab = QWidget()
        self.Player2Tab.setObjectName(u"Player2Tab")
        self.gridLayout_3 = QGridLayout(self.Player2Tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Player1DartsTable_2 = QTableWidget(self.Player2Tab)
        if (self.Player1DartsTable_2.columnCount() < 3):
            self.Player1DartsTable_2.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Player1DartsTable_2.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Player1DartsTable_2.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Player1DartsTable_2.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.Player1DartsTable_2.setObjectName(u"Player1DartsTable_2")
        self.Player1DartsTable_2.setColumnCount(3)
        self.Player1DartsTable_2.horizontalHeader().setStretchLastSection(False)
        self.Player1DartsTable_2.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.Player1DartsTable_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Player2Tab, "")

        self.gridLayout.addWidget(self.tabWidget, 4, 1, 1, 5)

        self.PreviousSetButton = QPushButton(self.centralwidget)
        self.PreviousSetButton.setObjectName(u"PreviousSetButton")

        self.gridLayout.addWidget(self.PreviousSetButton, 3, 4, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 2, Qt.AlignHCenter)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 2, Qt.AlignHCenter)

        self.graphicsView = DartboardView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(300, 300))

        self.gridLayout.addWidget(self.graphicsView, 0, 0, 6, 1)

        Scorer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Scorer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 719, 21))
        Scorer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Scorer)
        self.statusbar.setObjectName(u"statusbar")
        Scorer.setStatusBar(self.statusbar)

        self.retranslateUi(Scorer)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Scorer)
    # setupUi

    def retranslateUi(self, Scorer):
        Scorer.setWindowTitle(QCoreApplication.translate("Scorer", u"MainWindow", None))
        self.NextLegButton.setText(QCoreApplication.translate("Scorer", u">", None))
        self.PreviousLegButton.setText(QCoreApplication.translate("Scorer", u"<", None))
        self.NextSetButton.setText(QCoreApplication.translate("Scorer", u">", None))
        self.EndMatchButton.setText(QCoreApplication.translate("Scorer", u"End Match", None))
        self.SetNumberLabel.setText(QCoreApplication.translate("Scorer", u"2/4", None))
        self.LegNumberLabel.setText(QCoreApplication.translate("Scorer", u"4/14", None))
        ___qtablewidgetitem = self.Player1DartsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Scorer", u"Score", None));
        ___qtablewidgetitem1 = self.Player1DartsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Scorer", u"Dart Number", None));
        ___qtablewidgetitem2 = self.Player1DartsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Scorer", u"BKF", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Player1Tab), QCoreApplication.translate("Scorer", u"Player 1", None))
        ___qtablewidgetitem3 = self.Player1DartsTable_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Scorer", u"Score", None));
        ___qtablewidgetitem4 = self.Player1DartsTable_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Scorer", u"Dart Number", None));
        ___qtablewidgetitem5 = self.Player1DartsTable_2.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Scorer", u"BKF", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Player2Tab), QCoreApplication.translate("Scorer", u"Player 2", None))
        self.PreviousSetButton.setText(QCoreApplication.translate("Scorer", u"<", None))
        self.label_2.setText(QCoreApplication.translate("Scorer", u"Sets", None))
        self.label.setText(QCoreApplication.translate("Scorer", u"Legs", None))
    # retranslateUi

