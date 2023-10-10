# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design1.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(417, 272)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(12)
        font.setBold(True)
        self.progressBar.setFont(font)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar)

        self.plainEdit = QPlainTextEdit(self.centralwidget)
        self.plainEdit.setObjectName(u"plainEdit")

        self.verticalLayout.addWidget(self.plainEdit)

        self.pathVideo = QLineEdit(self.centralwidget)
        self.pathVideo.setObjectName(u"pathVideo")

        self.verticalLayout.addWidget(self.pathVideo)

        self.btn_dwld = QPushButton(self.centralwidget)
        self.btn_dwld.setObjectName(u"btn_dwld")

        self.verticalLayout.addWidget(self.btn_dwld)

        self.pathFile = QLineEdit(self.centralwidget)
        self.pathFile.setObjectName(u"pathFile")
        self.pathFile.setReadOnly(True)

        self.verticalLayout.addWidget(self.pathFile)

        self.btnPathFile = QPushButton(self.centralwidget)
        self.btnPathFile.setObjectName(u"btnPathFile")

        self.verticalLayout.addWidget(self.btnPathFile)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Download Video", None))
        self.pathVideo.setInputMask("")
        self.pathVideo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0441\u044b\u043b\u043a\u0443 \u0432\u0438\u0434\u0435\u043e", None))
        self.btn_dwld.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0443", None))
        self.pathFile.setInputMask("")
        self.pathFile.setText("")
        self.pathFile.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043f\u0430\u043f\u043a\u0438 \u0434\u043b\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438", None))
        self.btnPathFile.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438", None))
    # retranslateUi

