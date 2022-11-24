#Creation de la grille de jeux avec 3 liste
def afficher_grille(grille):
    print("     0)  1)  2)")
    print("   -------------")
    print("0)", end='')
    for i in range(3):
        print(" | "+str(grille[i]), end='')
    print(" |")
    print("   -------------")
    print("1)", end='')
    for i in range(3):
        print(" | "+str(grille[i+3]), end='')
    print(" |")
    print("   -------------")
    print("2)", end='')
    for i in range(3):
        print(" | "+str(grille[i+6]), end='')
    print(" |")
    print("   -------------")
 
#Le tour demande au joueur a qui c'est le tour les coordonner ou il veux jouer tout en verifiant que c'est possible de jouer a celle ci
def tour(grille, joueur):
    print("C'est le tour du joueur "+str(joueur))
    colonne=input("Entrez le numero de la colonne : ")
    ligne=input("Entrez le numero de la ligne : ")
    print("Vous avez joué la case ("+colonne+","+ligne+")")
    #tant que les coordonner (colonne + ligne * 3) n'est pas vide alors on rentre dans la boucle
    while grille[int(colonne)+int(ligne)*3]!=" ":
        afficher_grille(grille)
        print("Cette case est deja jouée ! Saisissez une autre case svp !")
        colonne=input("Entrez le numero de la colonne : ")
        ligne=input("Entrez le numero de la ligne : ")
        print("Vous avez joué la case ("+colonne+","+ligne+")")
    #ici cela permets au joueurs de bien jouer leur symbole associer
    if joueur==1 :
        grille[int(colonne)+int(ligne)*3]="X"
    if joueur==2 :
        grille[int(colonne)+int(ligne)*3]="O"
    afficher_grille(grille)

#On verifie ici si il y a un gagnant en comparant la premiere donner avec les possibilité pour gagné au morpions 
def est_gagnant(grille):
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
        return 1
    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]!=" "):
        return 1
    if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]!=" "):
        return 1
    if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]!=" "):
        return 1
    if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]!=" "):
        return 1
    if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]!=" "):
        return 1
    if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]!=" "):
        return 1
    if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]!=" "):
        return 1
 
 #Si toute case de la grille ne sont pas vide alors on retourne 1 pour signifier que le match est nul
def est_match_nul(grille):
    for i in range(9):
        if grille[i]==" ":
            return 0
    return 1
 
joueur=1
print("Le joueur 1 possède les X. Le joueur 2 possède les O")
grille=[" "," "," "," "," "," "," "," "," "]
afficher_grille(grille)
gagne=0
#Tant que gagne egal 0 alors on refait un tour
while gagne==0:
    tour(grille,joueur)
    #si est gagnant egal 1 alors on ecris le gagnant de la partie
    if est_gagnant(grille):
        print("Le joueur "+str(joueur)+" remporte la partie")
        gagne=1
    #sinon le match est nul
    else:
        if est_match_nul(grille):
            print("Plus de place ! Match nul !")
            gagne=1
    if joueur==1:
        joueur=2
    else:
        joueur=1
