import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QObject
import os
from threading import Thread
import htmlReporter
import messageBox
# -------------------------------------------
# ! Try adding Signaling to html generator
# -----------------------------------------
# from pubsubManager import PubSubManager

class TimerThread(QObject):
    timer_updated = pyqtSignal(str, str)

    # def run(self):
    #     counter = 0
    #     while True:
    #         counter += 1
    #         if counter % 5 == 0:  # Show message every 5 seconds
    #             # self.timer_updated.emit(counter)
    #             # os.startfile("Report.html")
    #             htmlReporter.genHtml(self)
    #             print(f"Signal Emitted with Timer value {counter}")
    #         self.msleep(1000)  # Sleep for 1 second

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Timer App')
        self.setGeometry(300, 300, 300, 200)

        self.timer_label = QLabel(self)
        self.timer_label.setGeometry(50, 20, 200, 50)
        self.updateTimerLabel(0)

        start_button = QPushButton('Start Timer', self)
        start_button.clicked.connect(self.startTimerThread)
        start_button.setGeometry(50, 80, 200, 50)

        message_button = QPushButton('Show Message', self)
        # message_button.clicked.connect(self.showMessage)
        message_button.setGeometry(50, 140, 200, 50)
        # PubSubManager.subscribe("ShowMessage", messageBox.show_message_box)
        self.show()

    def startTimerThread(self):
        self.timer_thread = TimerThread()
        self.timer_thread.timer_updated.connect(messageBox.show_message_box)
        myT = Thread(target=htmlReporter.genHtml, args=[self.timer_thread])
        myT.start()

        pass
        # htmlReporter.genHtml(self.timer_thread)

        # self.timer_thread.timer_updated.connect(self.showPopupMessage)
        # self.timer_thread.start()

    def updateTimerLabel(self, value):
        self.timer_label.setText(f'Timer Value: {value}')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer_app = TimerApp()
    sys.exit(app.exec_())
