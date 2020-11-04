
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mainwindow(object):
    def setupUi(self, Mainwindow):
        Mainwindow.setObjectName("Mainwindow")
        Mainwindow.setEnabled(True)
        Mainwindow.resize(652, 611)
        Mainwindow.setFocusPolicy(QtCore.Qt.TabFocus)
        Mainwindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

        self.centralwidget = QtWidgets.QWidget(Mainwindow)
        self.centralwidget.setObjectName("centralwidget")

#           desktop image 
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 561, 321))
        self.label.setObjectName("label")
        self.label.setPixmap(QtGui.QPixmap(r"C:\Users\kumar\OneDrive\Documents\python\pyqt\dog.jpg"))
        #%AppData%\Microsoft\Windows\Themes\TranscodedWallpaper

#           folder path
        self.folderpath = QtWidgets.QLineEdit(self.centralwidget)
        self.folderpath.setGeometry(QtCore.QRect(60, 429, 281, 21))
        self.folderpath.setObjectName("folderpath")
#       pushbutton brows
        self.BrowesFolder = QtWidgets.QPushButton(self.centralwidget)
        self.BrowesFolder.setGeometry(QtCore.QRect(60, 390, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BrowesFolder.setFont(font)
        self.BrowesFolder.setObjectName("BrowesFolder")
        


#           timetabble lable
        self.Timelable = QtWidgets.QLabel(self.centralwidget)
        self.Timelable.setGeometry(QtCore.QRect(450, 390, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Timelable.setFont(font)
        self.Timelable.setObjectName("Timelable")
#           time tible combobox
        self.timeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.timeComboBox.setGeometry(QtCore.QRect(450, 430, 131, 22))
        self.timeComboBox.setObjectName("timeComboBox")
        self.timeComboBox.addItem("")
        self.timeComboBox.addItem("")
        self.timeComboBox.addItem("")
        self.timeComboBox.addItem("")
        self.timeComboBox.addItem("")
        self.timeComboBox.addItem("")
        self.timeComboBox.addItem("")

#           check box
        self.suffilecheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.suffilecheckBox.setGeometry(QtCore.QRect(60, 480, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.suffilecheckBox.setFont(font)
        self.suffilecheckBox.setObjectName("suffilecheckBox")

#           pushbutton for
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setGeometry(QtCore.QRect(260, 520, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.applyButton.setFont(font)
        self.applyButton.setObjectName("applyButton")



        Mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Mainwindow)
        self.statusbar.setObjectName("statusbar")
        Mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(Mainwindow)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)


        self.applyButton.clicked.connect(self.click)

    def retranslateUi(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow.setWindowTitle(_translate("Mainwindow", "DeskTop WallPaper"))
        self.BrowesFolder.setText(_translate("Mainwindow", "Browes"))
        self.Timelable.setText(_translate("Mainwindow", "Time"))

        self.timeComboBox.setItemText(0, _translate("Mainwindow", "1 Minute"))
        self.timeComboBox.setItemText(1, _translate("Mainwindow", "2 Minute"))
        self.timeComboBox.setItemText(2, _translate("Mainwindow", "5 Minute"))
        self.timeComboBox.setItemText(3, _translate("Mainwindow", "10 Minute"))
        self.timeComboBox.setItemText(4, _translate("Mainwindow", "30 Minute"))
        self.timeComboBox.setItemText(5, _translate("Mainwindow", "1 Hour"))
        self.timeComboBox.setItemText(6, _translate("Mainwindow", "24 Hour"))

        self.suffilecheckBox.setText(_translate("Mainwindow", "Suffile"))

        self.applyButton.setText(_translate("Mainwindow", "Apply"))
    
#       Pushbutton Browsfolder  function
    def click(self):
        #path=QtWidgets.QFileDialog.getExistingDirectory()
        print("hello")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = QtWidgets.QMainWindow()
    ui = Ui_Mainwindow()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())
