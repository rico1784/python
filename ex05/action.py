from info_liste import traitement


liste_ville = ['paris','Lyon','Marseille','Toulouse','Bordeaux']
liste_vide = []

liste_saison = ['Eté','Hiver','Automne','Printemps']
liste_finale = [liste_ville,liste_vide,liste_saison]

for liste_courante in liste_finale:
    traitement(liste_courante)
