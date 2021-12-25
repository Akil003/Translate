import textract
from enum import auto
from PyQt5 import QtCore, QtGui, QtWidgets
import googletrans
from docx import Document
document = Document()
lang_dict = {v: k for k, v in googletrans.LANGUAGES.items()}
