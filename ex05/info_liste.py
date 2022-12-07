def affiche_info(mon_dict):
    equivalent_cle_phrase = {
        'nb_elem': 'Le nombre d\'éléments dans la liste',
        'first' : 'le 1er élément dans la liste',
        'last' : 'le dernier élément dans la liste'

    }

    for cle,valeur in mon_dict.items():
        phrase = equivalent_cle_phrase[cle]
        print(phrase,valeur)

def info_list(ma_liste):
    taille_liste = len(ma_liste)
    dict_a_retourner = {}
    dict_a_retourner['nb_elem'] = taille_liste
    if taille_liste>0:
            premier = ma_liste[0]
            dernier = ma_liste[-1]
            dict_a_retourner['first'] = premier
            dict_a_retourner['last'] = dernier
    return dict_a_retourner

def traitement(ma_liste):
    retour_info = info_list(ma_liste)
    affiche_info(retour_info)
