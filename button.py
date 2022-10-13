import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt

class EmptyWindow(QWidget):

    def __init__(self):
        # constructor of empty class
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # set up application
        self.setGeometry(100, 100, 250, 150) # x, y, width, height
        self.setWindowTitle('instance created no matter how many windows/boxes we need')
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """ Create a button that changes text of a QLabel"""
        self.times_pressed = 0

        self.name_label = QLabel("Don't push the button",self)
        self.alignment = Qt.AlignmentFlag.AlignCenter
        self.name_label.setAlignment(self.alignment) # AlignRight,AlignHCenter, etc
        self.name_label.move(60, 30)

        self.button = QPushButton("Push Me", self) # reminder = inherits QWidget
        self.button.move(80, 70)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.times_pressed += 1
        if self.times_pressed == 1:
            self.name_label.setText("Why'd you press me?")
        elif self.times_pressed == 2:
            self.name_label.setText("I'm warning you.")
            self.button.setText("Don't...")
            self.button.adjustSize()
            self.button.move(80, 70)
        elif self.times_pressed == 3:
            print("The window has been closed.")
            self.close() # QWidget method close()


if __name__ == "__main__":
    app = QApplication(sys.argv) # instance created no matter how many windows/boxes we need
    window = EmptyWindow()
    sys.exit(app.exec())
