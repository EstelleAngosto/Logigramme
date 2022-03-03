# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:31:43 2022

@author: Utilisateur
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsEllipseItem, QGraphicsTextItem

class Fonction:
    def __init__(self,texte):
        self.x = 0
        self.y = 0
        self.width = 200
        self.height = 100
        self.text = texte
        
    
    def draw(self):
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        text = self.text
                
        fonction = QGraphicsEllipseItem(x,y,w,h)
        fonction.setBrush(QBrush(Qt.blue))
        fonction.setFlag(QGraphicsItem.ItemIsMovable)
        
        texte = QGraphicsTextItem(text)
        dx = w/4
        dy = h/4
        texte.setPos(x + dx, y + dy)
        texte.setDefaultTextColor(Qt.black)
        texte.setFlag(QGraphicsItem.ItemIsMovable)

        return fonction,texte