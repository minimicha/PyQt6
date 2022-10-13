import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt
import time

class EmptyWindow(QWidget):

    def __init__(self):
        # constructor of empty class
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # set up application
        self.setMaximumSize(310, 130)
        # setMinimumSize() – Sets the widget’s minimum size
        # setFixedSize() – Sets the maximum and minimum sizes for the widget, preventing it from changing sizes
        self.setWindowTitle("QLineEdit Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.info_text = QLabel("Please enter your name bellow", self)
        self.info_text.move(70, 10)
        QLabel("Name:",self).move(20, 50)

        self.name_edit = QLineEdit(self)
        self.name_edit.resize(210,20)
        self.name_edit.move(70,50)
        self.name_edit.returnPressed.connect(self.ok_button_clicked)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.move(100, 100)
        self.clear_button.clicked.connect(self.clear_button_clicked)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.move(180, 100)
        self.ok_button.clicked.connect(self.ok_button_clicked)

    def clear_button_clicked(self):
        self.name_edit.clear()

    def ok_button_clicked(self):
        if len(self.name_edit.text()) <= 10:
            self.info_text.setText("Query invalid. Try again please")
            self.clear_button_clicked()

        elif len(self.name_edit.text()) > 10:
            print(self.name_edit.text())
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv) # instance created no matter how many windows/boxes we need
    window = EmptyWindow()
    sys.exit(app.exec())
