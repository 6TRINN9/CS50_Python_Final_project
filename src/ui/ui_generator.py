# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password_generator.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

import ui.Res_rc_rc

class Ui_Password_generator(object):
    def setupUi(self, Password_generator):
        if not Password_generator.objectName():
            Password_generator.setObjectName(u"Password_generator")
        Password_generator.resize(343, 208)
        Password_generator.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(25, 23, 27, 255), stop:1 rgba(43, 3, 7, 255));\n"
"font-family: OCR-A BT")
        self.verticalLayout_2 = QVBoxLayout(Password_generator)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 9, -1, 9)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.le_view_password = QLineEdit(Password_generator)
        self.le_view_password.setObjectName(u"le_view_password")
        self.le_view_password.setEnabled(True)
        self.le_view_password.setMouseTracking(False)
        self.le_view_password.setStyleSheet(u"font-size: 12pt;\n"
"font-weight: bold;\n"
"background-color:  rgba(255, 255, 255, 40);")
        self.le_view_password.setMaxLength(32767)
        self.le_view_password.setReadOnly(True)

        self.horizontalLayout.addWidget(self.le_view_password)

        self.bnt_repeat = QPushButton(Password_generator)
        self.bnt_repeat.setObjectName(u"bnt_repeat")
        self.bnt_repeat.setMinimumSize(QSize(24, 24))
        self.bnt_repeat.setStyleSheet(u"QPushButton {\n"
"font-size: 16pt;\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid  rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 30px;\n"
"height: 30px;\n"
"icon-size: 30pt 30pt;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"icon-size: 20pt 20pt;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/icons/replay_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_repeat.setIcon(icon)

        self.horizontalLayout.addWidget(self.bnt_repeat)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_strength = QLabel(Password_generator)
        self.lb_strength.setObjectName(u"lb_strength")
        font = QFont()
        font.setFamilies([u"OCR-A BT"])
        font.setPointSize(10)
        self.lb_strength.setFont(font)
        self.lb_strength.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_2.addWidget(self.lb_strength)

        self.lb_entropy = QLabel(Password_generator)
        self.lb_entropy.setObjectName(u"lb_entropy")
        self.lb_entropy.setFont(font)
        self.lb_entropy.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.lb_entropy)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slider_pass_length = QSlider(Password_generator)
        self.slider_pass_length.setObjectName(u"slider_pass_length")
        self.slider_pass_length.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height: 8px;\n"
"    background: rgba(255, 255, 255, 80);\n"
"    border-radius: 4px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #550000;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    margin: -6px 0;\n"
"    border-radius: 10px;\n"
"}")
        self.slider_pass_length.setMinimum(8)
        self.slider_pass_length.setMaximum(64)
        self.slider_pass_length.setSliderPosition(12)
        self.slider_pass_length.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.slider_pass_length)

        self.le_pass_length = QLineEdit(Password_generator)
        self.le_pass_length.setObjectName(u"le_pass_length")
        self.le_pass_length.setMaximumSize(QSize(30, 16777215))
        font1 = QFont()
        font1.setFamilies([u"OCR-A BT"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setHintingPreference(QFont.PreferVerticalHinting)
        self.le_pass_length.setFont(font1)
        self.le_pass_length.setStyleSheet(u"font-size: 12pt;\n"
"background-color:  rgba(255, 255, 255, 40);")
        self.le_pass_length.setReadOnly(False)

        self.horizontalLayout_3.addWidget(self.le_pass_length)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.cb_lowercase = QCheckBox(Password_generator)
        self.cb_lowercase.setObjectName(u"cb_lowercase")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_lowercase.sizePolicy().hasHeightForWidth())
        self.cb_lowercase.setSizePolicy(sizePolicy)
        self.cb_lowercase.setMinimumSize(QSize(0, 0))
        self.cb_lowercase.setMaximumSize(QSize(60, 16777215))
        self.cb_lowercase.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border: 2px solid #999999;\n"
"	font-size: 12pt;\n"
"	background-color: none;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"     background-color: rgba(255, 255, 255,80);\n"
"   	 border-color: rgba(255, 255, 255,80);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"     background-color: rgba(255, 255, 255,20);\n"
"    border-color: #999999;\n"
"}")
        self.cb_lowercase.setChecked(False)

        self.horizontalLayout_4.addWidget(self.cb_lowercase)

        self.cb_uppercase = QCheckBox(Password_generator)
        self.cb_uppercase.setObjectName(u"cb_uppercase")
        sizePolicy.setHeightForWidth(self.cb_uppercase.sizePolicy().hasHeightForWidth())
        self.cb_uppercase.setSizePolicy(sizePolicy)
        self.cb_uppercase.setMinimumSize(QSize(0, 0))
        self.cb_uppercase.setMaximumSize(QSize(60, 16777215))
        self.cb_uppercase.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border: 2px solid #999999;\n"
