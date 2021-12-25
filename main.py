
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import login as lg
import upload_window as uw
import live_translator as lt
from PyQt5 import QtCore, QtGui, QtWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    login_screen = QtWidgets.QMainWindow()
    login_screen.setWindowTitle("Translate+")

    ui = lg.Ui_login_window()
    ui.setupUi(login_screen)
    login_screen.show()

    sys.exit(app.exec_())
