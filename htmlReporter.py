import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
import os
from pubsubManager import PubSubManager
import time

def genHtml(self):
    counter = 1
    while True:
        # mess = QMessageBox()
        # mess.setWindowTitle("title1")
        # mess.setText("this is text")
        # mess.setInformativeText("infog taxt")
        # x = mess.exec_()
        # QMessageBox.information(self, 'Title1', "Text")
        self.timer_updated.emit(f"Count {counter}", "mymsg")
        # PubSubManager.send_message("ShowMessage", title="This is a title 1", text = "This is  a text 1")
        counter += 1
        os.startfile("Report.html")
        time.sleep(5)
        # mess = QMessageBox()
        # mess.setWindowTitle("title2")
        # mess.setText("this is text")
        # mess.setInformativeText("infog taxt")
        # x = mess.exec_()
        # QMessageBox.information(self, 'Title1', "Text")
        self.timer_updated.emit(f"Count {counter}", "mymsg")
        # PubSubManager.send_message("ShowMessage", title="This is a title 1", text = "This is  a text 1")
        counter += 1
        os.startfile("test.html")
        time.sleep(5)
        # mess = QMessageBox()
        # mess.setWindowTitle("title3")
        # mess.setText("this is text")
        # mess.setInformativeText("infog taxt")
        # x = mess.exec_() 
        # QMessageBox.information(self, 'Title1', "Text")
