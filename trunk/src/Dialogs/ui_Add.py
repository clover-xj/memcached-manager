# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add.ui'
#
# Created: Sun Feb 15 17:33:02 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddDialog(object):
    def setupUi(self, AddDialog):
        AddDialog.setObjectName("AddDialog")
        AddDialog.resize(308, 363)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/Add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(AddDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gbCluster = QtGui.QGroupBox(AddDialog)
        self.gbCluster.setObjectName("gbCluster")
        self.gridLayout_2 = QtGui.QGridLayout(self.gbCluster)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblClusterName = QtGui.QLabel(self.gbCluster)
        self.lblClusterName.setObjectName("lblClusterName")
        self.gridLayout_2.addWidget(self.lblClusterName, 0, 0, 1, 1)
        self.txtClusterName = QtGui.QLineEdit(self.gbCluster)
        self.txtClusterName.setObjectName("txtClusterName")
        self.gridLayout_2.addWidget(self.txtClusterName, 0, 1, 1, 1)
        self.btnAddCluster = QtGui.QPushButton(self.gbCluster)
        self.btnAddCluster.setObjectName("btnAddCluster")
        self.gridLayout_2.addWidget(self.btnAddCluster, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.gbCluster)
        self.gbAddServer = QtGui.QGroupBox(AddDialog)
        self.gbAddServer.setObjectName("gbAddServer")
        self.gridLayout = QtGui.QGridLayout(self.gbAddServer)
        self.gridLayout.setObjectName("gridLayout")
        self.cbClusters = QtGui.QComboBox(self.gbAddServer)
        self.cbClusters.setObjectName("cbClusters")
        self.gridLayout.addWidget(self.cbClusters, 1, 1, 1, 1)
        self.txtServerAddress = QtGui.QLineEdit(self.gbAddServer)
        self.txtServerAddress.setObjectName("txtServerAddress")
        self.gridLayout.addWidget(self.txtServerAddress, 3, 1, 1, 1)
        self.lblServerPort = QtGui.QLabel(self.gbAddServer)
        self.lblServerPort.setObjectName("lblServerPort")
        self.gridLayout.addWidget(self.lblServerPort, 4, 0, 1, 1)
        self.txtServerPort = QtGui.QLineEdit(self.gbAddServer)
        self.txtServerPort.setObjectName("txtServerPort")
        self.gridLayout.addWidget(self.txtServerPort, 4, 1, 2, 1)
        self.btnAddServer = QtGui.QPushButton(self.gbAddServer)
        self.btnAddServer.setObjectName("btnAddServer")
        self.gridLayout.addWidget(self.btnAddServer, 7, 1, 1, 1)
        self.lblServerAddress = QtGui.QLabel(self.gbAddServer)
        self.lblServerAddress.setObjectName("lblServerAddress")
        self.gridLayout.addWidget(self.lblServerAddress, 3, 0, 1, 1)
        self.lblCluster = QtGui.QLabel(self.gbAddServer)
        self.lblCluster.setObjectName("lblCluster")
        self.gridLayout.addWidget(self.lblCluster, 1, 0, 1, 1)
        self.txtServerName = QtGui.QLineEdit(self.gbAddServer)
        self.txtServerName.setObjectName("txtServerName")
        self.gridLayout.addWidget(self.txtServerName, 2, 1, 1, 1)
        self.lblServerName = QtGui.QLabel(self.gbAddServer)
        self.lblServerName.setObjectName("lblServerName")
        self.gridLayout.addWidget(self.lblServerName, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.gbAddServer)
        self.btnClose = QtGui.QPushButton(AddDialog)
        self.btnClose.setObjectName("btnClose")
        self.verticalLayout.addWidget(self.btnClose)

        self.retranslateUi(AddDialog)
        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL("clicked()"), AddDialog.close)
        QtCore.QMetaObject.connectSlotsByName(AddDialog)

    def retranslateUi(self, AddDialog):
        AddDialog.setWindowTitle(QtGui.QApplication.translate("AddDialog", "Add Clusters & Servers", None, QtGui.QApplication.UnicodeUTF8))
        self.gbCluster.setTitle(QtGui.QApplication.translate("AddDialog", "Add Cluster", None, QtGui.QApplication.UnicodeUTF8))
        self.lblClusterName.setText(QtGui.QApplication.translate("AddDialog", "Cluster Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddCluster.setText(QtGui.QApplication.translate("AddDialog", "Add Cluster", None, QtGui.QApplication.UnicodeUTF8))
        self.gbAddServer.setTitle(QtGui.QApplication.translate("AddDialog", "Add Server", None, QtGui.QApplication.UnicodeUTF8))
        self.lblServerPort.setText(QtGui.QApplication.translate("AddDialog", "Server Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddServer.setText(QtGui.QApplication.translate("AddDialog", "Add Server", None, QtGui.QApplication.UnicodeUTF8))
        self.lblServerAddress.setText(QtGui.QApplication.translate("AddDialog", "Server Address:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCluster.setText(QtGui.QApplication.translate("AddDialog", "Cluster:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblServerName.setText(QtGui.QApplication.translate("AddDialog", "Server Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose.setText(QtGui.QApplication.translate("AddDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

