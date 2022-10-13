import sys, os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QMessageBox , QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import time

class EmptyWindow(QWidget):

    def __init__(self):
        # constructor of empty class
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # set up application
        self.setGeometry(100, 100, 340, 140)
        self.setWindowTitle("QMessageBox Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        # modal dialogs => user can't use interface until this is closed
        # modeless dialogs => user can interect with both dialog & rest of app
        header = QLabel("Author Catalogue", self)
        header.setFont(QFont("Arial", 18))
        header.move(40,10)

        author_text = QLabel("Name:", self)
        author_text.move(10,40)

        self.author_edit = QLineEdit(self)
        self.author_edit.resize(210,20)
        self.author_edit.move(50,40)
        self.author_edit.setPlaceholderText("First Last")

        self.button = QPushButton('Search', self)
        self.button.move(40, 100)
        self.button.clicked.connect(self.search_button)

    def search_button(self):
        path = str(os.getcwd()) + "/file/authors.txt"
        print(path)
        try:
            with open(path, 'r') as file:
                authors = [line.rstrip('\n') for line in file]
            if self.author_edit.text() in authors:
                QMessageBox.information(
                    self,
                    "Author Found",
                    "We found the name in cat.",
                    QMessageBox.StandardButton.Ok
                    )
            else:
                answer = QMessageBox.question(
                    self,
                    "Author not found",
                    """<p>Author not found in catalogue.</p><p>Do you wish to continue?</p>""",
                    QMessageBox.StandardButton.Yes,
                    QMessageBox.StandardButton.No
                    )
                if answer == QMessageBox.StandardButton.No:
                    print('Closing app.')
                    self.close()

        except FileNotFoundError as error:
            QMessageBox.warning(
                self,
                "Error",
                f"""<p>File not found.</p><p>Error:{error}</p>Closing application.""",
                QMessageBox.StandardButton.Ok)
            self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv) # instance created no matter how many windows/boxes we need
    window = EmptyWindow()
    sys.exit(app.exec())
