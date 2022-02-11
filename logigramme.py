# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logigramme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from Condition import Condition
from EntreeSortie import EntreeSortie
from PyQt5 import QtCore, QtGui, QtWidgets

global scene 
scene = QtWidgets.QGraphicsScene()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 819)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 1001, 721))
        self.graphicsView.setObjectName("graphicsView")
        self.start_func_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_func_btn.setGeometry(QtCore.QRect(10, 740, 93, 28))
        self.start_func_btn.setObjectName("start_func_btn")
        self.fin_func_btn = QtWidgets.QPushButton(self.centralwidget)
        self.fin_func_btn.setGeometry(QtCore.QRect(10, 780, 93, 28))
        self.fin_func_btn.setObjectName("fin_func_btn")
        self.input_btn = QtWidgets.QPushButton(self.centralwidget)
        self.input_btn.setGeometry(QtCore.QRect(140, 740, 111, 28))
        self.input_btn.setObjectName("input_btn")
        self.output_btn = QtWidgets.QPushButton(self.centralwidget)
        self.output_btn.setGeometry(QtCore.QRect(140, 780, 111, 28))
        self.output_btn.setObjectName("output_btn")
        self.instruction_btn = QtWidgets.QPushButton(self.centralwidget)
        self.instruction_btn.setGeometry(QtCore.QRect(290, 740, 141, 28))
        self.instruction_btn.setObjectName("instruction_btn")
        self.condition_btn = QtWidgets.QPushButton(self.centralwidget)
        self.condition_btn.setGeometry(QtCore.QRect(290, 780, 141, 28))
        self.condition_btn.setObjectName("condition_btn")
        self.start_boucle_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_boucle_btn.setGeometry(QtCore.QRect(470, 740, 93, 28))
        self.start_boucle_btn.setObjectName("start_boucle_btn")
        self.fin_boucle_btn = QtWidgets.QPushButton(self.centralwidget)
        self.fin_boucle_btn.setGeometry(QtCore.QRect(470, 780, 93, 28))
        self.fin_boucle_btn.setObjectName("fin_boucle_btn")
        self.code_btn = QtWidgets.QPushButton(self.centralwidget)
        self.code_btn.setGeometry(QtCore.QRect(600, 740, 101, 28))
        self.code_btn.setObjectName("code_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.condition_btn.clicked.connect(self.drawCondition)
        self.input_btn.clicked.connect(self.drawInOut)
        self.output_btn.clicked.connect(self.drawInOut)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_func_btn.setText(_translate("MainWindow", "Début fonction"))
        self.fin_func_btn.setText(_translate("MainWindow", "Fin fonction"))
        self.input_btn.setText(_translate("MainWindow", "Définir une entrée"))
        self.output_btn.setText(_translate("MainWindow", "Définir une sortie"))
        self.instruction_btn.setText(_translate("MainWindow", "Définir une instruction"))
        self.condition_btn.setText(_translate("MainWindow", "Définir une condition"))
        self.start_boucle_btn.setText(_translate("MainWindow", "Début boucle"))
        self.fin_boucle_btn.setText(_translate("MainWindow", "Fin boucle"))
        self.code_btn.setText(_translate("MainWindow", "Générer le code"))

    def drawCondition(self):
        newCondition = Condition()
        drawnCond = newCondition.draw()
        scene.addItem(drawnCond)
        self.graphicsView.setScene(scene)
        self.graphicsView.show()

    def drawInOut(self):
        newEntry = EntreeSortie()
        drawnIO = newEntry.draw()
        scene.addItem(drawnIO)
        self.graphicsView.setScene(scene)
        self.graphicsView.show()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.quit())

