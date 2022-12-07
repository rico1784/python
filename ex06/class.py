class Ville:
    def __init__(self, nom, code_postal, nom_maire):
        self.nom = nom
        self.code_postal = code_postal
        self.nom_maire = nom_maire
        self.debug = False
        self.commentaire = "43443"

    def afficheNom(self):
        print(self.nom)

    def changeEtatDebug(self, nouvel_etat):
        self.debug = nouvel_etat
        return self.debug

    def majCommentaire(self, nouveau_com, garderOuEffacer):
        if nouveau_com[-1] != '.':
            nouveau_com+='.'
        if garderOuEffacer == True:
            self.commentaire = nouveau_com
        else:
            self.commentaire = self.commentaire + ' ' + nouveau_com



toulouse = Ville("Toulouse", "34400", "Jean-Luc Moudenc")
paris = Ville("Paris", "31000", "Anne Hidalgo")

liste_de_villes = [toulouse, paris]
for ma_ville in liste_de_villes:
    print('le code postal de', ma_ville.nom, 'est', ma_ville.code_postal)