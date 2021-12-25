from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QEvent
from Libraries.Speech import *
import googletrans

import googletrans
import login as lg
import time

lang_dict = {v: k for k, v in googletrans.LANGUAGES.items()}


class Ui_MainWindow(object):

    def mic_clicked(self):

        global voice_on
        if (not voice_on):
            voice_on = True
            from_lang = lang_dict[self.primary_lang.currentText()]
            to_lang = lang_dict[self.sec_lang.currentText()]
            listen(voice_on, from_lang, to_lang)
        else:
            voice_on = False

    # 1 for go back
    # 2 for log out
    def open_window(self, val):

        self.login_screen = QtWidgets.QMainWindow()

        self.ui = lg.Ui_login_window()
        self.ui.setupUi(self.login_screen)

        if val == 1:
            self.ui.mode_frame.setVisible(True)
        elif val == 2:
            self.ui.mode_frame.setVisible(False)

        self.login_screen.show()

    def textSonDurum(self):
        import re

        from_text = self.primary_text.toPlainText()
        if (re.search("[.?!\n। ]$", from_text) or from_text == ""):
            if (from_text != ""):
                to_text = translator.translate(
                    self.primary_text.toPlainText(), src=self.from_lang, dest=self.to_lang).text
            else:
                to_text = ""
            self.sec_text.setText(to_text)

    def setupUi(self, MainWindow):
        self.lcsr = MainWindow

        MainWindow.setObjectName("Live translation")
        MainWindow.resize(1005, 690)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.primary_text = QtWidgets.QTextEdit(self.centralwidget)
        self.primary_text.setGeometry(QtCore.QRect(10, 200, 471, 350))
        self.primary_text.textChanged.connect(self.textSonDurum)

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.primary_text.setFont(font)
        self.primary_text.setStyleSheet("")
        self.primary_text.setObjectName("primary_text")

        self.primary_lang = QtWidgets.QComboBox(self.centralwidget)
        self.primary_lang.setGeometry(QtCore.QRect(20, 150, 230, 30))

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.primary_lang.setFont(font)
        self.primary_lang.setObjectName("primary_lang")

        self.sec_lang = QtWidgets.QComboBox(self.centralwidget)
        self.sec_lang.setGeometry(QtCore.QRect(750, 150, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sec_lang.setFont(font)
        self.sec_lang.setObjectName("sec_lang")

        self.add_to_drop_down()
        self.primary_lang.activated.connect(self.update)
        self.sec_lang.activated.connect(self.update)
        self.from_lang = lang_dict[self.primary_lang.currentText()]
        self.to_lang = lang_dict[self.sec_lang.currentText()]

        self.microphone_button = QtWidgets.QPushButton(self.centralwidget)
        self.microphone_button.setGeometry(QtCore.QRect(440, 30, 121, 111))
        self.microphone_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/microphone.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.microphone_button.setIcon(icon)
        self.microphone_button.setIconSize(QtCore.QSize(100, 100))
        self.microphone_button.setFlat(False)
        self.microphone_button.setObjectName("microphone_button")
        self.microphone_button.setStyleSheet("")

        self.microphone_button.setStyleSheet("QPushButton {\n"
                                             "font: 12pt \"Comic Sans MS\";\n"
                                             "color : white;\n"
                                             "border-radius: 20%;\n"
                                             "border: 2px solid #4CAF50;\n"
                                             "}\n")

        self.sec_text = QtWidgets.QTextEdit(self.centralwidget)
        self.sec_text.setGeometry(QtCore.QRect(520, 200, 471, 350))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.sec_text.setFont(font)
        self.sec_text.setStyleSheet("QTextEdit {\n"
                                    "    background-color: rgb(250, 250, 250);\n"
                                    "}")
        self.sec_text.setReadOnly(True)
        self.sec_text.setObjectName("sec_text")

        self.recording_label = QtWidgets.QLabel(self.centralwidget)
        self.recording_label.setGeometry(QtCore.QRect(440, 150, 131, 43))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.recording_label.setFont(font)
        self.recording_label.setObjectName("recording_label")
        self.recording_label.setVisible(False)

        self.logout_ico = QtWidgets.QLabel(self.centralwidget)
        self.logout_ico.setGeometry(QtCore.QRect(840, 20, 41, 41))
        self.logout_ico.setText("")
        self.logout_ico.setPixmap(QtGui.QPixmap("images/log_out_icon.png"))
        self.logout_ico.setScaledContents(True)
        self.logout_ico.setObjectName("logout_ico")
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setGeometry(QtCore.QRect(890, 20, 102, 40))

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet("QPushButton {\n"
                                         "	font: 12pt \"Comic Sans MS\";\n"
                                         "	background-color: white;\n"
                                         "	color: black;\n"
                                         "	border: 2px solid #4CAF50;\n"
                                         "	border-radius: 5%;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "	background-color: #4CAF50;\n"
                                         "	color: white;\n"
                                         "\n"
                                         "	border: 2px solid #4CAF50;\n"
                                         "}\n")

        self.logout_button.setIconSize(QtCore.QSize(100, 100))
        self.logout_button.setFlat(False)
        self.logout_button.setObjectName("logout_button")

        self.goback_btn = QtWidgets.QPushButton(self.centralwidget)
        self.goback_btn.setGeometry(QtCore.QRect(420, 580, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.goback_btn.setFont(font)
        self.goback_btn.setStyleSheet("QPushButton {\n"
                                      "    font: 12pt \"Comic Sans MS\";\n"
                                      "color : white;\n"
                                      "background-color: #4CAF50;\n"
                                      "border-radius: 2px;\n"
                                      "border: 2px solid #4CAF50;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: white;\n"
                                      "    color: black;\n"
                                      "}\n"
                                      "")
        self.goback_btn.setIconSize(QtCore.QSize(100, 100))
        self.goback_btn.setFlat(False)
        self.goback_btn.setObjectName("goback_btn")

        self.goback_btn.setObjectName("goback_btn")
        self.proj_ico = QtWidgets.QLabel(self.centralwidget)
        self.proj_ico.setGeometry(QtCore.QRect(20, 10, 90, 80))
        self.proj_ico.setText("")
        self.proj_ico.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.proj_ico.setScaledContents(True)
        self.proj_ico.setObjectName("proj_ico")

        self.proj_ico.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        # recording label click
        self.clicks = 0

        self.microphone_button.clicked.connect(self.show_label)

        # navigation
        self.goback_btn.clicked.connect(lambda: self.open_window(1))
        self.goback_btn.clicked.connect(MainWindow.close)

        # log out
        self.logout_button.clicked.connect(lambda: self.open_window(2))
        self.logout_button.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.recording_label.setText(
            _translate("MainWindow", "Recording....."))
        self.logout_button.setText(_translate("MainWindow", "Log Out"))
        self.goback_btn.setText(_translate("MainWindow", "Go back"))

    def update(self):
        self.from_lang = lang_dict[self.primary_lang.currentText()]
        self.to_lang = lang_dict[self.sec_lang.currentText()]
        self.textSonDurum()

    def show_label(self):
        # print(self.clicks)
        if self.clicks % 2 == 1:
            # print("should show")
            self.recording_label.setVisible(False)
            self.clicks = 0

            self.microphone_button.setStyleSheet("QPushButton {\n"
                                                 "font: 12pt \"Comic Sans MS\";\n"
                                                 "color : white;\n"
                                                 "border-radius: 20%;\n"
                                                 "border: 2px solid #4CAF50;\n"
                                                 "}\n")

        else:

            # print("should not show")
            self.recording_label.setVisible(True)
            self.clicks = 1

            self.microphone_button.setStyleSheet("QPushButton {\n"
                                                 "font: 12pt \"Comic Sans MS\";\n"
                                                 "color : white;\n"
                                                 "border-radius: 20%;\n"
                                                 "border: 2px solid rgb(255, 0, 0);\n"
                                                 "}\n")

        self.mic_clicked()

    def add_to_drop_down(self):
        self.sec_lang.addItems([x for x in googletrans.LANGUAGES.values()])
        self.primary_lang.addItems([x for x in googletrans.LANGUAGES.values()])
        self.primary_lang.setItemText(0, 'english')
        self.sec_lang.setItemText(0, 'hindi')
        self.primary_lang.setCurrentIndex(0)
        self.sec_lang.setCurrentIndex(0)
