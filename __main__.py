import os, sys

from sqlalchemy.exc import OperationalError
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QAbstractItemView, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem

from gui.ui_mainwindow import Ui_MainWindow
from gui.ui_insertdialog import Ui_Dialog as Ui_InsertDialog
from gui.ui_seriesdialog import Ui_Dialog as Ui_SeriesDialog
from gui.ui_searchdialog import Ui_Dialog as Ui_SearchDialog
from gui.ui_seriesname import Ui_Dialog as Ui_SeriesName
from gui.ui_connectiondialog import Ui_Dialog as Ui_ConnectionDialog
#from gui.ui_settingsdialog import Ui_Dialog as Ui_SettingsDialog

from modules.sql import Samples, SQL
from modules.config import Settings
import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("InMaTo")

        self.ui.ibutton.clicked.connect(self.insert)
        self.ui.sbutton.clicked.connect(self.searchInterace)
        self.ui.rbutton.clicked.connect(self.update_table)

        self.ui.actionConnect.triggered.connect(self.connectSQL)
        self.ui.actionConnection_details.triggered.connect(self.connectionSettings)

        self.conf = Settings()

    def connectSQL(self):
        try:
            self.sql = SQL(os.environ["HOST"],
                           os.environ["PORT"],
                           os.environ["USER"],
                           os.environ["PASSWORD"],
                           os.environ["DATABASE"])
            self.sql.create_table()
            self.update_table()
        except OperationalError as err:
            Message(str(err), "There was an Error establishing a connection to the Database Server", "SQL-Error")

    def closeSQL(self):
        self.sql.session.close()
        self.sql.connection.close()
        del self.sql

    def insert(self):
        self.data = []
        dialog = InsertDialog()
        dialog.exec()
        self.data.append([dialog.ui.sid.text(),
                          dialog.ui.desc.text(),
                          dialog.ui.comp.text(),
                          dialog.ui.vol.text(),
                          dialog.ui.exday.currentText(),
                          dialog.ui.exmonth.currentText(),
                          dialog.ui.exyear.currentText(),
                          dialog.ui.vos.currentText(),
                          dialog.ui.comm.text()])
        print(self.data)

        if (dialog.ui.pos.isChecked() == True):
            dialog = SeriesName()
            dialog.exec()
            self.series_name = dialog.ui.sname.text()
            self.series()
        else:
            self.finalise()

    def finalise(self):
        if len(self.data) > 1:
            for i in range(len(self.data)):
                insert = Samples(sid=self.data[i][0],
                                 description=self.data[i][1],
                                 compound=self.data[i][2],
                                 volume=self.data[i][3],
                                 expiration_date=datetime.date(int(self.data[i][6]), int(self.data[i][5]), int(self.data[i][4])),
                                 validity=bool(int(self.data[i][7])),
                                 comment=self.data[i][8],
                                 series_name=self.series_name,
                                 series_id=i+1
                                 )
                self.sql.session.add(insert)
            self.sql.session.commit()
        else:
            i = 0
            insert = Samples(sid=self.data[i][0],
                             description=self.data[i][1],
                             compound=self.data[i][2],
                             volume=self.data[i][3],
                             expiration_date=datetime.date(int(self.data[i][6]), int(self.data[i][5]), int(self.data[i][4])),
                             validity=bool(int(self.data[i][7])),
                             comment=self.data[i][8]
                             )
            self.sql.session.add(insert)
            self.sql.session.commit()
        self.update_table()
        print(self.data)
        #print(self.data[0])
        #print(self.data[1])

    def series(self):
        dialog = SeriesDialog()
        dialog.ui.buttonBox.accepted.connect(lambda: self.data.append([dialog.ui.sid.text(),
                                                                       dialog.ui.desc.text(),
                                                                       dialog.ui.comp.text(),
                                                                       dialog.ui.vol.text(),
                                                                       dialog.ui.exday.currentText(),
                                                                       dialog.ui.exmonth.currentText(),
                                                                       dialog.ui.exyear.currentText(),
                                                                       dialog.ui.vos.currentText(),
                                                                       dialog.ui.comm.text()]))
        dialog.ui.buttonBox.accepted.connect(self.series)
        btn = dialog.ui.buttonBox.button(QDialogButtonBox.Apply)
        btn.clicked.connect(dialog.close)
        btn.clicked.connect(lambda: print("Fuck you"))
        btn.clicked.connect(lambda: self.data.append([dialog.ui.sid.text(),
                                                      dialog.ui.desc.text(),
                                                      dialog.ui.comp.text(),
                                                      dialog.ui.vol.text(),
                                                      dialog.ui.exday.currentText(),
                                                      dialog.ui.exmonth.currentText(),
                                                      dialog.ui.exyear.currentText(),
                                                      dialog.ui.vos.currentText(),
                                                      dialog.ui.comm.text()]))
        btn.clicked.connect(self.finalise)
        dialog.exec()


    def update_table(self):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['ID',
                                              'Sample ID',
                                              'Description',
                                              'Compound',
                                              'Volume',
                                              'Series Name',
                                              'Series ID',
                                              'VOS',
                                              'Expiration Date',
                                              'Comment',
                                              'TOR'])
        self.ui.table.setModel(self.model)
        self.ui.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        q = self.sql.session.query(Samples).all()
        for r in q:
            # Insert the text into the model
            row = self.model.rowCount()
            print(r.comment, r)
            self.model.insertRow(row, [QStandardItem(str(r.id)),
                                       QStandardItem(str(r.sid)),
                                       QStandardItem(str(r.description)),
                                       QStandardItem(str(r.compound)),
                                       QStandardItem(str(r.volume)),
                                       QStandardItem(str(r.series_name)),
                                       QStandardItem(str(r.series_id)),
                                       QStandardItem(str(r.validity)),
                                       QStandardItem(str(r.expiration_date)),
                                       QStandardItem(str(r.comment)),
                                       QStandardItem(str(r.timestamp))])

    def searchInterace(self):
        dialog = SearchDialog()
        dialog.ui.buttonBox.accepted.connect(lambda: self.search(dialog.ui.category.currentText(), dialog.ui.lineEdit.text()))
        dialog.exec()

    def search(self, category: str, search: str):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['ID',
                                          'Sample ID',
                                          'Description',
                                          'Compound',
                                          'Volume',
                                          'Series Name',
                                          'Series ID',
                                          'VOS',
                                          'Expiration Date',
                                          'Comment',
                                          'TOR'])
        self.ui.table.setModel(self.model)
        self.ui.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        q = self.sql.session.query(Samples).filter_by(sid=f"{search}").all()
        for r in q:
            # Insert the text into the model
            row = self.model.rowCount()
            print(r.comment, r)
            self.model.insertRow(row, [QStandardItem(str(r.id)),
                                       QStandardItem(str(r.sid)),
                                       QStandardItem(str(r.description)),
                                       QStandardItem(str(r.compound)),
                                       QStandardItem(str(r.volume)),
                                       QStandardItem(str(r.series_name)),
                                       QStandardItem(str(r.series_id)),
                                       QStandardItem(str(r.validity)),
                                       QStandardItem(str(r.expiration_date)),
                                       QStandardItem(str(r.comment)),
                                       QStandardItem(str(r.timestamp))])
            
    def Settings(self):
        dialog = SettingsDialog()
        dialog.exec()

    def connectionSettings(self):
        dialog = ConnectionDialog()
        dialog.ui.host.setText(os.environ['HOST'])
        dialog.ui.port.setText(os.environ['PORT'])
        dialog.ui.user.setText(os.environ['USER'])
        dialog.ui.password.setText(os.environ['PASSWORD'])
        dialog.ui.database.setText(os.environ['DATABASE'])
        dialog.ui.buttonBox.accepted.connect(lambda: self.change_settings(host=str(dialog.ui.host.text()),
                                                                          port=str(dialog.ui.port.text()),
                                                                          user=str(dialog.ui.user.text()),
                                                                          password=str(dialog.ui.password.text()),
                                                                          database=str(dialog.ui.database.text())))
        dialog.exec()

    def change_settings(self, host: str, port: str, user: str, password: str, database: str):
        if (bool(host) == True):
            self.conf.changeEntry('HOST', host)
        if (bool(port) == True):
            self.conf.changeEntry('PORT', port)
        if (bool(user) == True):
            self.conf.changeEntry('USER', user)
        if (bool(password) == True):
            self.conf.changeEntry('PASSWORD', password)
        if (bool(database) == True):
            self.conf.changeEntry('DATABASE', database)


