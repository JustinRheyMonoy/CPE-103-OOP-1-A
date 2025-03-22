import sys
from PyQt5.QtWidgets import QApplication
from registration import RegistrationForm

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())