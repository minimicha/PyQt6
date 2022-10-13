import sys, os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QCheckBox, QMessageBox
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
from registration import NewUserWindow

class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setFixedSize(300, 150)
        self.setWindowTitle("3.1 - Login GUI")
        self.LoginGUI()
        self.show()

    def LoginGUI(self):
        """Create and arrange widgets in the main window."""
        self.login_is_successful = False

        header_text = QLabel("Login", self)
        header_text.setFont(QFont("Calibri", 15))
        header_text.move(80,10)

        QLabel("Username:", self).move(5,40)
        self.user_edit = QLineEdit(self)
        self.user_edit.resize(210,20)
        self.user_edit.move(80,40)

        QLabel("Password:", self).move(5,70)
        self.pass_edit = QLineEdit(self)
        self.pass_edit.setEchoMode(QLineEdit.EchoMode.Password) # method provided by QLineEdit Class hides pass
        self.pass_edit.resize(210,20)
        self.pass_edit.move(80,70)

        # Create QCheckBox for displaying password
        self.show_pass_box = QCheckBox("Show Password", self)
        self.show_pass_box.move(80, 100)
        self.show_pass_box.toggled.connect(self.show_pass_if_check)

        # Create QPushButton for signing in
        self.login_button = QPushButton("Login", self)
        self.login_button.move(215, 95)
        self.login_button.clicked.connect(self.login_function)
        self.pass_edit.returnPressed.connect(self.login_button.click)

        # Create sign up QLabel and QPushButton
        QLabel("Not a member ?", self).move(80, 130)
        self.member_button = QPushButton("Sign up", self)
        self.member_button.move(215,125)
        self.member_button.clicked.connect(self.create_new_user)

    def OpenApplicationWindow(self):
        self.main_window = MainWindow()
        self.main_window.show()

    def show_pass_if_check(self, checked):
        sender = self.sender()
        if checked:
            self.pass_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        elif checked == False:
            self.pass_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def login_function(self):
        path = str(os.getcwd())+'/file/users.txt'
        try:
            with open(path, 'r') as file:
                users_info = [line.split() for line in file.readlines()]
            user_info = [self.user_edit.text(), self.pass_edit.text()]
            if user_info in users_info:
                QMessageBox.information(
                    self, "Login Successful!", "Login Successful!",
                    QMessageBox.StandardButton.Ok)
                self.login_is_successful = True
                self.close() # Close app
                self.OpenApplicationWindow()
            else:
                QMessageBox.warning(
                    self, "Error Message","The username or password is incorrect.",
                    QMessageBox.StandardButton.Close)
                self.login_is_successful = False
                self.user_edit.clear()
                self.pass_edit.clear()

        except FileNotFoundError as error:
            QMessageBox.warning(
                self, "Error", f"""<p>File not found.</p><p>Error:{error}</p>""",
                QMessageBox.StandardButton.Ok)
            f = open(file, "w")

        pass

    def create_new_user(self):
        """ Open a dialog for creating a new account. """
        self.create_new_user_window = NewUserDialog()
        self.create_new_user_window.show()
        self.close()


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(640,426)
        self.setWindowTitle('3.1 - Main Window')
        self.setUpMainWindow()

    def setUpMainWindow(self):
        """ Create QPixmap displayed in window """
        image = "images/background_kingfisher.jpg"
        try:
            with open(image):
                main_label = QLabel(self)
                pixmap = QPixmap(image)
                main_label.setPixmap(pixmap)
        except FileNotFoundError as error:
            pQMessageBox.warning(
                self, "Error", f"""<p>Image not found.</p><p>Error:{error}</p>""",
                QMessageBox.StandardButton.Ok)
        self.log_out_button = QPushButton('Log out', self)
        self.log_out_button.clicked.connect(self.logout)

    def logout(self):
        self.close()
        self.main_window = LoginWindow()
        self.main_window.show()

class NewUserDialog(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(330, 185)
        self.setWindowTitle("3.1 - Registration GUI")
        self.getRegistration()
        self.show()

    def getRegistration(self):
        header_text = QLabel("Create New Account", self)
        header_text.setFont(QFont("Calibri", 15))
        header_text.move(80,10)

        QLabel("Username:",self).move(5,40)
        self.user_edit = QLineEdit(self)
        self.user_edit.resize(210,20)
        self.user_edit.move(80,40)

        QLabel("Full Name:",self).move(5,70)
        self.name_edit = QLineEdit(self)
        self.name_edit.resize(210,20)
        self.name_edit.move(80,70)

        QLabel("Password:",self).move(5,100)
        self.pass_edit = QLineEdit(self)
        self.pass_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_edit.resize(210,20)
        self.pass_edit.move(80,100)

        QLabel("Confirm:",self).move(5,130)
        self.pass_confirm_edit = QLineEdit(self)
        self.pass_confirm_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_confirm_edit.resize(210,20)
        self.pass_confirm_edit.move(80,130)

        self.member_button = QPushButton("Send", self)
        self.member_button.move(80,155)
        self.member_button.clicked.connect(self.append_new_user)
        self.pass_edit.returnPressed.connect(self.member_button.click)

        self.back_button = QPushButton("Back", self)
        self.back_button.move(155,155)
        self.back_button.clicked.connect(self.OpenAppLoginWindow)

    def append_new_user(self):
        """ open txt """
        path = str(os.getcwd()) + '/file/users.txt'
        with open(path, 'r') as file:
            users = [line.strip() for line in file if line.strip()]

        """ verify if username is already used. """
        user_condition = False
        user_condition_empty = True
        if not str(self.user_edit.text()):
            QMessageBox.warning(
                self, "Error Message","Wrong input. Please try again",
                QMessageBox.StandardButton.Ok)
            user_condition_empty = False
        for user_info in users:
            if str(user_info[0]) != str(self.user_edit.text()) and str(self.user_edit.text()):
                user_condition = True
            elif str(user_info[0]) == str(self.user_edit.text()):
                user_condition = False
                break
        if user_condition == False and user_condition_empty == True:
            QMessageBox.warning(
                self, "Error Message","Username already used. Please try another one",
                QMessageBox.StandardButton.Ok)
            self.user_edit.clear()

        """ verify if password is correct """
        password_condition = False
        if self.pass_edit.text() == self.pass_confirm_edit.text():
            password_condition = True
        else:
            QMessageBox.warning(
                self, "Error Message","The passwords to not match password is incorrect.",
                QMessageBox.StandardButton.Close)
            self.pass_edit.clear()
            self.pass_confirm_edit.clear()

        if password_condition == True and user_condition == True:
            with open(path, 'a') as file:
                file.write(f"{self.user_edit.text()} {self.pass_confirm_edit.text()}\n")
                file.close()
            QMessageBox.information(
                self, "Welcome", 'New user has been created !',
                QMessageBox.StandardButton.Ok
            )
            self.close()
            self.OpenApplicationWindow()

    def OpenApplicationWindow(self):
        self.close()
        self.main_window = MainWindow()
        self.main_window.show()

    def OpenAppLoginWindow(self):
        self.close()
        self.main_window = LoginWindow()
        self.main_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