class InsertDialog(QDialog):
    def __init__(self):
        super(InsertDialog, self).__init__()
        self.ui = Ui_InsertDialog()
        self.ui.setupUi(self)

class SeriesName(QDialog):
    def __init__(self):
        super(SeriesName, self).__init__()
        self.ui = Ui_SeriesName()
        self.ui.setupUi(self)

class SeriesDialog(QDialog):
    def __init__(self):
        super(SeriesDialog, self).__init__()
        self.ui = Ui_SeriesDialog()
        self.ui.setupUi(self)

class SearchDialog(QDialog):
    def __init__(self):
        super(SearchDialog, self).__init__()
        self.ui = Ui_SearchDialog()
        self.ui.setupUi(self)
        
#class SettingsDialog(QDialog):
#    def __init__(self):
#        super(SettingsDialog, self).__init__()
#        self.ui = Ui_SettingsDialog()
#        self.ui.setupUi(self)
        
class ConnectionDialog(QDialog):
    def __init__(self):
        super(ConnectionDialog, self).__init__()
        self.ui = Ui_ConnectionDialog()
        self.ui.setupUi(self)


class Message(QMessageBox):
    def __init__(self, text: str, info: str, title: str):
        super(Message, self).__init__()
        self.setIcon(QMessageBox.Information)
        self.setText(text)
        self.setInformativeText(info)
        self.setWindowTitle(title)
        self.setStandardButtons(QMessageBox.Ok)
        self.buttonClicked.connect(self.close)
        self.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()