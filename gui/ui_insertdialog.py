# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'insertdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(760, 360)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.desclabel = QLabel(Dialog)
        self.desclabel.setObjectName(u"desclabel")

        self.gridLayout.addWidget(self.desclabel, 1, 0, 1, 1)

        self.exlabel = QLabel(Dialog)
        self.exlabel.setObjectName(u"exlabel")

        self.gridLayout.addWidget(self.exlabel, 4, 0, 1, 1)

        self.comm = QLineEdit(Dialog)
        self.comm.setObjectName(u"comm")

        self.gridLayout.addWidget(self.comm, 6, 1, 1, 1)

        self.desc = QLineEdit(Dialog)
        self.desc.setObjectName(u"desc")

        self.gridLayout.addWidget(self.desc, 1, 1, 1, 1)

        self.complabel = QLabel(Dialog)
        self.complabel.setObjectName(u"complabel")

        self.gridLayout.addWidget(self.complabel, 2, 0, 1, 1)

        self.sidlabel = QLabel(Dialog)
        self.sidlabel.setObjectName(u"sidlabel")

        self.gridLayout.addWidget(self.sidlabel, 0, 0, 1, 1)

        self.voslabel = QLabel(Dialog)
        self.voslabel.setObjectName(u"voslabel")

        self.gridLayout.addWidget(self.voslabel, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exday = QComboBox(Dialog)
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.addItem("")
        self.exday.setObjectName(u"exday")

        self.horizontalLayout.addWidget(self.exday)

        self.exmonth = QComboBox(Dialog)
        self.exmonth.addItem("")
        self.exmonth.addItem("")
        self.exmonth.addItem("")
        self.exmonth.addItem("")
        self.exmonth.addItem("")
        self.exmonth.addItem("")
        self.exmonth.addItem("")
        self.exmonth.addItem("")
        self.exmonth.addItem("")
        self.exmonth.addItem("")
        self.exmonth.addItem("")
        self.exmonth.addItem("")
        self.exmonth.setObjectName(u"exmonth")

        self.horizontalLayout.addWidget(self.exmonth)

        self.exyear = QComboBox(Dialog)
        self.exyear.addItem("")
        self.exyear.addItem("")
        self.exyear.addItem("")
        self.exyear.addItem("")
        self.exyear.addItem("")
        self.exyear.addItem("")
        self.exyear.addItem("")
        self.exyear.addItem("")
        self.exyear.addItem("")
        self.exyear.addItem("")
        self.exyear.addItem("")
        self.exyear.setObjectName(u"exyear")

        self.horizontalLayout.addWidget(self.exyear)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)

        self.vollabel = QLabel(Dialog)
        self.vollabel.setObjectName(u"vollabel")

        self.gridLayout.addWidget(self.vollabel, 3, 0, 1, 1)

        self.commlabel = QLabel(Dialog)
        self.commlabel.setObjectName(u"commlabel")

        self.gridLayout.addWidget(self.commlabel, 6, 0, 1, 1)

        self.comp = QLineEdit(Dialog)
        self.comp.setObjectName(u"comp")

        self.gridLayout.addWidget(self.comp, 2, 1, 1, 1)

        self.sid = QLineEdit(Dialog)
        self.sid.setObjectName(u"sid")

        self.gridLayout.addWidget(self.sid, 0, 1, 1, 1)

        self.vol = QLineEdit(Dialog)
        self.vol.setObjectName(u"vol")

        self.gridLayout.addWidget(self.vol, 3, 1, 1, 1)

        self.pos = QCheckBox(Dialog)
        self.pos.setObjectName(u"pos")

        self.gridLayout.addWidget(self.pos, 7, 1, 1, 1)

        self.poslabel = QLabel(Dialog)
        self.poslabel.setObjectName(u"poslabel")

        self.gridLayout.addWidget(self.poslabel, 7, 0, 1, 1)

        self.vos = QComboBox(Dialog)
        self.vos.addItem("")
        self.vos.addItem("")
        self.vos.setObjectName(u"vos")

        self.gridLayout.addWidget(self.vos, 5, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok|QDialogButtonBox.Close)

        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.desclabel.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.exlabel.setText(QCoreApplication.translate("Dialog", u"Expiration Date", None))
        self.complabel.setText(QCoreApplication.translate("Dialog", u"Compound", None))
        self.sidlabel.setText(QCoreApplication.translate("Dialog", u"Sample ID", None))
        self.voslabel.setText(QCoreApplication.translate("Dialog", u"Vailidity", None))
        self.exday.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.exday.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.exday.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))
        self.exday.setItemText(3, QCoreApplication.translate("Dialog", u"4", None))
        self.exday.setItemText(4, QCoreApplication.translate("Dialog", u"5", None))
        self.exday.setItemText(5, QCoreApplication.translate("Dialog", u"6", None))
        self.exday.setItemText(6, QCoreApplication.translate("Dialog", u"7", None))
        self.exday.setItemText(7, QCoreApplication.translate("Dialog", u"8", None))
        self.exday.setItemText(8, QCoreApplication.translate("Dialog", u"9", None))
        self.exday.setItemText(9, QCoreApplication.translate("Dialog", u"10", None))
        self.exday.setItemText(10, QCoreApplication.translate("Dialog", u"11", None))
        self.exday.setItemText(11, QCoreApplication.translate("Dialog", u"12", None))
        self.exday.setItemText(12, QCoreApplication.translate("Dialog", u"13", None))
        self.exday.setItemText(13, QCoreApplication.translate("Dialog", u"14", None))
        self.exday.setItemText(14, QCoreApplication.translate("Dialog", u"15", None))
        self.exday.setItemText(15, QCoreApplication.translate("Dialog", u"16", None))
        self.exday.setItemText(16, QCoreApplication.translate("Dialog", u"17", None))
        self.exday.setItemText(17, QCoreApplication.translate("Dialog", u"18", None))
        self.exday.setItemText(18, QCoreApplication.translate("Dialog", u"19", None))
        self.exday.setItemText(19, QCoreApplication.translate("Dialog", u"20", None))
        self.exday.setItemText(20, QCoreApplication.translate("Dialog", u"21", None))
        self.exday.setItemText(21, QCoreApplication.translate("Dialog", u"22", None))
        self.exday.setItemText(22, QCoreApplication.translate("Dialog", u"23", None))
        self.exday.setItemText(23, QCoreApplication.translate("Dialog", u"24", None))
        self.exday.setItemText(24, QCoreApplication.translate("Dialog", u"25", None))
        self.exday.setItemText(25, QCoreApplication.translate("Dialog", u"26", None))
        self.exday.setItemText(26, QCoreApplication.translate("Dialog", u"27", None))
        self.exday.setItemText(27, QCoreApplication.translate("Dialog", u"28", None))
        self.exday.setItemText(28, QCoreApplication.translate("Dialog", u"29", None))
        self.exday.setItemText(29, QCoreApplication.translate("Dialog", u"30", None))
        self.exday.setItemText(30, QCoreApplication.translate("Dialog", u"31", None))

        self.exmonth.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.exmonth.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.exmonth.setItemText(2, QCoreApplication.translate("Dialog", u"3", None))
        self.exmonth.setItemText(3, QCoreApplication.translate("Dialog", u"4", None))
        self.exmonth.setItemText(4, QCoreApplication.translate("Dialog", u"5", None))
        self.exmonth.setItemText(5, QCoreApplication.translate("Dialog", u"6", None))
        self.exmonth.setItemText(6, QCoreApplication.translate("Dialog", u"7", None))
        self.exmonth.setItemText(7, QCoreApplication.translate("Dialog", u"8", None))
        self.exmonth.setItemText(8, QCoreApplication.translate("Dialog", u"9", None))
        self.exmonth.setItemText(9, QCoreApplication.translate("Dialog", u"10", None))
        self.exmonth.setItemText(10, QCoreApplication.translate("Dialog", u"11", None))
        self.exmonth.setItemText(11, QCoreApplication.translate("Dialog", u"12", None))

        self.exyear.setItemText(0, QCoreApplication.translate("Dialog", u"2023", None))
        self.exyear.setItemText(1, QCoreApplication.translate("Dialog", u"2024", None))
        self.exyear.setItemText(2, QCoreApplication.translate("Dialog", u"2025", None))
        self.exyear.setItemText(3, QCoreApplication.translate("Dialog", u"2026", None))
        self.exyear.setItemText(4, QCoreApplication.translate("Dialog", u"2027", None))
        self.exyear.setItemText(5, QCoreApplication.translate("Dialog", u"2028", None))
        self.exyear.setItemText(6, QCoreApplication.translate("Dialog", u"2029", None))
        self.exyear.setItemText(7, QCoreApplication.translate("Dialog", u"2030", None))
        self.exyear.setItemText(8, QCoreApplication.translate("Dialog", u"2031", None))
        self.exyear.setItemText(9, QCoreApplication.translate("Dialog", u"2032", None))
        self.exyear.setItemText(10, QCoreApplication.translate("Dialog", u"2033", None))

        self.vollabel.setText(QCoreApplication.translate("Dialog", u"Volume", None))
        self.commlabel.setText(QCoreApplication.translate("Dialog", u"Comment", None))
        self.pos.setText("")
        self.poslabel.setText(QCoreApplication.translate("Dialog", u"Part of Series", None))
        self.vos.setItemText(0, QCoreApplication.translate("Dialog", u"0", None))
        self.vos.setItemText(1, QCoreApplication.translate("Dialog", u"1", None))

    # retranslateUi

