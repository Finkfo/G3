# Import des bibliotheques necessaires au programme
from player import *

# Class Human - Implementation de Player pour le joueur
class Human(Player):
    def play(self , game):
        colonne=input("Entrez le numero de la colonne : ")
        ligne=input("Entrez le numero de la ligne : ")
        return (colonne, ligne)