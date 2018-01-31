# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CCD.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_CCD(object):
    def setupUi(self, CCD):
        CCD.setObjectName(_fromUtf8("CCD"))
        CCD.resize(569, 300)
        self.verticalLayout = QtGui.QVBoxLayout(CCD)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.CCD_connect = QtGui.QPushButton(CCD)
        self.CCD_connect.setCheckable(True)
        self.CCD_connect.setObjectName(_fromUtf8("CCD_connect"))
        self.horizontalLayout.addWidget(self.CCD_connect)
        self.CCD_trigger = QtGui.QComboBox(CCD)
        self.CCD_trigger.setObjectName(_fromUtf8("CCD_trigger"))
        self.CCD_trigger.addItem(_fromUtf8(""))
        self.CCD_trigger.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.CCD_trigger)
        self.CCD_exposure = QtGui.QSpinBox(CCD)
        self.CCD_exposure.setMinimum(1)
        self.CCD_exposure.setMaximum(100)
        self.CCD_exposure.setProperty("value", 1)
        self.CCD_exposure.setObjectName(_fromUtf8("CCD_exposure"))
        self.horizontalLayout.addWidget(self.CCD_exposure)
        self.label = QtGui.QLabel(CCD)
        self.label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(CCD)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.D4Sigma = QtGui.QLabel(CCD)
        self.D4Sigma.setStyleSheet(_fromUtf8("font: 75 18pt \"Noto Sans\";\n"
"color: rgb(255, 0, 0);"))
        self.D4Sigma.setObjectName(_fromUtf8("D4Sigma"))
        self.horizontalLayout.addWidget(self.D4Sigma)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.CCD_plot = QtGui.QVBoxLayout()
        self.CCD_plot.setObjectName(_fromUtf8("CCD_plot"))
        self.verticalLayout.addLayout(self.CCD_plot)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.CCD_rec = QtGui.QPushButton(CCD)
        self.CCD_rec.setCheckable(True)
        self.CCD_rec.setObjectName(_fromUtf8("CCD_rec"))
        self.horizontalLayout_2.addWidget(self.CCD_rec)
        self.filePath = QtGui.QLineEdit(CCD)
        self.filePath.setObjectName(_fromUtf8("filePath"))
        self.horizontalLayout_2.addWidget(self.filePath)
        self.pathSelect = QtGui.QToolButton(CCD)
        self.pathSelect.setObjectName(_fromUtf8("pathSelect"))
        self.horizontalLayout_2.addWidget(self.pathSelect)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(CCD)
        QtCore.QMetaObject.connectSlotsByName(CCD)

    def retranslateUi(self, CCD):
        CCD.setWindowTitle(_translate("CCD", "Form", None))
        self.CCD_connect.setText(_translate("CCD", "Connect", None))
        self.CCD_trigger.setItemText(0, _translate("CCD", "Int.", None))
        self.CCD_trigger.setItemText(1, _translate("CCD", "Ext.", None))
        self.label.setText(_translate("CCD", "%", None))
        self.label_2.setText(_translate("CCD", "D4Sigma:", None))
        self.D4Sigma.setToolTip(_translate("CCD", "fast diameter", None))
        self.D4Sigma.setText(_translate("CCD", "val", None))
        self.CCD_rec.setText(_translate("CCD", "rec", None))
        self.filePath.setText(_translate("CCD", "./test.raw", None))
        self.pathSelect.setText(_translate("CCD", "...", None))

