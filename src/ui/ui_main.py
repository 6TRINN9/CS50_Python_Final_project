# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 601)
        MainWindow.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(25, 23, 27, 255), stop:1 rgba(43, 3, 7, 255));\n"
"font-family: OCR-A BT")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = QLabel(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.Title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 24pt;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.Title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Title)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_create = QPushButton(self.centralwidget)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_create)

        self.btn_edit = QPushButton(self.centralwidget)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 24pt;\n"
"font-weight: bold;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.le_search_password = QLineEdit(self.centralwidget)
        self.le_search_password.setObjectName(u"le_search_password")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_search_password.sizePolicy().hasHeightForWidth())
        self.le_search_password.setSizePolicy(sizePolicy)
        self.le_search_password.setMinimumSize(QSize(30, 0))
        self.le_search_password.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid  rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")

        self.horizontalLayout.addWidget(self.le_search_password)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"Password manager", None))
        self.btn_create.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Search:", None))
        self.le_search_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password by Title", None))
    # retranslateUi

