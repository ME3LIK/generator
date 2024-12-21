# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
    QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(542, 418))
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background-color:#121212;\n"
"	color: white;\n"
"	font-family: Verdana;\n"
"	font-size: 16ptn;\n"
"	margin: 10px;\n"
"}\n"
"QPushButton {\n"
"		border: 2px solid gray;\n"
"		border-radius: 5px;\n"
"}\n"
"QPushButton#btn_lower,\n"
"#btn_upper,\n"
"#btn_digits,\n"
"#btn_special{\n"
"		padding: 10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover { \n"
"		border-color: #090;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"		border: 4px solid #090;\n"
"		border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"		background-color: #006300;\n"
"		border-color: #090;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/lock.png", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.pushButton)

        self.layout_password = QHBoxLayout()
        self.layout_password.setObjectName(u"layout_password")
        self.frame_password = QFrame(self.centralwidget)
        self.frame_password.setObjectName(u"frame_password")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_password.sizePolicy().hasHeightForWidth())
        self.frame_password.setSizePolicy(sizePolicy1)
        self.frame_password.setStyleSheet(u"QFrame{\n"
"		border: 2px solid gray;\n"
"		border-radius: 5 px;\n"
"		margin-right: 0;\n"
"}\n"
"QFrame:hover {\n"
"		border-color: #090;\n"
"}")
        self.frame_password.setFrameShape(QFrame.StyledPanel)
        self.frame_password.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_password)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.frame_password)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setMinimumSize(QSize(30, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"		border: none;\n"
"		margin: 0;\n"
"		forn-size: 20pt;\n"
"}")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.btn_visibility = QPushButton(self.frame_password)
        self.btn_visibility.setObjectName(u"btn_visibility")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_visibility.sizePolicy().hasHeightForWidth())
        self.btn_visibility.setSizePolicy(sizePolicy3)
        self.btn_visibility.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_visibility.setStyleSheet(u"QPushButton{\n"
"		border: none;\n"
"		margin: 0;\n"
"		background-color: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/visibility.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_visibility.setIcon(icon1)
        self.btn_visibility.setIconSize(QSize(52, 52))
        self.btn_visibility.setCheckable(True)
        self.btn_visibility.setChecked(True)

        self.horizontalLayout.addWidget(self.btn_visibility)


        self.layout_password.addWidget(self.frame_password)

        self.btn_refresh = QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName(u"btn_refresh")
        sizePolicy3.setHeightForWidth(self.btn_refresh.sizePolicy().hasHeightForWidth())
        self.btn_refresh.setSizePolicy(sizePolicy3)
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
"		margin-right: 0;\n"
"		margin-left: 0;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_refresh.setIcon(icon2)
        self.btn_refresh.setIconSize(QSize(52, 52))

        self.layout_password.addWidget(self.btn_refresh)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        sizePolicy3.setHeightForWidth(self.btn_copy.sizePolicy().hasHeightForWidth())
        self.btn_copy.setSizePolicy(sizePolicy3)
        self.btn_copy.setStyleSheet(u"QPushButton{\n"
"		pading: 5px;\n"
"		margin-left: 0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/tab_inactive.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_copy.setIcon(icon3)
        self.btn_copy.setIconSize(QSize(52, 52))

        self.layout_password.addWidget(self.btn_copy)


        self.verticalLayout.addLayout(self.layout_password)

        self.layout_info = QHBoxLayout()
        self.layout_info.setObjectName(u"layout_info")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.layout_info.addWidget(self.label_2)

        self.label_entropy = QLabel(self.centralwidget)
        self.label_entropy.setObjectName(u"label_entropy")
        self.label_entropy.setMinimumSize(QSize(52, 52))
        self.label_entropy.setAlignment(Qt.AlignCenter)

        self.layout_info.addWidget(self.label_entropy)


        self.verticalLayout.addLayout(self.layout_info)

        self.layout_lenght = QHBoxLayout()
        self.layout_lenght.setObjectName(u"layout_lenght")
        self.slider_lenght = QSlider(self.centralwidget)
        self.slider_lenght.setObjectName(u"slider_lenght")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.slider_lenght.sizePolicy().hasHeightForWidth())
        self.slider_lenght.setSizePolicy(sizePolicy4)
        self.slider_lenght.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.slider_lenght.setStyleSheet(u"QSlider_lengh::groove:horizontal {\n"
"		background-color: transparent;\n"
"		height: 5px;\n"
"}\n"
"QSlider_lengh:: sub-page:horizontal {\n"
"		background-color: #090;\n"
"}\n"
"QSlider_lengh::add-page:horizontal{\n"
"		background-color: gray;\n"
"}\n"
"QSlider_lengh::handle:horizontal {\n"
"		background-color: white;\n"
"		widht: 22px;\n"
"		broder-radius: 10px;\n"
"		margin-top: -8px;\n"
"		margin-bottom: -8px;\n"
"}\n"
"")
        self.slider_lenght.setMaximum(100)
        self.slider_lenght.setValue(12)
        self.slider_lenght.setOrientation(Qt.Horizontal)

        self.layout_lenght.addWidget(self.slider_lenght)

        self.spinbox_lenight = QSpinBox(self.centralwidget)
        self.spinbox_lenight.setObjectName(u"spinbox_lenight")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.spinbox_lenight.sizePolicy().hasHeightForWidth())
        self.spinbox_lenight.setSizePolicy(sizePolicy5)
        self.spinbox_lenight.setStyleSheet(u"QSpinBox{\n"
"		border: 2px solid gray;\n"
"		border-radius: 5px;\n"
"		background: transparent;\n"
"		padding: 2px;\n"
"}\n"
"\n"
"QSpinBox:hover{\n"
"		border-color: #009900;\n"
"}")
        self.spinbox_lenight.setAlignment(Qt.AlignCenter)
        self.spinbox_lenight.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinbox_lenight.setValue(12)

        self.layout_lenght.addWidget(self.spinbox_lenight)


        self.verticalLayout.addLayout(self.layout_lenght)

        self.layout_characters_2 = QHBoxLayout()
        self.layout_characters_2.setObjectName(u"layout_characters_2")
        self.btn_lower = QPushButton(self.centralwidget)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setCheckable(True)
        self.btn_lower.setChecked(True)

        self.layout_characters_2.addWidget(self.btn_lower)

        self.btn_upper = QPushButton(self.centralwidget)
        self.btn_upper.setObjectName(u"btn_upper")
        self.btn_upper.setCheckable(True)
        self.btn_upper.setChecked(True)

        self.layout_characters_2.addWidget(self.btn_upper)

        self.btn_digits = QPushButton(self.centralwidget)
        self.btn_digits.setObjectName(u"btn_digits")
        self.btn_digits.setIconSize(QSize(52, 52))
        self.btn_digits.setCheckable(True)
        self.btn_digits.setChecked(True)

        self.layout_characters_2.addWidget(self.btn_digits)

        self.btn_special = QPushButton(self.centralwidget)
        self.btn_special.setObjectName(u"btn_special")
        self.btn_special.setCheckable(True)

        self.layout_characters_2.addWidget(self.btn_special)


        self.verticalLayout.addLayout(self.layout_characters_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.pushButton.setText("")
        self.btn_visibility.setText("")
        self.btn_refresh.setText("")
        self.btn_copy.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Strenght: Stronk", None))
        self.label_entropy.setText(QCoreApplication.translate("MainWindow", u"Entropy: 13.37 bit", None))
        self.btn_lower.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.btn_upper.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.btn_digits.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.btn_special.setText(QCoreApplication.translate("MainWindow", u"#$%", None))
    # retranslateUi

