# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ManagePlayers.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ManagePlayers(object):
    def setupUi(self, ManagePlayers):
        if not ManagePlayers.objectName():
            ManagePlayers.setObjectName(u"ManagePlayers")
        ManagePlayers.resize(800, 600)
        self.centralwidget = QWidget(ManagePlayers)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(616, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.new_player_button = QPushButton(self.centralwidget)
        self.new_player_button.setObjectName(u"new_player_button")

        self.gridLayout.addWidget(self.new_player_button, 0, 2, 1, 1)

        self.players_listwidget = QListWidget(self.centralwidget)
        self.players_listwidget.setObjectName(u"players_listwidget")

        self.gridLayout.addWidget(self.players_listwidget, 1, 0, 1, 3)

        self.return_button = QPushButton(self.centralwidget)
        self.return_button.setObjectName(u"return_button")

        self.gridLayout.addWidget(self.return_button, 2, 2, 1, 1)

        ManagePlayers.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ManagePlayers)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        ManagePlayers.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ManagePlayers)
        self.statusbar.setObjectName(u"statusbar")
        ManagePlayers.setStatusBar(self.statusbar)

        self.retranslateUi(ManagePlayers)

        QMetaObject.connectSlotsByName(ManagePlayers)
    # setupUi

    def retranslateUi(self, ManagePlayers):
        ManagePlayers.setWindowTitle(QCoreApplication.translate("ManagePlayers", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("ManagePlayers", u"Manage Players", None))
        self.new_player_button.setText(QCoreApplication.translate("ManagePlayers", u"New Player", None))
        self.return_button.setText(QCoreApplication.translate("ManagePlayers", u"Back", None))
    # retranslateUi

