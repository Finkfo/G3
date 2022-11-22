class Game:

    # Initialisation du tableau de jeu
    def __init__(self, size, player1, player2):
        self.size = size
        self.table = [["*" for x in range(size)] for y in range(size)]
        self.player1 = player1
        self.player2 = player2

    # Affichage du tableau de jeu
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

    def start(grille, joueur):
        print("C'est le tour du joueur "+str(joueur))

        print("Vous avez joué la case ("+colonne+","+ligne+")")
        #tant que les coordonner (colonne + ligne * 3) n'est pas vide alors on rentre dans la boucle
        while grille[int(colonne)+int(ligne)*3]!=" ":
            afficher_grille(grille)
            print("Cette case est deja jouée ! Saisissez une autre case svp !")

            print("Vous avez joué la case ("+colonne+","+ligne+")")
        #ici cela permets au joueurs de bien jouer leur symbole associer
        if joueur==1 :
            grille[int(colonne)+int(ligne)*3]="X"
        if joueur==2 :
            grille[int(colonne)+int(ligne)*3]="O"
        afficher_grille(grille)

    
    #Regarde si un joueur a gagne le match
    def win(grille):
        if (grille[0] == grille[1]) and (grille[0] == grille[2]) and (grille[0] != " "):
            return 1
        if (grille[3] == grille[4]) and (grille[3] == grille[5]) and (grille[3] != " "):
            return 1
        if (grille[6] == grille[7]) and (grille[6] == grille[8]) and (grille[6] != " "):
            return 1
        if (grille[0] == grille[3]) and (grille[0] == grille[6]) and (grille[0] != " "):
            return 1
        if (grille[1] == grille[4]) and (grille[1] == grille[7]) and (grille[1] != " "):
            return 1
        if (grille[2] == grille[5]) and (grille[2] == grille[8]) and (grille[2] != " "):
            return 1
        if (grille[0] == grille[4]) and (grille[0] == grille[8]) and (grille[0] != " "):
            return 1
        if (grille[2] == grille[4]) and (grille[2] == grille[6]) and (grille[2] != " "):
            return 1

    #Regarde si le match est nul
    def est_match_nul(grille):
        for i in range(9):
            if grille[i]==" ":
                return 0
        return 1
