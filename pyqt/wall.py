


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import ctypes
import time
import threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.timelist=[1,2,5,10,30,60,1440] #time list

        self.indexNumberofCombobox=2 #combobox index number store

        self.path=""  #store path 
        
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)

        #lebel for display image
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.currentimageLable = QtWidgets.QLabel(self.centralwidget)
        self.currentimageLable.setGeometry(QtCore.QRect(70, 40, 551, 311))
        self.currentimageLable.setObjectName("currentimageLable")
        self.deskImg() 
        
        

        # Folderpath TextBox
        self.folderpath = QtWidgets.QLineEdit(self.centralwidget)
        self.folderpath.setGeometry(QtCore.QRect(60, 440, 281, 21))
        self.folderpath.setObjectName("folderpath")
        # Browse button
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(60, 410, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")
        self.browseButton.clicked.connect(self.BrowsePath) #callfunction

#           time lable
        self.Timelable = QtWidgets.QLabel(self.centralwidget)
        self.Timelable.setGeometry(QtCore.QRect(450, 406, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Timelable.setFont(font)
        self.Timelable.setObjectName("Timelable")
#           time combobox
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

#           check box for suffle
        self.suffilecheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.suffilecheckBox.setGeometry(QtCore.QRect(60, 480, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.suffilecheckBox.setFont(font)
        self.suffilecheckBox.setObjectName("suffilecheckBox")

#           pushbutton for apply
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setGeometry(QtCore.QRect(260, 520, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.applyButton.setFont(font)
        self.applyButton.setObjectName("applyButton")
        self.applyButton.clicked.connect(self.ApplyButton) #connect method

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wallpaper"))
        
        self.browseButton.setText(_translate("MainWindow", "Browse"))
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

    # ------- Browes button function  for get file path from user------
    def BrowsePath(self):
        self.path=QtWidgets.QFileDialog.getExistingDirectory()
        self.folderpath.setText(self.path)
    
    #----------Apply Push Button function--------
    def ApplyButton(self):
        self.indexNumberofCombobox=self.timeComboBox.currentIndex()
        os.chdir(self.path)
        images=os.listdir()
        for i in range(len(images)):
            #t=self.timelist[self.indexNumberofCombobox]*60
            try:
                name,extesion=os.path.splitext(images[i])
                if extesion in [".JPEG",".jpeg",".PNG",".png",".jpg",".JPG"]:
                    absolutepath = self.path+ "\\" + images[i]
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, absolutepath , 0)
                    time.sleep(10)
            except Exception as e:
                print(e)

    #----------Get current desktop wallpaper---
    def GetCurrentDesktopImage(self):
        gopath=os.path.expandvars(r"%AppData%\Microsoft\Windows\Themes\CachedFiles")
        os.chdir(gopath)
        listofImage=os.listdir()
        imagepath= f"{gopath}\{listofImage[0]}"
        return (imagepath)

#--------display current desktop wallpaper--------
    def deskImg(self):
        self.current_desktopImagePath=self.GetCurrentDesktopImage()
        self.DesktopImage = QtGui.QPixmap(self.current_desktopImagePath)
        self.pixmap=self.DesktopImage.scaled(551, 311)
        self.currentimageLable.setPixmap(self.pixmap)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
