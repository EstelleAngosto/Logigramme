# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:34:21 2022

@author: Utilisateur
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem, QGraphicsTextItem
#import sys

class Condition:
    def __init__(self,texte):
        self.x = 0
        self.y = 0
        self.width = 200
        self.height = 200
        self.text = texte

    def draw(self):
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        texte = self.text
        
        condition = QGraphicsRectItem(x,y,w,h)
        condition.setBrush(QBrush(Qt.magenta))
        condition.setFlag(QGraphicsItem.ItemIsMovable)
        
        texte = QGraphicsTextItem(texte)
        dx = w/4
        dy = h/4
        texte.setPos(x + dx, y + dy)
        texte.setDefaultTextColor(Qt.black)
        texte.setFlag(QGraphicsItem.ItemIsMovable)
        
        condition.setRotation(45)

        return condition,texte
    