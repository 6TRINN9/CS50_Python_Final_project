# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_note.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_New_Note(object):
    def setupUi(self, New_Note):
        if not New_Note.objectName():
            New_Note.setObjectName(u"New_Note")
        New_Note.resize(300, 300)
        New_Note.setMinimumSize(QSize(300, 300))
        New_Note.setMaximumSize(QSize(300, 300))
        New_Note.setBaseSize(QSize(300, 300))
        New_Note.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(25, 23, 27, 255), stop:1 rgba(43, 3, 7, 255));\n"
"font-family: OCR-A BT")
        self.verticalLayout_2 = QVBoxLayout(New_Note)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_note = QLabel(New_Note)
        self.label_note.setObjectName(u"label_note")
        self.label_note.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 24pt;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_note, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_title = QLabel(New_Note)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 16pt;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout.addWidget(self.lb_title)

        self.le_Title = QLineEdit(New_Note)
        self.le_Title.setObjectName(u"le_Title")
        self.le_Title.setStyleSheet(u"font-size: 8pt;\n"
"background-color:  rgba(255, 255, 255, 40);")

        self.horizontalLayout.addWidget(self.le_Title)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_login = QLabel(New_Note)
        self.lb_login.setObjectName(u"lb_login")
        self.lb_login.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 16pt;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_2.addWidget(self.lb_login)

        self.le_login = QLineEdit(New_Note)
        self.le_login.setObjectName(u"le_login")
        self.le_login.setStyleSheet(u"font-size: 8pt;\n"
"background-color:  rgba(255, 255, 255, 40);")

        self.horizontalLayout_2.addWidget(self.le_login)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_password = QLabel(New_Note)
        self.lb_password.setObjectName(u"lb_password")
        self.lb_password.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 16pt;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_3.addWidget(self.lb_password)

        self.le_password = QLineEdit(New_Note)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setStyleSheet(u"font-size: 8pt;\n"
"background-color:  rgba(255, 255, 255, 40);")

        self.horizontalLayout_3.addWidget(self.le_password)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Spacer = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.Spacer)

        self.btn_create_password = QPushButton(New_Note)
        self.btn_create_password.setObjectName(u"btn_create_password")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_create_password.sizePolicy().hasHeightForWidth())
        self.btn_create_password.setSizePolicy(sizePolicy)
        self.btn_create_password.setMinimumSize(QSize(20, 0))
        self.btn_create_password.setStyleSheet(u"QPushButton {\n"
"font-size: 16pt;\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid  rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 100px;\n"
"height: 25px;\n"
"icon-size: 30pt 30pt;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"icon-size: 20pt 20pt;\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_create_password)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_url = QLabel(New_Note)
        self.lb_url.setObjectName(u"lb_url")
        self.lb_url.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 16pt;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_5.addWidget(self.lb_url)

        self.le_url = QLineEdit(New_Note)
        self.le_url.setObjectName(u"le_url")
        self.le_url.setStyleSheet(u"font-size: 8pt;\n"
"background-color:  rgba(255, 255, 255, 40);")

        self.horizontalLayout_5.addWidget(self.le_url)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.btn_create_note = QPushButton(New_Note)
        self.btn_create_note.setObjectName(u"btn_create_note")
        self.btn_create_note.setStyleSheet(u"QPushButton {\n"
"font-size: 16pt;\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid  rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"icon-size: 30pt 30pt;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"icon-size: 20pt 20pt;\n"
"}")

        self.verticalLayout.addWidget(self.btn_create_note)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(New_Note)

        QMetaObject.connectSlotsByName(New_Note)
    # setupUi

    def retranslateUi(self, New_Note):
        New_Note.setWindowTitle(QCoreApplication.translate("New_Note", u"New note", None))
        self.label_note.setText(QCoreApplication.translate("New_Note", u"New note", None))
        self.lb_title.setText(QCoreApplication.translate("New_Note", u"Title", None))
        self.le_Title.setText("")
        self.le_Title.setPlaceholderText(QCoreApplication.translate("New_Note", u"Title", None))
        self.lb_login.setText(QCoreApplication.translate("New_Note", u"Login", None))
        self.le_login.setPlaceholderText(QCoreApplication.translate("New_Note", u"Login", None))
        self.lb_password.setText(QCoreApplication.translate("New_Note", u"Password", None))
        self.le_password.setPlaceholderText(QCoreApplication.translate("New_Note", u"Password", None))
        self.btn_create_password.setText(QCoreApplication.translate("New_Note", u"Generate", None))
        self.lb_url.setText(QCoreApplication.translate("New_Note", u"URL", None))
        self.le_url.setPlaceholderText(QCoreApplication.translate("New_Note", u"URL", None))
        self.btn_create_note.setText(QCoreApplication.translate("New_Note", u"Create", None))
    # retranslateUi

