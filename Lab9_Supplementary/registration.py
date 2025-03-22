import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon, QFont


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Account Registration System "
        self.initUi()
        self.centerWindow()

    def initUi(self):
        self.setWindowTitle(self.title)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowIcon(QIcon('Application.ico'))
        title = QLabel("Account Registration Form", self)
        title.setFont(QFont("Arial", 14, QFont.Bold))
        title.move(120, 20)

        self.textbox = QLineEdit(self)
        self.textbox.move(200,60)
        self.textbox.resize(250, 30)
        self.textbox.setFont(QFont("Arial", 11, QFont.Bold))

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(200,110)
        self.textbox2.resize(250,30)
        self.textbox2.setFont(QFont("Arial", 11, QFont.Bold))

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(200,160)
        self.textbox3.resize(250, 30)
        self.textbox3.setFont(QFont("Arial", 11, QFont.Bold))

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(200,210)
        self.textbox4.resize(250, 30)
        self.textbox4.setFont(QFont("Arial", 11, QFont.Bold))

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(200,260)
        self.textbox5.resize(250, 30)
        self.textbox5.setFont(QFont("Arial", 11, QFont.Bold))

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(200,310)
        self.textbox6.resize(250, 30)
        self.textbox6.setFont(QFont("Arial", 11, QFont.Bold))

        self.textboxlbl = QLabel("First Name: ", self)
        self.textboxlbl.move(40,65)
        self.textboxlbl.setFont(QFont("Arial", 12, QFont.Bold))

        self.textboxlbl2 = QLabel("Last Name: ", self)
        self.textboxlbl2.move(40, 115)
        self.textboxlbl2.setFont(QFont("Arial", 12, QFont.Bold))

        self.textboxlbl3 = QLabel("Username: ", self)
        self.textboxlbl3.move(40, 165)
        self.textboxlbl3.setFont(QFont("Arial", 12, QFont.Bold))

        self.textboxlbl4 = QLabel("Password: ", self)
        self.textboxlbl4.move(40, 215)
        self.textboxlbl4.setFont(QFont("Arial", 12, QFont.Bold))
        self.textbox4.setEchoMode(QLineEdit.Password)

        self.textboxlbl5 = QLabel("Email Address: ", self)
        self.textboxlbl5.move(40, 265)
        self.textboxlbl5.setFont(QFont("Arial", 12, QFont.Bold))

        self.textboxlbl6 = QLabel("Contact Number: ", self)
        self.textboxlbl6.move(40, 315)
        self.textboxlbl6.setFont(QFont("Arial", 12, QFont.Bold))

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.move(215, 370)
        self.submit_button.resize(100, 30)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.move(340, 370)
        self.clear_button.resize(100, 30)
        self.clear_button.clicked.connect(self.clearFields)
        self.show()

    def clearFields(self):

        self.textbox.clear()
        self.textbox2.clear()
        self.textbox3.clear()
        self.textbox4.clear()
        self.textbox5.clear()
        self.textbox6.clear()


    def centerWindow(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = RegistrationForm()
    sys.exit(app.exec_())