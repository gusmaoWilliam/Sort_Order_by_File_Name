# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sort_files.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from sort import Sort

st = Sort()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 150)
        MainWindow.setMinimumSize(QtCore.QSize(300, 150))
        MainWindow.setMaximumSize(QtCore.QSize(300, 150))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.select_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_btn.setObjectName("select_btn")
        self.horizontalLayout.addWidget(self.select_btn)
        self.line_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.line_dir.setReadOnly(True)
        self.line_dir.setObjectName("line_dir")
        self.horizontalLayout.addWidget(self.line_dir)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.misturar_btn = QtWidgets.QPushButton(self.centralwidget)
        self.misturar_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.misturar_btn.setMaximumSize(QtCore.QSize(100, 40))
        self.misturar_btn.setObjectName("misturar_btn")
        self.horizontalLayout_2.addWidget(self.misturar_btn)
        self.remover_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remover_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.remover_btn.setMaximumSize(QtCore.QSize(100, 40))
        self.remover_btn.setObjectName("remover_btn")
        self.horizontalLayout_2.addWidget(self.remover_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # -- Disable buttons
        self.misturar_btn.setDisabled(True)
        self.remover_btn.setDisabled(True)

        # -- Select Button
        self.select_btn.clicked.connect(self.ReadDir)

        # -- Misturar Button
        self.misturar_btn.clicked.connect(self.Misturar)

        #-- Remover Button
        self.remover_btn.clicked.connect(self.Remover)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Musicas Aleat??rio"))
        self.label.setText(_translate("MainWindow", "Selecione a pasta de musicas"))
        self.select_btn.setText(_translate("MainWindow", "Selecionar"))
        self.misturar_btn.setText(_translate("MainWindow", "Misturar"))
        self.remover_btn.setText(_translate("MainWindow", "Remover"))

    # Read Dir Function
    def ReadDir(self):
        dialog = QFileDialog()
        self.foo_dir = dialog.getExistingDirectory(None, 'Select an awesome directory')
        just_folder = self.foo_dir.split('/')[-1]
        self.line_dir.setText(just_folder)
        if len(self.foo_dir) > 1:
            self.misturar_btn.setEnabled(True)
            self.remover_btn.setEnabled(True)

    def Misturar(self):
        if st.SortNum(self.foo_dir) == 0:
            qmsg = QMessageBox()
            qmsg.setIcon(QMessageBox.Information)
            qmsg.setText("Misturado com Sucesso!")
            qmsg.exec()
            path = self.foo_dir
            path = os.path.realpath(path)
            os.startfile(path)
           
        else:
            qmsg = QMessageBox()
            qmsg.setIcon(QMessageBox.Critical)
            qmsg.setText("Falha")
            qmsg.exec()

    def Remover(self):
            if st.RemoveNum(self.foo_dir) == 0:
                qmsg = QMessageBox()
                qmsg.setIcon(QMessageBox.Information)
                qmsg.setText("Numeros removidos com Sucesso!")
                qmsg.exec()
                path = self.foo_dir
                path = os.path.realpath(path)
                os.startfile(path)
            
            else:
                qmsg = QMessageBox()
                qmsg.setIcon(QMessageBox.Critical)
                qmsg.setText("Falha")
                qmsg.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
