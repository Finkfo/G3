class Computer(Player):
    #Definir la fonction play(self, game) qui permets de jouer le tour de l'ia
    def play(self, game):
        #Retourne la fonction bestMove qui va jouer le meilleur coup possible pour ce tour
        return self.bestMove(game, game.table, game.size, self.sign)[0]

    #Definir la fonction bestMove qui va selectionner la meilleure possibilitee de jeu
    def bestMove(self, game, table, size, sign):
        # Other recupera le signe de l'adversaire 
        other = ("X" if sign == "O" else "O")
        # On cree une liste vide pour y ajouter nos possibilitees avec leur score
        moves = list()

        # On parcours le tableau pour classer chaque possibilitee
        for x in range(size):
            for y in range(size):
                # Si la case est disponible
                if table[x][y] == " ":
                    # On fait une Deepcopy du tableau dans laquelle on joue (deepcopy pour recuperer le tableau et les donner dans le tableau)
                    copy = deepcopy(table)
                    #dans la copie on mets le signe de l'ia au coordonné
                    copy[x][y] = sign
                    # Et on recupere le resultat
                    win = game.win(copy)

                    # Si le tableau est plein et que personne ne gagne
                    if win == "*" and game.full(copy):
                        #alors score égal 0
                        score = 0
                    # Si il permet de gagner
                    elif win == sign:
                        #alors score égal 1
                        score = 1
                    # Sinon, on le grade avec l'oppose du score pour le joueur adverse
                    # pour son meilleur coup dans son jeu suivant
                    else:
                        score = 0 - self.bestMove(game, copy, size, other)[1]
                    result = ((x, y), score)

                    # Si le score est 1, on joue ce coup
                    if score == 1:
                        return result
                    # Sinon on l'ajoute dans la liste avec les autres et on continue
                    moves.append(result)

        # Une fois tous les coups dans la liste, on les trie par score
        shuffle(moves)
        moves.sort(key=lambda move: move[1], reverse=True)
        #Retourner le meilleur move
        return moves[0]
