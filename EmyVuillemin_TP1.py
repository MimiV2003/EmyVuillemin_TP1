#TP1 EmyVuillemin
#Importe-----------------------------------------------------------------------------------------------------

import sys
import json
import os #Affiche le nom, la taille en memoire et le nbr element du fichier

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QLabel
)

#----------------------------------------------------------------------------------------------------------
#Creation de la fenetre, son conteneur principale, barre de recherche et affichage de donnee---------------

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.data = data

        #Widget principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        #-------------------------------------------------------------------------------------------------------
        #Affichage du nom du fichier, taille de memoire, nbr element du fichier---------------------------------

        #QLabel sert a afficher le texte dans le MainWindow
        #Le f sert inserer directement les variables dans une chaine de caracteres
        #basename recupere nom du fichier
        #QVBoxLayout organise les widgets verticalement
        #os.path.getsize sert a obtenir la taille du fichier

        self.file_info = QLabel(f"Nom : {os.path.basename(json_file)} | "f"Taille : {os.path.getsize(json_file)} octets | "f"Nombre d'elements : {len(data)}" )

        layout.addWidget(self.file_info)#Met la barre de recherche en dessous

        #-------------------------------------------------------------------------------------------------------
        #Barre de recherche-------------------------------------------------------------------------------------

        self.searchbar = QLineEdit() #Creation de la barre
        self.searchbar.setPlaceholderText("Rechercher...") #Affichage du texte sur la barre
        self.searchbar.textChanged.connect(self.update_display) #Chaque fois que le texte change va appeler la fonction (update_display)
        #Grace a cette fonction, dès la premiere lettre ou chiffre = trie deja le resultat

        layout.addWidget(self.searchbar) #Ajoute

        self.tableau = tableau
        layout.addWidget(self.tableau) #Met le tableau en dessous de la barre de recherche

        self.setCentralWidget(central_widget)

    #----------------------------------------------------------------------------------------------------------
    #Filtrage--------------------------------------------------------------------------------------------------

    def update_display(self, text):

        #Nettoyage
        search = text.strip().casefold() #Strip ca enleve les espaces
        #Casefold permet de faire une recherche peut importe la minuscule/majuscule

        for row in range(self.tableau.rowCount()): #Nbr de lignes

            found = False

            for column in range(self.tableau.columnCount()): #Parcours les colonnes

                item = self.tableau.item(row, column) #Trouve la bulle
                #Row = ranger et Column = colonne

                if item and search in item.text().casefold(): #Assurer que le texte rechercher est bien dans cette bulle du tableau

                    found = True
                    break

            self.tableau.setRowHidden(row, not found) #Cache ou affiche la ligne

#-------------------------------------------------------------------------------------------------------
# Utilisation du JSON file------------------------------------------------------------------------------

json_file = sys.argv[1]
# tableau 1 c'est le large
# tableau 2 c'est le small

print("JSON FILE >>>>>>>> " + json_file +  "<<<<<<<<<<")

try:
    file = open(json_file, encoding= "utf-8") #Grace a utf-8, les caracteres speciaux sont visible
    data = json.load(file)
    print(type(data))

    #Imprime seulement dans la console et non dans le window
    print("Nom du fichier :", os.path.basename(json_file))
    print("Taille du fichier :", os.path.getsize(json_file), "octets")
    print("Nombre d'elements:", len(data))

except:
    print(f"Could not load data from {json_file}")
    

#--------------------------------------------------------------------------------------------------------
#Croissant/Decroissant-----------------------------------------------------------------------------------

def trier(tableau):

    #Ordre croissant et decroissant
    tableau.setSortingEnabled(True) #Par contre marche seulement par ordre alphabethique 
    #Doit cliquer sur une colonne pour changer l'ordre /Chaque colone a son ordre
    #De plus, capte seulement le premier chiffre du nombre par ordre croi/decroi.
    #Exemple: le 28500 est considere plus petit que 3200 car le premier chiffre est 2

#-----------------------------------------------------------------------------------------------------
#Tableau----------------------------------------------------------------------------------------------

app = QApplication([])

tableau = QTableWidget()
tableau.setRowCount(len(data))
tableau.setColumnCount(len(data[0])) #0 pour la premiere ligne (seulement la premiere boite)
tableau.setHorizontalHeaderLabels(list(data[0].keys()))

#------------------------------------------------------------------------------------------------------
#Mettre les donnees dans le QTableWidget (Remplissage de tableau)--------------------------------------

for i in range(len(data)): #ligne par ligne
    item = data[i]
    list(item.keys())
    for t in range(len(list(data[i].keys()))): #Chaque information triee, t = colonne, i = items
        tableau.setItem(i, t, QTableWidgetItem(str(item[list(item.keys())[t]]))) #str pour pouvoir mettre des nombres

#----------------------------------------------------------------------------------------------------------
#Execute---------------------------------------------------------------------------------------------------

trier(tableau)#Fonction pour mettre en ordre

window = MainWindow();

window.resize(tableau.horizontalHeader().length() + tableau.verticalHeader().width() + 30, 500) #Taille du tableau

window.show()
sys.exit(app.exec())

#Fin--------------------------------------------------------------------------------------------------------