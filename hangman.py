#!/usr/bin/python3
#-*-Coding:utf-8 -*-

import os
import datetime
from random import choice
from unidecode import unidecode

# Sélectionner un mot au hasard
def word():
    f = open('mots.txt', 'r', encoding='utf8')
    contenu = f.readlines()
    return unidecode(choice(contenu)).upper().replace('\n', '')

# Remplacement par des underscores
def underscore(mot, L=[]):
    r = ''
    for i in mot:
        if i in L:
            r += i + ' '
        else:
            r += '_ '
    return r[:-1]

# Saisie du nom de l'utilisateur
def demander_nom():
    nom = input('Entrez votre nom : ')
    
    # Vérifier si le nom contient au moins une lettre
    if not any(char.isalpha() for char in nom):
        print("Le nom doit contenir au moins une lettre.")
        return demander_nom()  # Rappeler la fonction pour obtenir un nom valide
    
    return nom

# Saisie d'une lettre
def saisie(lettres_deja_proposees):
    lettre = input('Entrez une lettre : ').upper()
    
    # Vérifier si l'entrée est une seule lettre (A-Z ou a-z)
    if len(lettre) != 1 or not lettre.isalpha():
        print("Veuillez entrer une seule lettre.")
        return saisie(lettres_deja_proposees)  # Rappeler la fonction pour obtenir une entrée valide
    
    # Vérifier si la lettre a déjà été choisie
    if lettre in lettres_deja_proposees:
        print("Vous avez déjà choisi cette lettre.")
        return saisie(lettres_deja_proposees)  # Rappeler la fonction pour obtenir une nouvelle lettre
    else:
        return lettre

# Obtenir la date actuelle au format YYYY-MM-DD HH:MM:SS
def obtenir_date():
    maintenant = datetime.datetime.now()
    return maintenant.strftime("%Y-%m-%d %H:%M:%S")

# Afficher les scores
def afficher_scores():
    score_file = 'scores.txt'
    try:
        with open(score_file, 'r') as f:
            scores = f.readlines()
            if not scores:
                print("Aucun score enregistré.")
            else:
                print("Scores enregistrés :")
                for score in scores:
                    print(score.strip())  # Afficher chaque score sans les sauts de ligne
    except FileNotFoundError:
        print("Aucun score enregistré.")

# Fonction pour jouer
def jouer():
    nom_utilisateur = demander_nom()
    lettres_deja_proposees = []
    mot_a_deviner = word()
    affichage = underscore(mot_a_deviner)
    score = 0  # Initialiser le score
    print('Mot à deviner : ', affichage)
    nb_erreurs = 0

    while '_' in affichage and nb_erreurs < 11:
        lettre = saisie(lettres_deja_proposees)
        lettres_deja_proposees.append(lettre)
            
        if lettre not in mot_a_deviner:
            nb_erreurs += 1
        else:
            score += 10  # Augmenter le score si la lettre est correcte
                
        affichage = underscore(mot_a_deviner, lettres_deja_proposees)
        print('\nMot à deviner : ', affichage, ' ' * 10, 'Nombre d\'erreurs maximum :', 11 - nb_erreurs)

    # Message de défaite ou victoire
    if '_' in affichage:
        print('\nVous avez perdu. Le mot était :', mot_a_deviner)
    else:
        print('\nFélicitations ! Vous avez deviné le mot :', mot_a_deviner)

    # Enregistrement du score de l'utilisateur dans "scores.txt" avec la date
    date_format = obtenir_date()
    score_file = 'scores.txt'

    with open(score_file, 'a') as f:
        f.write(f'Nom : {nom_utilisateur}, Score : {score}, Date : {date_format}\n')

    # Afficher le score
    print(f'Votre score est de {score} points.')

# Programme principal
while True:
    print("\nMenu:")
    print("1. Jouer")
    print("2. Voir les scores")
    print("3. Quitter")
    
    choix = input("Choisissez une option : ").strip()
    
    if choix == '1':
        jouer()
    elif choix == '2':
        afficher_scores()
    elif choix == '3':
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")
