# Import des bibliotheques necessaires au programme
from player import *

# Class Human - Implementation de Player pour le joueur
class Human(Player):
    def play(self):
        colonne=int(input("Entrez le numero de la colonne : "))
        ligne=int(input("Entrez le numero de la ligne : "))
        return (colonne, ligne)