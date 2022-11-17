#Definir la fonction afficher_grille(grille) qui creer la grile de jeu du morpion
    #Afficher "     0)  1)  2)"
    #Afficher "   -------------"
    #Afficher "0)", end='' 'end' qui incremente un espace vide a la fin
    #Pour i de 0 à 3
        #Afficher " | "+str(grille[i]), end=''
    #Afficher " |"
    #Afficher "   -------------"
    #Afficher "1)", end='' 'end' qui incremente un espace vide a la fin
    #Pour 1 de 0 à 3
        #Afficher " | "+str(grille[i+3]), end=''
    #Afficher " |"
    #Afficher "   -------------"
    #Afficher "2)", end='' 'end' qui incremente un espace vide a la fin
    #Pour 1 de 0 à 3
        #Afficher " | "+str(grille[i+6]), end=''
    #Afficher " |"
    #Afficher "   -------------"


#Definir la fonction tour(grille, joueur) qui permets a un joueur de mettre son pions dans la grille
    #Afficher "C'est le tour du joueur "+str(joueur)
    #colonne est egal aux chiffre ecris par le joueur
    #ligne est egal aux chiffre ecris par le joueur
    #Afficher "Vous avez joué la case ("+colonne+","+ligne+")"
    #Tant que la colonne et la ligne selectionné ne sont pas vide dans la grille
        #on retourne la fonction afficher_grille() avec grille en parametre
        #Afficher "Cette case est deja jouée ! Saisissez une autre case svp !"
        #colonne est egal aux chiffre ecris par le joueur
        #ligne est egal aux chiffre ecris par le joueur
        #Afficher "Vous avez joué la case ("+colonne+","+ligne+")"
    #Si joueur est egal à 1
        #Le signe X serait Afficher au coordonnées de la colonne et de la ligne dans la grille
     #Si joueur est egal à 2
        #Le signe O serait Afficher au coordonnées de la colonne et de la ligne dans la grille
    #on retourne la fonction afficher_grille() avec grille en parametre



#Definir la fonction est_gagnant(grille) qui retourne si il y a un gagnant en verifiant les données dans la grille
    #Si grille[0] est égal à grille[1] et grille[0] est égal à grille[2] et que grille[0] est different de " "
        #Alors retourner 1
    #Si grille[3] est égal à grille[4] et grille[3] est égal à grille[5] et que grille[3] est different de " "
        #Alors retourner 1
    #Si grille[6] est égal à grille[7] et grille[6] est égal à grille[8] et que grille[6] est different de " "
        #Alors retourner 1
    #Si grille[0] est égal à grille[3] et grille[6] est égal à grille[5] et que grille[0] est different de " "
        #Alors retourner 1
    #Si grille[1] est égal à grille[4] et grille[1] est égal à grille[7] et que grille[1] est different de " "
        #Alors retourner 1
    #Si grille[2] est égal à grille[5] et grille[2] est égal à grille[8] et que grille[2] est different de " "
        #Alors retourner 1
    #Si grille[0] est égal à grille[4] et grille[0] est égal à grille[8] et que grille[0] est different de " "
        #Alors retourner 1
    #Si grille[2] est égal à grille[4] et grille[2] est égal à grille[6] et que grille[2] est different de " "
        #Alors retourner 1


#Definir la fonction est_match_nul(grille)
    #Pour 1 de 0 à 9
        #Si i dans grille est egal à " "
            #Retourner 0
    #Retourner 1


#joueur egal à 1
#Afficher "Le joueur 1 possède les X. Le joueur 2 possède les O"
#grille égal [" "," "," "," "," "," "," "," "," "]
#gagne egal 0
#Tant que gagne est égal à 0
    #Lancer la fonction tour avec grille et joueur en parametre
    #Si la fonction est_gagnant avec grille en parametre
        #Afficher "Le joueur "+str(joueur)+" remporte la partie"
        #gagne egal 1
    #Sinon
        #Si la fonction est_match_nul avec grille en parametre
            #Afficher "Plus de place ! Match nul !"
            #gagne egal 1
    #Si joueur est egal à 1:
        #joueur egal 2
    #Sinon 
        #joueur egal 1
