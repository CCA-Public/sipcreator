# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.sipName = QtWidgets.QLineEdit(self.centralwidget)
        self.sipName.setObjectName("sipName")
        self.gridLayout.addWidget(self.sipName, 10, 0, 1, 2)
        self.bagSIPs = QtWidgets.QCheckBox(self.centralwidget)
        self.bagSIPs.setObjectName("bagSIPs")
        self.gridLayout.addWidget(self.bagSIPs, 12, 0, 1, 1)
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout.addWidget(self.cancelBtn, 19, 1, 1, 1)
        self.bulkExt = QtWidgets.QCheckBox(self.centralwidget)
        self.bulkExt.setObjectName("bulkExt")
        self.gridLayout.addWidget(self.bulkExt, 13, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 15, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 11, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.destination = QtWidgets.QLineEdit(self.centralwidget)
        self.destination.setObjectName("destination")
        self.gridLayout.addWidget(self.destination, 8, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 14, 0, 1, 1)
        self.status = QtWidgets.QLineEdit(self.centralwidget)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 16, 0, 1, 2)
        self.processBtn = QtWidgets.QPushButton(self.centralwidget)
        self.processBtn.setObjectName("processBtn")
        self.gridLayout.addWidget(self.processBtn, 19, 0, 1, 1)
        self.destinationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.destinationBtn.setObjectName("destinationBtn")
        self.gridLayout.addWidget(self.destinationBtn, 8, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 5, 0, 1, 2)
        self.sourceBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sourceBtn.setObjectName("sourceBtn")
        self.gridLayout.addWidget(self.sourceBtn, 3, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.toolBar.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SIP Creator", None))
        self.sipName.setPlaceholderText(_translate("MainWindow", "Name of SIP (Identifier---Accession Number)", None))
        self.bagSIPs.setText(_translate("MainWindow", "Bag SIP", None))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel", None))
        self.bulkExt.setText(_translate("MainWindow", "Run bulk_extractor", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Options</span></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Output Directory</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Source</span></p></body></html>", None))
        self.destination.setPlaceholderText(_translate("MainWindow", "/path/to/destination", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Status</span></p></body></html>", None))
        self.processBtn.setText(_translate("MainWindow", "Create SIP", None))
        self.destinationBtn.setText(_translate("MainWindow", "Browse", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Directory Selector</span></p></body></html>", None))
        self.sourceBtn.setText(_translate("MainWindow", "Select source", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SIP Name</span></p></body></html>", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

