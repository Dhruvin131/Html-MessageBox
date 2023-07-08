import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import htmlReporter
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
import os


class HTMLReportGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('HTML Report Generator')
        self.setGeometry(300, 300, 300, 200)

        generate_button = QPushButton('Generate HTML Report', self)
        generate_button.setGeometry(50, 50, 200, 50)
        generate_button.clicked.connect(self.generateReport)

        self.show()

    def generateReport(self):
        # Add your code to generate the HTML report here
        QMessageBox.information(self, 'Title1', "Text")
        QMessageBox.information(self, 'Title2', "Text")
        QMessageBox.information(self, 'Title3', "Text")
        # htmlReporter.genHtml(self)
        print("HTML report generated.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    report_generator = HTMLReportGenerator()
    sys.exit(app.exec_())
