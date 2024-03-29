# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logigramme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import generateCode 
from Boucle import Boucle
from Condition import Condition
from EntreeSortie import EntreeSortie
from Fonction import Fonction
from Instruction import Instruction
from text_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

global scene 
scene = QtWidgets.QGraphicsScene()

global list_object
list_object = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 868)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 1061, 721))
        self.graphicsView.setObjectName("graphicsView")
        self.start_func_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_func_btn.setGeometry(QtCore.QRect(10, 790, 93, 28))
        self.start_func_btn.setObjectName("start_func_btn")
        self.fin_func_btn = QtWidgets.QPushButton(self.centralwidget)
        self.fin_func_btn.setGeometry(QtCore.QRect(10, 830, 93, 28))
        self.fin_func_btn.setObjectName("fin_func_btn")
        self.input_btn = QtWidgets.QPushButton(self.centralwidget)
        self.input_btn.setGeometry(QtCore.QRect(140, 790, 111, 28))
        self.input_btn.setObjectName("input_btn")
        self.output_btn = QtWidgets.QPushButton(self.centralwidget)
        self.output_btn.setGeometry(QtCore.QRect(140, 830, 111, 28))
        self.output_btn.setObjectName("output_btn")
        self.instruction_btn = QtWidgets.QPushButton(self.centralwidget)
        self.instruction_btn.setGeometry(QtCore.QRect(290, 790, 141, 28))
        self.instruction_btn.setObjectName("instruction_btn")
        self.condition_btn = QtWidgets.QPushButton(self.centralwidget)
        self.condition_btn.setGeometry(QtCore.QRect(290, 830, 141, 28))
        self.condition_btn.setObjectName("condition_btn")
        self.start_boucle_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_boucle_btn.setGeometry(QtCore.QRect(470, 790, 93, 28))
        self.start_boucle_btn.setObjectName("start_boucle_btn")
        self.fin_boucle_btn = QtWidgets.QPushButton(self.centralwidget)
        self.fin_boucle_btn.setGeometry(QtCore.QRect(470, 830, 93, 28))
        self.fin_boucle_btn.setObjectName("fin_boucle_btn")
        self.code_btn = QtWidgets.QPushButton(self.centralwidget)
        self.code_btn.setGeometry(QtCore.QRect(600, 790, 101, 28))
        self.code_btn.setObjectName("code_btn")
        self.text_lbl = QtWidgets.QLabel(self.centralwidget)
        self.text_lbl.setGeometry(QtCore.QRect(10, 750, 111, 16))
        self.text_lbl.setObjectName("text_lbl")
        self.text_led = QtWidgets.QLineEdit(self.centralwidget)
        self.text_led.setGeometry(QtCore.QRect(120, 741, 581, 31))
        self.text_led.setObjectName("text_led")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.start_func_btn.clicked.connect(lambda: self.drawFonction(self.start_func_btn))
        self.fin_func_btn.clicked.connect(lambda: self.drawFonction(self.fin_func_btn))
        self.start_boucle_btn.clicked.connect(lambda: self.drawBoucle(self.start_boucle_btn))
        self.fin_boucle_btn.clicked.connect(lambda: self.drawBoucle(self.fin_boucle_btn))
        self.input_btn.clicked.connect(lambda: self.drawInOut(self.input_btn))
        self.output_btn.clicked.connect(lambda: self.drawInOut(self.output_btn))
        self.instruction_btn.clicked.connect(self.drawInstruction)
        self.condition_btn.clicked.connect(self.drawCondition)
        self.code_btn.clicked.connect(self.generateScript)

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
        self.text_lbl.setText(_translate("MainWindow", "Texte à afficher :"))

    # def recup_text(self):
    #     if self.text_led.text() == "":
    #        return "" 
    #     else:
    #         return self.text_led.text()

    def drawCondition(self):
        
        if self.text_led.text() == "":
           texte = "" 
        else:
            texte = self.text_led.text()
        
        #texte = self.recup_text(self)
        newCondition = Condition(texte)
        drawnCond, textCond = newCondition.draw()
        list_object.append(newCondition)
        scene.addItem(drawnCond)
        scene.addItem(textCond)
        self.graphicsView.setScene(scene)
        self.graphicsView.show()
    
    def drawFonction(self,b):
        
        name = b.objectName()
        
        if name == "start_func_btn":
            texte = "Début de la fonction"
            
        if name == "fin_func_btn":
            texte = "Fin de la fonction"
                    
        newFonction = Fonction(texte)
        drawFonc,textFonc = newFonction.draw()
        list_object.append(newFonction)
        scene.addItem(drawFonc)
        scene.addItem(textFonc)
        self.graphicsView.setScene(scene)
        self.graphicsView.show()
        
    def drawBoucle(self,b):
        
        name = b.objectName()
        
        if name == "start_boucle_btn":
            if self.text_led.text() != "":
                texte = self.text_led.text()
        elif name == "fin_boucle_btn":
            texte = "Fin de la boucle"
                    
        newBoucle = Boucle(texte)
        list_object.append(newBoucle)
        drawBoucle,textBoucle = newBoucle.draw()
        scene.addItem(drawBoucle)
        scene.addItem(textBoucle)
        self.graphicsView.setScene(scene)
        self.graphicsView.show()

    def drawInOut(self,b):
                
        if self.text_led.text() == "":
           texte = "" 
        else:
            texte = self.text_led.text()
        
        newEntry = EntreeSortie(texte)
        list_object.append(newEntry)
        drawnIO,textIO = newEntry.draw()
        scene.addItem(drawnIO)
        scene.addItem(textIO)
        self.graphicsView.setScene(scene)
        self.graphicsView.show()
    
    def drawInstruction(self):
        if self.text_led.text() == "":
           texte = "" 
        else:
            texte = self.text_led.text()
        newInst = Instruction(texte)
        list_object.append(newInst)
        drawInst,textInst = newInst.draw()
        scene.addItem(drawInst)
        scene.addItem(textInst)
        self.graphicsView.setScene(scene)
        self.graphicsView.show()

    def generateScript(self):
        generateCode.generateCode(list_object)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.quit())