"	font-size: 12pt;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255,20);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"     background-color: rgba(255, 255, 255,80);\n"
"   	 border-color: rgba(255, 255, 255,80);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"     background-color: rgba(255, 255, 255,20);\n"
"    border-color: #999999;\n"
"}")

        self.horizontalLayout_4.addWidget(self.cb_uppercase)

        self.cb_digits = QCheckBox(Password_generator)
        self.cb_digits.setObjectName(u"cb_digits")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_digits.sizePolicy().hasHeightForWidth())
        self.cb_digits.setSizePolicy(sizePolicy1)
        self.cb_digits.setMinimumSize(QSize(0, 0))
        self.cb_digits.setMaximumSize(QSize(60, 16777215))
        self.cb_digits.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.cb_digits.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border: 2px solid #999999;\n"
"	font-size: 12pt;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255,20);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"     background-color: rgba(255, 255, 255,80);\n"
"   	 border-color: rgba(255, 255, 255,80);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"     background-color: rgba(255, 255, 255,20);\n"
"    border-color: #999999;\n"
"}")

        self.horizontalLayout_4.addWidget(self.cb_digits)

        self.cb_specials = QCheckBox(Password_generator)
        self.cb_specials.setObjectName(u"cb_specials")
        sizePolicy.setHeightForWidth(self.cb_specials.sizePolicy().hasHeightForWidth())
        self.cb_specials.setSizePolicy(sizePolicy)
        self.cb_specials.setMinimumSize(QSize(0, 0))
        self.cb_specials.setMaximumSize(QSize(60, 16777215))
        self.cb_specials.setAutoFillBackground(False)
        self.cb_specials.setStyleSheet(u"QCheckBox::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border: 2px solid #999999;\n"
"	font-size: 12pt;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255,20);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"     background-color: rgba(255, 255, 255,80);\n"
"   	 border-color: rgba(255, 255, 255,80);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"     background-color: rgba(255, 255, 255,20);\n"
"    border-color: #999999;\n"
"}")
        self.cb_specials.setTristate(False)

        self.horizontalLayout_4.addWidget(self.cb_specials)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.btm_ok = QPushButton(Password_generator)
        self.btm_ok.setObjectName(u"btm_ok")
        self.btm_ok.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btm_ok)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Password_generator)

        QMetaObject.connectSlotsByName(Password_generator)
    # setupUi

    def retranslateUi(self, Password_generator):
        Password_generator.setWindowTitle(QCoreApplication.translate("Password_generator", u"Password generator", None))
        self.le_view_password.setInputMask("")
        self.le_view_password.setText("")
        self.bnt_repeat.setText("")
        self.lb_strength.setText(QCoreApplication.translate("Password_generator", u"Strength: good", None))
        self.lb_entropy.setText(QCoreApplication.translate("Password_generator", u"Entropy: 150.00 bit", None))
        self.le_pass_length.setText(QCoreApplication.translate("Password_generator", u"64", None))
        self.cb_lowercase.setText(QCoreApplication.translate("Password_generator", u"a-z", None))
        self.cb_uppercase.setText(QCoreApplication.translate("Password_generator", u"A-Z", None))
        self.cb_digits.setText(QCoreApplication.translate("Password_generator", u"0-9", None))
        self.cb_specials.setText(QCoreApplication.translate("Password_generator", u"#$%?", None))
        self.btm_ok.setText(QCoreApplication.translate("Password_generator", u"OK", None))
    # retranslateUi

