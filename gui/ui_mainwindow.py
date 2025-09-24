# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1115, 677)
        self.actionExport_data = QAction(MainWindow)
        self.actionExport_data.setObjectName(u"actionExport_data")
        self.actionConnection_details = QAction(MainWindow)
        self.actionConnection_details.setObjectName(u"actionConnection_details")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ibutton = QPushButton(self.centralwidget)
        self.ibutton.setObjectName(u"ibutton")

        self.verticalLayout.addWidget(self.ibutton)

        self.sbutton = QPushButton(self.centralwidget)
        self.sbutton.setObjectName(u"sbutton")

        self.verticalLayout.addWidget(self.sbutton)

        self.rbutton = QPushButton(self.centralwidget)
        self.rbutton.setObjectName(u"rbutton")

        self.verticalLayout.addWidget(self.rbutton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.table = QTableView(self.centralwidget)
        self.table.setObjectName(u"table")

        self.gridLayout.addWidget(self.table, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1115, 23))
        self.menuData = QMenu(self.menubar)
        self.menuData.setObjectName(u"menuData")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuSQL = QMenu(self.menubar)
        self.menuSQL.setObjectName(u"menuSQL")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSQL.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuData.addAction(self.actionExport_data)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuSQL.addAction(self.actionConnect)
        self.menuSQL.addAction(self.actionConnection_details)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExport_data.setText(QCoreApplication.translate("MainWindow", u"Export data", None))
        self.actionConnection_details.setText(QCoreApplication.translate("MainWindow", u"Connection details", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.ibutton.setText(QCoreApplication.translate("MainWindow", u"Insert Data", None))
        self.sbutton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.rbutton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.menuData.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuSQL.setTitle(QCoreApplication.translate("MainWindow", u"SQL", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

