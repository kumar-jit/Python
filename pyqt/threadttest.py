#!/usr/bin/python
# Standard Lib
from datetime import datetime
import logging
import os
import random
import sys
import time
# Third Party
from PyQt5 import QtGui, QtCore



class SSITesterThread(QtCore.QThread):
    # vars for updating gui using signals
    updateText = QtCore.pyqtSignal(str)
    updateColor = QtCore.pyqtSignal(str)
    updateSN = QtCore.pyqtSignal(str)
    def __init__(self, thread_number, port, path, parent=None):
        super(SSITesterThread, self).__init__(parent)
        self.delay = random.random()
    def run(self):
        self.ssitester()
    def ssitester(self):
        print("hello")



class SSITestSuiteGUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        self._threads = []
        QtGui.QWidget.__init__(self, parent)
        # Init class from template and paths
        self.launch_tester_threads()

    def init_gui_nodes(self, com_ports_list):
        for num, port, in zip(range(1, 25), range(0, 24)):
            label = getattr(self.ui, 'com_{}'.format(num))
            label.setText("COM Port: {}".format(com_ports_list[port]["COM"]))

    def launch_tester_threads(self):
        logging.info("Spinning up threads...")
        for num, com_port_chunk in zip(range(1, 25), self.com_ports_list):
            tester_thread = SSITesterThread(thread_number=num, port=com_port_chunk["COM"], path=self.vc_test_path)
            # get a reference to the associated textbox somehow...
            status_box = getattr(self.ui, 'status_{}'.format(num))
            tester_thread.updateText.connect(status_box.setText)
            status_box = getattr(self.ui, 'status_{}'.format(num))
            tester_thread.updateColor.connect(status_box.setStyleSheet)
            sn_label = getattr(self.ui, 'sn_{}'.format(num))
            tester_thread.updateSN.connect(sn_label.setText)
            sn_label.setText("S/N: None")
            tester_thread.start()
            self._threads.append(tester_thread)
        logging.info("Ready for tests.")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    test_suite = SSITestSuiteGUI()
    test_suite.show()
    # Close app only when window is closed.
    sys.exit(app.exec_())