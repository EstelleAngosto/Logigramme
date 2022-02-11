# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:31:43 2022

@author: Utilisateur
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem

class Fonction():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 20
        self.height = 10
        
    
    def draw(self):
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        
        fonction = QGraphicsRectItem(x,y,w,h)
        return fonction