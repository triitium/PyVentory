# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 182)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 130, 581, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 621, 101))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.category = QComboBox(self.gridLayoutWidget)
        self.category.addItem("")
        self.category.addItem("")
        self.category.addItem("")
        self.category.addItem("")
        self.category.addItem("")
        self.category.addItem("")
        self.category.addItem("")
        self.category.addItem("")
        self.category.setObjectName(u"category")

        self.gridLayout.addWidget(self.category, 0, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.category.setItemText(0, QCoreApplication.translate("Dialog", u"Sample ID", None))
        self.category.setItemText(1, QCoreApplication.translate("Dialog", u"Description", None))
        self.category.setItemText(2, QCoreApplication.translate("Dialog", u"Compound", None))
        self.category.setItemText(3, QCoreApplication.translate("Dialog", u"Expiration Date", None))
        self.category.setItemText(4, QCoreApplication.translate("Dialog", u"Validity", None))
        self.category.setItemText(5, QCoreApplication.translate("Dialog", u"Series Name", None))
        self.category.setItemText(6, QCoreApplication.translate("Dialog", u"Date", None))
        self.category.setItemText(7, QCoreApplication.translate("Dialog", u"Comment", None))

    # retranslateUi

