# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(687, 669)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 13, 0, 1, 2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 9, 0, 1, 1)
        self.bagSIPs = QtGui.QCheckBox(self.centralwidget)
        self.bagSIPs.setObjectName(_fromUtf8("bagSIPs"))
        self.gridLayout.addWidget(self.bagSIPs, 10, 0, 1, 1)
        self.cancelBtn = QtGui.QPushButton(self.centralwidget)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.gridLayout.addWidget(self.cancelBtn, 17, 1, 1, 1)
        self.bulkExt = QtGui.QCheckBox(self.centralwidget)
        self.bulkExt.setObjectName(_fromUtf8("bulkExt"))
        self.gridLayout.addWidget(self.bulkExt, 11, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.destination = QtGui.QLineEdit(self.centralwidget)
        self.destination.setObjectName(_fromUtf8("destination"))
        self.gridLayout.addWidget(self.destination, 8, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 12, 0, 1, 1)
        self.status = QtGui.QLineEdit(self.centralwidget)
        self.status.setObjectName(_fromUtf8("status"))
        self.gridLayout.addWidget(self.status, 14, 0, 1, 2)
        self.processBtn = QtGui.QPushButton(self.centralwidget)
        self.processBtn.setObjectName(_fromUtf8("processBtn"))
        self.gridLayout.addWidget(self.processBtn, 17, 0, 1, 1)
        self.destinationBtn = QtGui.QPushButton(self.centralwidget)
        self.destinationBtn.setObjectName(_fromUtf8("destinationBtn"))
        self.gridLayout.addWidget(self.destinationBtn, 8, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.gridLayout.addWidget(self.treeView, 5, 0, 1, 2)
        self.sourceBtn = QtGui.QPushButton(self.centralwidget)
        self.sourceBtn.setObjectName(_fromUtf8("sourceBtn"))
        self.gridLayout.addWidget(self.sourceBtn, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SIP Creator", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Options</span></p></body></html>", None))
        self.bagSIPs.setText(_translate("MainWindow", "Bag SIP", None))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel", None))
        self.bulkExt.setText(_translate("MainWindow", "Run bulk_extractor", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Destination</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Source</span></p></body></html>", None))
        self.destination.setPlaceholderText(_translate("MainWindow", "/path/to/destination", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Status</span></p></body></html>", None))
        self.processBtn.setText(_translate("MainWindow", "Create SIP", None))
        self.destinationBtn.setText(_translate("MainWindow", "Browse", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Directory Selector</span></p></body></html>", None))
        self.sourceBtn.setText(_translate("MainWindow", "Select source", None))

