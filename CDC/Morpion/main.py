#!/usr/local/bin/python3

# Jeu du morpion
# Le joueur commence a jouer en premier, l'ordinateur joue ensuite

# Import des bibliotheques necessaires au programme
from game import *
from player import *
from human import *



# Choix de la configuration
print("1 - Joueur contre joueur\n2 - Joueur contre ordinateur\n3 - Ordinateur contre joueur\n4 - Ordinateur contre ordinateur\n")
config = 0
while config < 1 or config > 2:
    config = int(input("Choisissez une configuration : "))

if config == 1:
    Game(3, Human("X"), Human("O")).start()
