# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:28:19 2022

@author: Utilisateur
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem, QGraphicsTextItem
#import sys

class EntreeSortie:
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
        
        inOut = QGraphicsRectItem(x,y,w,h)
        inOut.setBrush(QBrush(Qt.green))
        inOut.setFlag(QGraphicsItem.ItemIsMovable)
        
        texte = QGraphicsTextItem(text)
        dx = w/4
        dy = h/4
        texte.setPos(x + dx, y + dy)
        texte.setDefaultTextColor(Qt.black)
        texte.setFlag(QGraphicsItem.ItemIsMovable)
        
        return inOut,texte