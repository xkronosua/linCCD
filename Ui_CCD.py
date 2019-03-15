# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CCD.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CCD(object):
    def setupUi(self, CCD):
        CCD.setObjectName("CCD")
        CCD.resize(591, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(CCD)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CCD_connect = QtWidgets.QPushButton(CCD)
        self.CCD_connect.setCheckable(True)
        self.CCD_connect.setObjectName("CCD_connect")
        self.horizontalLayout.addWidget(self.CCD_connect)
        self.CCD_trigger = QtWidgets.QComboBox(CCD)
        self.CCD_trigger.setObjectName("CCD_trigger")
        self.CCD_trigger.addItem("")
        self.CCD_trigger.addItem("")
        self.horizontalLayout.addWidget(self.CCD_trigger)
        self.CCD_exposure = QtWidgets.QSpinBox(CCD)
        self.CCD_exposure.setMinimum(1)
        self.CCD_exposure.setMaximum(100)
        self.CCD_exposure.setProperty("value", 1)
        self.CCD_exposure.setObjectName("CCD_exposure")
        self.horizontalLayout.addWidget(self.CCD_exposure)
        self.CCD_baseline = QtWidgets.QPushButton(CCD)
        self.CCD_baseline.setCheckable(True)
        self.CCD_baseline.setObjectName("CCD_baseline")
        self.horizontalLayout.addWidget(self.CCD_baseline)
        self.CCD_fastMode = QtWidgets.QCheckBox(CCD)
        self.CCD_fastMode.setObjectName("CCD_fastMode")
        self.horizontalLayout.addWidget(self.CCD_fastMode)
        self.label = QtWidgets.QLabel(CCD)
        self.label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(CCD)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.D4Sigma = QtWidgets.QLabel(CCD)
        self.D4Sigma.setStyleSheet("font: 75 18pt \"Noto Sans\";\n"
"color: rgb(255, 0, 0);")
        self.D4Sigma.setObjectName("D4Sigma")
        self.horizontalLayout.addWidget(self.D4Sigma)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.CCD_plot = QtWidgets.QVBoxLayout()
        self.CCD_plot.setObjectName("CCD_plot")
        self.verticalLayout.addLayout(self.CCD_plot)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.CCD_rec = QtWidgets.QPushButton(CCD)
        self.CCD_rec.setCheckable(True)
        self.CCD_rec.setObjectName("CCD_rec")
        self.horizontalLayout_2.addWidget(self.CCD_rec)
        self.rec_limit = QtWidgets.QSpinBox(CCD)
        self.rec_limit.setMinimum(1)
        self.rec_limit.setMaximum(999999999)
        self.rec_limit.setObjectName("rec_limit")
        self.horizontalLayout_2.addWidget(self.rec_limit)
        self.rec_counter = QtWidgets.QLabel(CCD)
        self.rec_counter.setObjectName("rec_counter")
        self.horizontalLayout_2.addWidget(self.rec_counter)
        self.filePath = QtWidgets.QLineEdit(CCD)
        self.filePath.setObjectName("filePath")
        self.horizontalLayout_2.addWidget(self.filePath)
        self.pathSelect = QtWidgets.QToolButton(CCD)
        self.pathSelect.setObjectName("pathSelect")
        self.horizontalLayout_2.addWidget(self.pathSelect)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(CCD)
        QtCore.QMetaObject.connectSlotsByName(CCD)

    def retranslateUi(self, CCD):
        _translate = QtCore.QCoreApplication.translate
        CCD.setWindowTitle(_translate("CCD", "Form"))
        self.CCD_connect.setText(_translate("CCD", "Connect"))
        self.CCD_trigger.setItemText(0, _translate("CCD", "Int."))
        self.CCD_trigger.setItemText(1, _translate("CCD", "Ext."))
        self.CCD_baseline.setText(_translate("CCD", "baseline"))
        self.CCD_fastMode.setText(_translate("CCD", "Fast"))
        self.label.setText(_translate("CCD", "%"))
        self.label_2.setText(_translate("CCD", "D4Sigma:"))
        self.D4Sigma.setToolTip(_translate("CCD", "fast diameter"))
        self.D4Sigma.setText(_translate("CCD", "val"))
        self.CCD_rec.setText(_translate("CCD", "rec"))
        self.rec_counter.setText(_translate("CCD", "0"))
        self.filePath.setText(_translate("CCD", "./test.dat"))
        self.pathSelect.setText(_translate("CCD", "..."))

