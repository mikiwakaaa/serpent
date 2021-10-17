# -*- coding: utf-8 -*-

'''
Titre : le_serpent_siffle.py
Auteur : Miki Wakaaa
Version : 1.0

Date de la version courante : 22-04-21
Date de la version 1.0 : 22-04-21


- Traduction d'un source Serpent (en .serpe)
vers un source python.
- Un test de la bonne execution est effectué.

'''

import os
import glob

# dictionnaire des modifications
dico = dict()

def est_vide(mot):
    return mot.strip() == ''

# on construit le dictionnaire modif
def sifflet(fichier_csv):
    entree = open(fichier_csv, 'r')
    lignes = entree.readlines()
    for ligne in lignes:
        ligne = ligne.replace('\n', '')
        ligne = ligne.replace('\r', '')
        if est_vide(ligne):
            continue
        lst = ligne.split(',')
        if len(lst) < 2:
            print('le format du csv : "motif,mot-clef"',
                  "n'est pas respecté")
        x = lst[0].strip()
        y = lst[1].strip()
        dico[x] = y
    entree.close()

def traduction(nom_entree):
    entree = open(nom_entree, 'r')
    nom_sortie = nom_entree.replace('.serpe', '.py')
    print(nom_sortie + '...', end="")
    sortie = open(nom_sortie, 'w')
    lignes = entree.readlines()
    for ligne in lignes:
        for motif in dico.keys():
            ligne = ligne.replace(motif, dico[motif])
        # print(ligne)
        sortie.write(ligne)
    entree.close()
    sortie.close()
    print('[OK]')
    os.system('python' + nom_sortie + '.py')
    
if __name__ == '__main__':
    # constructio du dictionnaire de traduction
    sifflet('sifflet.csv')
    
    sources_serpent = glob.glob('progremmes_serpent/*.serpe')
    for source in sources_serpent:
        traduction(source)
