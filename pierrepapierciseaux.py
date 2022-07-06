#!/usr/bin/python
# -*- coding: utf-8 -*-

# Projet de Pierre papier ciseaux

# Créer un pierre papier ciseaux est un bon exercice pour vous entraîner en
# Python et réaliser vos premiers projets.

# Au programme, vous devrez créer :

# une fonction qui génère de l’aléatoire : pierre, papier ou ciseaux
# une fonction pour vérifier et valider le coup qui vient d’être joué
# une fonction de résultat pour déclarer le vainqueur du tour
# un compteur de points pour suivre le score total

# Le programme demande à l’utilisateur d’effectuer le premier coup avant
# d’effectuer un coup. Une fois le coup validé, l’entrée est évaluée, l’entrée
# saisie pouvant être une chaîne de caractères, une lettre ou un nombre. Après
# évaluation de la chaîne de caractères, la fonction de résultat détermine le
# gagnant et la fonction de comptabilisation des points actualise le score
# total.

import random

# Définition du dictionnaire de jeu
jeudict = {1: "Pierre", 2: "Papier", 3: "Ciseaux"}
winlist = ['Vous avez gagné !', 'Egalité', 'L\'ordinateur a gagné']


# Fonction pour générer le jeu aléatoire de l'ordinateur
def generation_alea_turn():
    return random.randint(1, len(jeudict))


def main():
    scoredepartuser = 0
    scoredepartpc = 0
    scoreuser = scoredepartuser
    scorepc = scoredepartpc
    while True:
        if scoreuser == 10 or scorepc == 10:
            print('Fin de la partie.')
            break

        for i in jeudict.items():
            print(i)

        userturn = int(input('Que jouez-vous ?'))
        pcturn = generation_alea_turn()

        # Si l'utilisateur gagne
        if userturn == 1 and pcturn == 3:
            scoreuser = scoreuser + 1
            scorepc = scorepc
            print(winlist[0])
            print('Vous : {} - Ordinateur : {}'.format(scoreuser, scorepc))
        elif userturn == 2 and pcturn == 1:
            scoreuser = scoreuser + 1
            scorepc = scorepc
            print(winlist[0])
            print('Vous : {} - Ordinateur : {}'.format(scoreuser, scorepc))
        elif userturn == 3 and pcturn == 2:
            scoreuser = scoreuser + 1
            scorepc = scorepc
            print(winlist[0])
            print('Vous : {} - Ordinateur : {}'.format(scoreuser, scorepc))
        # Si vous avez joué le même coup
        elif userturn == pcturn:
            scoreuser = scoreuser
            scorepc = scorepc
            print(winlist[1])
            print('Vous : {} - Ordinateur : {}'.format(scoreuser, scorepc))
        # Sinon c'est l'ordinateur qui gagne
        else:
            scoreuser = scoreuser
            scorepc = scorepc + 1
            print(winlist[2])
            print('Vous : {} - Ordinateur : {}'.format(scoreuser, scorepc))

main()
