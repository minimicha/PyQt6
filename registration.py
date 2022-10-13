from PyQt6.QtWidgets import QWidget

class NewUserWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI():
        self.setGeometry(100, 100, 340, 200)
        self.setWindowTitle("QMessageBox Example")
        self.LoginGUI()
        self.show()
