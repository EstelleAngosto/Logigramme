# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:28:21 2022

@author: Utilisateur
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem
#import sys

class Instruction:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 200
        self.height = 200

    def draw(self):
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        
        instruction = QGraphicsRectItem(x,y,w,h)
        instruction.setBrush(QBrush(Qt.blue))
        instruction.setFlag(QGraphicsItem.ItemIsMovable)
        
        return instruction
    