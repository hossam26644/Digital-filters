# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1387, 686)
        Form.setFixedSize(1387, 690)

        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(225, 20, 1000, 181))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Import = QtGui.QPushButton(self.layoutWidget)
        self.Import.setAccessibleName(_fromUtf8(""))
        self.Import.setObjectName(_fromUtf8("Import"))
        self.verticalLayout.addWidget(self.Import)
        self.Record = QtGui.QPushButton(self.layoutWidget)
        self.Record.setObjectName(_fromUtf8("Record"))
        self.verticalLayout.addWidget(self.Record)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.FirstOption = QtGui.QRadioButton(self.layoutWidget)
        self.FirstOption.setObjectName(_fromUtf8("FirstOption"))
        self.verticalLayout_2.addWidget(self.FirstOption)
        self.SecondOption = QtGui.QRadioButton(self.layoutWidget)
        self.SecondOption.setObjectName(_fromUtf8("SecondOption"))
        self.verticalLayout_2.addWidget(self.SecondOption)
        self.ThirdOption = QtGui.QRadioButton(self.layoutWidget)
        self.ThirdOption.setObjectName(_fromUtf8("ThirdOption"))
        self.verticalLayout_2.addWidget(self.ThirdOption)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Listen = QtGui.QPushButton(self.layoutWidget)
        self.Listen.setObjectName(_fromUtf8("Listen"))
        self.verticalLayout_3.addWidget(self.Listen)
        self.Save = QtGui.QPushButton(self.layoutWidget)
        self.Save.setObjectName(_fromUtf8("Save"))
        self.verticalLayout_3.addWidget(self.Save)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 200, 531, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 440, 151, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frequency_widget_b = QtGui.QWidget(Form)
        self.frequency_widget_b.setGeometry(QtCore.QRect(10, 220, 531, 211))
        self.frequency_widget_b.setObjectName(_fromUtf8("frequency_widget_b"))
        self.phase_widget_b = QtGui.QWidget(Form)
        self.phase_widget_b.setGeometry(QtCore.QRect(10, 460, 531, 221))
        self.phase_widget_b.setObjectName(_fromUtf8("phase_widget_b"))
        self.phase_widget = QtGui.QWidget(Form)
        self.phase_widget.setGeometry(QtCore.QRect(550, 460, 411, 221))
        self.phase_widget.setObjectName(_fromUtf8("phase_widget"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(550, 440, 151, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(550, 200, 531, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.frequency_widget = QtGui.QWidget(Form)
        self.frequency_widget.setGeometry(QtCore.QRect(550, 220, 411, 211))
        self.frequency_widget.setObjectName(_fromUtf8("frequency_widget"))
        self.frequency_widget_a = QtGui.QWidget(Form)
        self.frequency_widget_a.setGeometry(QtCore.QRect(970, 220, 411, 211))
        self.frequency_widget_a.setObjectName(_fromUtf8("frequency_widget_a"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(970, 440, 531, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(970, 200, 531, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.phase_widget_a = QtGui.QWidget(Form)
        self.phase_widget_a.setGeometry(QtCore.QRect(970, 460, 411, 221))
        self.phase_widget_a.setObjectName(_fromUtf8("phase_widget_a"))

        self.mplvlfb = QtGui.QVBoxLayout(self.frequency_widget_b)
        self.mplvlfb.setObjectName("mplvlfb")
        self.mplvlpb = QtGui.QVBoxLayout(self.phase_widget_b)
        self.mplvlpb.setObjectName("mplvlpb")
        self.mplvlf = QtGui.QVBoxLayout(self.frequency_widget)
        self.mplvlf.setObjectName("mplvlf")
        self.mplvlp = QtGui.QVBoxLayout(self.phase_widget)
        self.mplvlp.setObjectName("mplvlp")
        self.mplvlfa = QtGui.QVBoxLayout(self.frequency_widget_a)
        self.mplvlfa.setObjectName("mplvlfa")
        self.mplvlpa = QtGui.QVBoxLayout(self.phase_widget_a)
        self.mplvlpa.setObjectName("mplvlpa")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Online filter", None))
        self.Import.setText(_translate("Form", "Import", None))
        self.Record.setText(_translate("Form", "Record", None))
        self.FirstOption.setText(_translate("Form", "LowPass Filter", None))
        self.SecondOption.setText(_translate("Form", "HighPass Filter", None))
        self.ThirdOption.setText(_translate("Form", "Notch Filter", None))
        self.Listen.setText(_translate("Form", "Listen", None))
        self.Save.setText(_translate("Form", "Save", None))
        self.label.setText(_translate("Form", "Signal frequencies", None))
        self.label_2.setText(_translate("Form", "Signal phase response", None))
        self.label_3.setText(_translate("Form", "Filter phase response", None))
        self.label_4.setText(_translate("Form", "Filter frequency response", None))
        self.label_5.setText(_translate("Form", "Filtered phase response", None))
        self.label_6.setText(_translate("Form", "Filtered frequencies", None))

        self.Import.setToolTip("Import Wav file to apply the filter on it")
        self.Listen.setToolTip("Listen to filtered WAV file")

        self.Record.setToolTip("Record 5 seconds audio to apply the filter on it")

        self.Save.setToolTip("Save output")
