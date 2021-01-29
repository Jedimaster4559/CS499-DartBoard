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
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.graphicsView = DartboardView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.graphicsView)

        Scorer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Scorer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 719, 21))
        Scorer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Scorer)
        self.statusbar.setObjectName(u"statusbar")
        Scorer.setStatusBar(self.statusbar)

        self.retranslateUi(Scorer)

        QMetaObject.connectSlotsByName(Scorer)
    # setupUi

    def retranslateUi(self, Scorer):
        Scorer.setWindowTitle(QCoreApplication.translate("Scorer", u"MainWindow", None))
    # retranslateUi

