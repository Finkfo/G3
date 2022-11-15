#DEBUT

#On admet que la fonction random existe et qu'elle retourne un nombre aleatoirement
import random
#definir la fonction pierreFeuilleCiseau qui retourne si vous avez gagnez ou perdu contre l'IA par rapport a votre coup (joueurAction(string))
def pfcpc(joueurAction=""):
    #tableau iaCoup qui enregistre les differents coup possible pour l'IA(string) tableau = ["pierre","feuille","ciseau"]
    iaCoup = ["pierre", "feuille", "ciseau"]
    #variable iaAction qui recupere le retour de la fonction random.randrange(0,3) qui va recuperer une coup possible du tableau iaCoup
    iaAction = iaCoup[random.randrange(0,3)]
    #si joueurAction est égal à iaAction
    if (joueurAction == iaAction):
        #alors écrire joueurAction +"contre"+ iaAction +" , Egalité !"
        print(joueurAction +" contre "+ iaAction +", Égalité !")
    #sinon si joueurAction est égal à pierre et iaAction est égal à feuille
    elif (joueurAction == "pierre" and iaAction == "feuille"):
        #alors écrire pierre contre feuille , Perdu !
        print("Pierre contre Feuille, Perdu !")
    #sinon si joueurAction est égal à feuille et iaAction est égal à ciseau
    elif (joueurAction == "feuille" and iaAction == "ciseau"):
        #alors écrire feuille contre ciseau , Perdu !
        print("Feuille contre Ciseau, Perdu !")
    #sinon si joueurAction est égal à ciseau et iaAction est égal à pierre
    elif (joueurAction == "ciseau" and iaAction == "pierre"):
        #alors écrire ciseau contre pierre , Perdu !
        print("Ciseau contre Pierre, Perdu !")
    #sinon si joueurAction est égal à pierre et iaAction est égal à ciseau
    elif (joueurAction == "pierre" and iaAction =="ciseau"):
        #alors écrire pierre contre ciseau , Gagné !
        print("Pierre contre Ciseau, Gagné !")
    #sinon si joueurAction est égal à feuille et iaAction est égal à pierre
    elif (joueurAction == "feuille" and iaAction == "pierre"):
        #alors écrire feuille contre pierre , Gagné !
        print("Feuille contre Pierre, Gagné !")
    #sinon si joueurAction est égal à ciseau et iaAction est égal à feuille
    elif (joueurAction == "ciseau" and iaAction == "feuille"):
        #alors écrire ciseau contre feuille , Gagné !
        print("Ciseau contre Feuille, Gagné !")
#FIN

pfcpc(joueurAction="feuille")