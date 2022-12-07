def affiche_temps_actuel(temps_actuel):
    if temps_actuel == "beau":
        print('temps actuel :', temps_actuel, 'je dois prendre une casquette')

    elif temps_actuel == "pluie":
        print('temps actuel :', temps_actuel, 'je dois prendre un parapluie')

    elif temps_actuel == "orage":
        print('temps actuel :', temps_actuel, 'je ne dois pas sortir')

    else:
        print('temps actuel :', temps_actuel, 'Je dois prendre un manteau')

affiche_temps_actuel('pluie')
