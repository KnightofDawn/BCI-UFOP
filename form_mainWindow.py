# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 568)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.filepath_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.filepath_lineEdit.setObjectName("filepath_lineEdit")
        self.gridLayout.addWidget(self.filepath_lineEdit, 0, 0, 1, 1)
        self.browse_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.browse_pushButton.setObjectName("browse_pushButton")
        self.gridLayout.addWidget(self.browse_pushButton, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(11, 11, 11, 11)
        self.formLayout_2.setSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.batchSize_Label = QtWidgets.QLabel(self.centralWidget)
        self.batchSize_Label.setObjectName("batchSize_Label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.batchSize_Label)
        self.batchSize_lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.batchSize_lineEdit.setObjectName("batchSize_lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.batchSize_lineEdit)
        self.steps_label = QtWidgets.QLabel(self.centralWidget)
        self.steps_label.setObjectName("steps_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.steps_label)
        self.steps_lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.steps_lineEdit.setObjectName("steps_lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.steps_lineEdit)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.addHiddenLayer_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.addHiddenLayer_pushButton.setObjectName("addHiddenLayer_pushButton")
        self.verticalLayout.addWidget(self.addHiddenLayer_pushButton)
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 322, 305))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.beginLearning_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.beginLearning_pushButton.setFlat(False)
        self.beginLearning_pushButton.setObjectName("beginLearning_pushButton")
        self.verticalLayout.addWidget(self.beginLearning_pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.saveLog_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.saveLog_pushButton.setObjectName("saveLog_pushButton")
        self.gridLayout_2.addWidget(self.saveLog_pushButton, 1, 2, 1, 1)
        self.log_plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.log_plainTextEdit.setReadOnly(True)
        self.log_plainTextEdit.setObjectName("log_plainTextEdit")
        self.gridLayout_2.addWidget(self.log_plainTextEdit, 0, 0, 1, 3)
        self.clearLog_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.clearLog_pushButton.setObjectName("clearLog_pushButton")
        self.gridLayout_2.addWidget(self.clearLog_pushButton, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 675, 19))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DeepLearning Tensorflow"))
        self.groupBox.setTitle(_translate("MainWindow", "Dataset Filepath"))
        self.browse_pushButton.setText(_translate("MainWindow", "Browse..."))
        self.batchSize_Label.setText(_translate("MainWindow", "Batch Size"))
        self.steps_label.setText(_translate("MainWindow", "Steps"))
        self.addHiddenLayer_pushButton.setText(_translate("MainWindow", "Add Hidden Layer"))
        self.beginLearning_pushButton.setText(_translate("MainWindow", "Begin Learning"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Log"))
        self.saveLog_pushButton.setText(_translate("MainWindow", "Save Log"))
        self.clearLog_pushButton.setText(_translate("MainWindow", "Clear Log"))

