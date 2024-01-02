# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'atelie_manager.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 449)
        MainWindow.setMaximumSize(QSize(320, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sendButton = QPushButton(self.centralwidget)
        self.sendButton.setObjectName(u"sendButton")

        self.gridLayout.addWidget(self.sendButton, 9, 0, 1, 1)

        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName(u"editButton")

        self.gridLayout.addWidget(self.editButton, 6, 0, 1, 1)

        self.productsBox = QComboBox(self.centralwidget)
        self.productsBox.setObjectName(u"productsBox")

        self.gridLayout.addWidget(self.productsBox, 1, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")

        self.gridLayout.addWidget(self.addButton, 7, 0, 1, 1)

        self.quantityProducts = QSpinBox(self.centralwidget)
        self.quantityProducts.setObjectName(u"quantityProducts")

        self.gridLayout.addWidget(self.quantityProducts, 3, 0, 1, 1)

        self.discountPercentage = QSpinBox(self.centralwidget)
        self.discountPercentage.setObjectName(u"discountPercentage")

        self.gridLayout.addWidget(self.discountPercentage, 5, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 320, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Editar produtos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Selecione o produto:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Quantos % de desconto?", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Quantos produtos foram comprados?", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Adicionar novos produtos", None))
    # retranslateUi

