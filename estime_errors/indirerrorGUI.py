# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'indirerrorgui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1069, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.inpFuncBtn = QtWidgets.QPushButton(self.centralwidget)
        self.inpFuncBtn.setObjectName("inpFuncBtn")
        self.verticalLayout.addWidget(self.inpFuncBtn)
        self.inputVarsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.inputVarsBtn.setObjectName("inputVarsBtn")
        self.verticalLayout.addWidget(self.inputVarsBtn)
        self.calcFuncBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calcFuncBtn.setObjectName("calcFuncBtn")
        self.verticalLayout.addWidget(self.calcFuncBtn)
        self.plotFuncBtn = QtWidgets.QPushButton(self.centralwidget)
        self.plotFuncBtn.setObjectName("plotFuncBtn")
        self.verticalLayout.addWidget(self.plotFuncBtn)
        self.fitPlotBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fitPlotBtn.setObjectName("fitPlotBtn")
        self.verticalLayout.addWidget(self.fitPlotBtn)
        self.polyFitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.polyFitBtn.setObjectName("polyFitBtn")
        self.verticalLayout.addWidget(self.polyFitBtn)
        self.clearListBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearListBtn.setObjectName("clearListBtn")
        self.verticalLayout.addWidget(self.clearListBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1069, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.dirErrorOpen = QtWidgets.QAction(MainWindow)
        self.dirErrorOpen.setObjectName("dirErrorOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar_2.addAction(self.dirErrorOpen)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Рассчет косвенных погрешностей"))
        self.inpFuncBtn.setText(_translate("MainWindow", "Ввести функцию"))
        self.inputVarsBtn.setText(_translate("MainWindow", "Ввести переменные"))
        self.calcFuncBtn.setText(_translate("MainWindow", "Рассчитать функцию с погрешностями"))
        self.plotFuncBtn.setText(_translate("MainWindow", "Построить точки функции с погрешностью"))
        self.fitPlotBtn.setText(_translate("MainWindow", "Аппроксимировать нелинейным МНК"))
        self.polyFitBtn.setText(_translate("MainWindow", "Аппроксимация полиномом n степени"))
        self.clearListBtn.setText(_translate("MainWindow", "Очистить список"))
        self.menuFile.setTitle(_translate("MainWindow", "&Файл"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionOpen.setText(_translate("MainWindow", "Открыть"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Сохранить как..."))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionHelp.setText(_translate("MainWindow", "Помощь"))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1"))
        self.dirErrorOpen.setText(_translate("MainWindow", "Прямая погрешность"))

