import sys
from PyQt5.QtWidgets import QApplication, QMessageBox


def show_message_box(title, text):
    # app = QApplication(sys.argv)

    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(text)
    msg_box.exec_()

    # sys.exit(app.exec_())

if __name__ == "__main__":

    # Example usage:
    show_message_box("Information", "This is a sample message.")

