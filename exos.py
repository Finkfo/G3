#DEBUT
#add(x,y)
#sub(x,y)
#multiply(x,y)
#divide(x,y)
#modulo(x,y)

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divideDeMerde(x,y):
    return x/y

def modulo(x,y):
    return x%y

def salaireNet(salaireBrut, coefficient):
    return salaireBrut*coefficient

def calculSalParSec(salaireHoraire, heureParJO, jO):
    #Calculer mon salaire annuel
    salaireAnnuel = salaireHoraire * heureParJO * jO
    #Calculer le nombre de secondes dans une année
    nbSecondeParAn = 365 * 24 * 60 * 60 
    #Je pose et retourne la division
    return salaireAnnuel / nbSecondeParAn

#Definir une fonction withdrawFees qui retire un pourcentage total en fonction d'un total et d'un pourcentage
def withdrawFees(total, percent):
    #Definir fees en fonction d'un total et d'un pourcentage
    fees = total * (percent/100)
    #Soustraire fees au total
    result = total - fees
    #retourner la valeur obtenue
    return result

#Definir une fonction qui retourne le salaire net en fonction du salaire brut (float) et du secteur d'activité (isPublic > booleen) 
def calculBrutEnNet(salaireBrut, isPublic):
    #Si je suis un travailleur du secteur publique
    if isPublic:
        #Alors je soustrais 15% de mon salaire Brut a mon salaire Brut et je l'assigne a la variable salaireNet
        salaireNet = withdrawFees(salaireBrut, 15)
    #Sinon : Je suis un travailleur du secteur privé
    else:
        #Alors je soustrais 23% de mon salaire Brut a mon salaire Brut et je l'assigne a la variable salaireNet
        salaireNet = withdrawFees(salaireBrut, 23)
    #Retourner salaireNet
    return salaireNet

#Definir une divison de x par y
def divide(x,y):
    #Si y est egal à zero
    if y==0:
        #Alors je retourne que la division par zero n'est pas possible
        print("ERROR : cannot divided by 0")
        #retourner vide
        return
    #Sinon: y est different de 0
    else:
        #Alors je retourne la divison entre x est y
       return x/y
 
import random
import string
    
def input():#Renvoie un caractere de type string au hasard
    return random.choice(string.ascii_letters)

#Exercice:
    #Faire un mini jeu qui affiche un message lorsque  input renvoie le bon caractere
    #le caractere doit etre parametrable

#Definir mingame
def minigame(characwinner):
    guess = None
    count = 0
    #Tant que input est different de characwinner
    while guess!=characwinner:
        #Demander un nouveaux guess
        guess = input()
        count += 1
    #Prevenir de l'input gagant et fin du jeu
    print("Votre Charactere a été trouver en",count,"Féliciations")

#demande la lettre a trouver
#enlever le hashtag en dessous pour jouer
#recherche = str(input("qu'elle est ta lettre :"))

#definir la classe minigame avec un compteur a 0
def maxigame(recherche, compteur=0):
    #augmenter le compteur
    compteur = compteur + 1
    #importer les caractere aleatoire
    caractereGagnant = str(input())
    #si cractere rechercher et cractere aleatoire sont pareil
    if recherche == caractereGagnant:
        #alors ecrire en combien d'etapes le robot la trouver
        print ("Ta lettre a etais trouvé en "+str(compteur)+ " étapes")
    #sinon on recommence
    else:
        maxigame(recherche, compteur)

maxigame("h")
#FIN