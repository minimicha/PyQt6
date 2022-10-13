import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QLineEdit
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
        self.setWindowTitle("QCheckBox Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        header_label = QLabel("Which shift works for you ?", self)
        header_label.setWordWrap(True)
        header_label.move(20,10)

        morning_shift = QCheckBox("Morning shift", self)
        morning_shift.move(40,60)
        morning_shift.toggle()
        morning_shift.toggled.connect(self.printSelected) # different from the clicked with QPushButton

        day_shift = QCheckBox("Day shift", self)
        day_shift.move(60, 80)
        day_shift.toggled.connect(self.printSelected) # toggle also passes additional information

        night_shift = QCheckBox("Day shift", self)
        night_shift.move(80, 100)
        night_shift.toggled.connect(self.printSelected)

    def printSelected(self, checked):
        sender = self.sender() # QObject method returns which object is sending signal
        if checked:
            print(f"{sender.text()} Selected.") # getter
        else:
            print(f"{sender.text()} Deselected.")


if __name__ == "__main__":
    app = QApplication(sys.argv) # instance created no matter how many windows/boxes we need
    window = EmptyWindow()
    sys.exit(app.exec())
