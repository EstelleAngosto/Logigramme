# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:34:22 2022

@author: Utilisateur
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsEllipseItem, QGraphicsTextItem
#import sys

class Boucle:
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
        
        boucle = QGraphicsEllipseItem(x,y,w,h)
        boucle.setBrush(QBrush(Qt.red))
        boucle.setFlag(QGraphicsItem.ItemIsMovable)
                
        texte = QGraphicsTextItem(text)
        dx = w/4
        dy = h/4
        texte.setPos(x + dx, y + dy)
        texte.setDefaultTextColor(Qt.black)
        texte.setFlag(QGraphicsItem.ItemIsMovable)
        
        return boucle,texte