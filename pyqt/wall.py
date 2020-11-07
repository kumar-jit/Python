#http://www.brunningonline.net/simon/blog/archives/winDesktop.py.html


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import time
import threading
import DesktopWallpaper
import win32api, win32con, win32gui
import Userinformetion
import multiprocessing as mp

def foo():
    print("work")


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.applyflag=0
        Userinformetion.setpath()  #set the path
        self.timelist=[0.15,0.5,1,2,5,10,30,60,1440] #time list

        self.indexNumberofCombobox=2 #combobox index number store

        self.path=""  #store path 
        
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedHeight(600)
        MainWindow.setFixedWidth(670)
        MainWindow.setWindowIcon(QtGui.QIcon(r'img\thms.png'))

        #lebel for display image
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.currentimageLable = QtWidgets.QLabel(self.centralwidget)
        self.currentimageLable.setGeometry(QtCore.QRect(60, 40, 551, 311))
        self.currentimageLable.setObjectName("currentimageLable")
        t=threading.Thread(target=self.deskImg)
        t.daemon=True
        t.start()
        
        

        # Folderpath TextBox
        self.folderpath = QtWidgets.QLineEdit(self.centralwidget)
        self.folderpath.setGeometry(QtCore.QRect(60, 440, 281, 21))
        self.folderpath.setObjectName("folderpath")
        self.folderpath.setText(DesktopWallpaper.Read_last_location())
        self.path=self.folderpath.text()

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
        self.timeComboBox.setItemText(0, _translate("Mainwindow", "10 Secoend"))
        self.timeComboBox.setItemText(1, _translate("Mainwindow", "30 Secoend"))
        self.timeComboBox.setItemText(2, _translate("Mainwindow", "1 Minute"))
        self.timeComboBox.setItemText(3, _translate("Mainwindow", "2 Minute"))
        self.timeComboBox.setItemText(4, _translate("Mainwindow", "5 Minute"))
        self.timeComboBox.setItemText(5, _translate("Mainwindow", "10 Minute"))
        self.timeComboBox.setItemText(6, _translate("Mainwindow", "30 Minute"))
        self.timeComboBox.setItemText(7, _translate("Mainwindow", "1 Hour"))
        self.timeComboBox.setItemText(8, _translate("Mainwindow", "24 Hour"))

        self.suffilecheckBox.setText(_translate("Mainwindow", "Suffile"))

        self.applyButton.setText(_translate("Mainwindow", "Apply"))



    # ------- Browes button function  for get file path from user------
    def BrowsePath(self):
        getpath=self.folderpath.text()
        self.folderpath.setText(QFileDialog.getExistingDirectory(None,"Select a Folder",getpath))
        self.path=self.folderpath.text()
        
        #DesktopWallpaper.Write_last_location(self.path)
        # QtWidgets.QFileDialog.getExistingDirectoryUrl(self,"open file",r"C:\Users\kumar\OneDrive\Pictures\Saved Pictures")
    

    
    #----------Apply Push Button function--------
    def ApplyButton(self):

        if self.applyflag==0:
            
            
            self.indexNumberofCombobox=self.timeComboBox.currentIndex()
            t=self.timelist[self.indexNumberofCombobox]*60
            self.p = mp.Process(target=DesktopWallpaper.changeDeskWall, args=(self.path,t,self.suffilecheckBox.isChecked(),))
            self.p.daemon=True
            self.applyflag +=1
            self.p.start()


            # t1=mp.Process(target=self.ApplyButtonFunctionCall,args=())
            # self.t1.daemon=True
            # self.t1=threading.Thread(target=self.ApplyButtonFunctionCall) #creat thread and call function
            #t1.start()

        else:
            self.p.kill()
            self.indexNumberofCombobox=self.timeComboBox.currentIndex()
            t=self.timelist[self.indexNumberofCombobox]*60
            print(self.indexNumberofCombobox)
            print(t)
            self.p = mp.Process(target=DesktopWallpaper.changeDeskWall, args=(self.path,5,self.suffilecheckBox.isChecked(),))
            self.p.daemon=True
            self.p.start()
            
            # self.t1.kill()
            # self.t1=threading.Thread(target=self.ApplyButtonFunctionCall) #creat thread and call function
            # self.t1.daemon=True
            # self.t1.start()
        DesktopWallpaper.Write_last_location(self.folderpath.text())


        #--------display current desktop wallpaper--------
    def deskImg(self):
        t3=threading.Thread(target=self.displaywall)
        t3.daemon=True
        t3.start()

    def displaywall(self):
        while True:
            try:
                time.sleep(0.5)
                current_desktopImagePath=DesktopWallpaper.GetCurrentDesktopImage()
                self.DesktopImage = QtGui.QPixmap(current_desktopImagePath)
                self.pixmap=self.DesktopImage.scaled(551, 311)
                self.currentimageLable.setPixmap(self.pixmap)
            except:
                time.sleep(1)
            
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
