# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:36:46 2022

@author: Utilisateur
"""

from Boucle import Boucle
from Condition import Condition
from EntreeSortie import EntreeSortie
from Fonction import Fonction
from Instruction import Instruction


def generateCode(liste_forme) : 
    
    print("Je suis à l'entrée de la fonction")
    
    fichier = open("script_final.py", "w")
    
    print("Fichier ouvert")
    print(liste_forme)
    
    for x in liste_forme:
                
        print("Je suis dans la boucle")
        print(type(x))
        
        text = x.text
        
        if isinstance(x,Instruction):
            fichier.write(text+"\n") 
            
        if isinstance(x, EntreeSortie):
            if text.startswith("Demander"):
                commande = text[9:]+"="+"input('Saisisssez la valeur de "+ text[9:] +" : ')\n"
                
            if text.startswith("Afficher"):
                commande = "print("+text[9:]+")\n"
                
            fichier.write(commande)
        
        if isinstance(x, Condition):
            commande = "if "+text[3:]+": \n"
            fichier.write(commande)
        
        if isinstance(x, Boucle):
            if text.startswith("Pour"):
                #Pour i allant de 0 à 10
               words = text.split()
               commande =  "for "+words[1]+" in range("+words[4]+","+words[6]+"):\n"
               
            if text.startswith("Tant que"): 
                commande = "while "+text[9:]+":\n"
            
            if text.startswith("Fin"):
                print("Fin de boucle")
            
            fichier.write(commande)
            
        #if isinstance(x, Fonction)
    
    fichier.close()