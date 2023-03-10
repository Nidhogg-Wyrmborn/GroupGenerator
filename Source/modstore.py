# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIS/modulestore.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModuleStore(object):
    def setupUi(self, ModuleStore):
        ModuleStore.setObjectName("ModuleStore")
        ModuleStore.resize(772, 579)
        self.Modules = QtWidgets.QListWidget(ModuleStore)
        self.Modules.setGeometry(QtCore.QRect(10, 10, 256, 561))
        self.Modules.setObjectName("Modules")
        self.Desc = QtWidgets.QFrame(ModuleStore)
        self.Desc.setGeometry(QtCore.QRect(269, 9, 491, 501))
        self.Desc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Desc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Desc.setObjectName("Desc")
        self.Details = QtWidgets.QLabel(self.Desc)
        self.Details.setGeometry(QtCore.QRect(0, 395, 491, 101))
        self.Details.setAutoFillBackground(True)
        self.Details.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Details.setObjectName("Details")
        self.ModLabel = QtWidgets.QLabel(self.Desc)
        self.ModLabel.setGeometry(QtCore.QRect(0, 0, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ModLabel.setFont(font)
        self.ModLabel.setAutoFillBackground(True)
        self.ModLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.ModLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ModLabel.setObjectName("ModLabel")
        self.DescLabel = QtWidgets.QLabel(self.Desc)
        self.DescLabel.setGeometry(QtCore.QRect(0, 70, 491, 311))
        self.DescLabel.setAutoFillBackground(True)
        self.DescLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.DescLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.DescLabel.setObjectName("DescLabel")
        self.Un_Install = QtWidgets.QPushButton(ModuleStore)
        self.Un_Install.setGeometry(QtCore.QRect(660, 540, 93, 28))
        self.Un_Install.setObjectName("Un_Install")
        self.Update = QtWidgets.QPushButton(ModuleStore)
        self.Update.setGeometry(QtCore.QRect(560, 540, 93, 28))
        self.Update.setObjectName("Update")
        self.pushButton = QtWidgets.QPushButton(ModuleStore)
        self.pushButton.setGeometry(QtCore.QRect(270, 540, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.installBar = QtWidgets.QProgressBar(ModuleStore)
        self.installBar.setGeometry(QtCore.QRect(370, 540, 181, 23))
        self.installBar.setProperty("value", 24)
        self.installBar.setObjectName("installBar")
        self.installStatus = QtWidgets.QLabel(ModuleStore)
        self.installStatus.setGeometry(QtCore.QRect(370, 520, 55, 16))
        self.installStatus.setObjectName("installStatus")
        self.Request = QtWidgets.QPushButton(ModuleStore)
        self.Request.setGeometry(QtCore.QRect(270, 510, 93, 28))
        self.Request.setObjectName("Request")

        self.retranslateUi(ModuleStore)
        QtCore.QMetaObject.connectSlotsByName(ModuleStore)

    def retranslateUi(self, ModuleStore):
        _translate = QtCore.QCoreApplication.translate
        ModuleStore.setWindowTitle(_translate("ModuleStore", "Module Store"))
        self.Details.setText(_translate("ModuleStore", "{Author/Requestor Details}"))
        self.ModLabel.setText(_translate("ModuleStore", "{ModuleName}"))
        self.DescLabel.setText(_translate("ModuleStore", "{Description}"))
        self.Un_Install.setText(_translate("ModuleStore", "{Install/Uninstall}"))
        self.Update.setText(_translate("ModuleStore", "{Update}"))
        self.pushButton.setText(_translate("ModuleStore", "Report"))
        self.installStatus.setText(_translate("ModuleStore", "{Status}"))
        self.Request.setText(_translate("ModuleStore", "Request"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModuleStore = QtWidgets.QWidget()
    ui = Ui_ModuleStore()
    ui.setupUi(ModuleStore)
    ModuleStore.show()
    sys.exit(app.exec_())
