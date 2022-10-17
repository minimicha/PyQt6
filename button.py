import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize, QPoint

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.centerWindow()
        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(50,50))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("green.png"), "green", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()
        toolbar.addSeparator()

        button_action2 = QAction(QIcon("red.png"), "red", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addSeparator()
        toolbar.addSeparator()

        button_action = QAction(QIcon("green.png"), "green2", self)
        button_action.setStatusTip("This is your button3")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))
        self.show()

    def centerWindow(self):
        frame_geometry = self.frameGeometry()
        #center_location = self.screen().availableGeometry().center()
        center_location = QPoint(1300,700)
        frame_geometry.moveCenter(center_location)
        self.move(frame_geometry.topLeft())

    def onMyToolBarButtonClick(self, signal):
        print("click", signal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
