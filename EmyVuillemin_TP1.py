#TP1 EmyVuillemin
#Importe

import sys
import json

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget
)


json_file = sys.argv[2]
# tableau 1 c'est le large
# tableau 2 c'est le small

print("JSON FILE >>>>>>>> " + json_file +  "<<<<<<<<<<")

try:
    file = open(json_file)
    data = json.load(file)
    print(type(data))
except:
    print(f"Could not load data from {json_file}")

def trier(tableau):

    #Ordre croissant et decroissant
    tableau.setSortingEnabled(True)#Par contre marche seulement par ordre alphabethique // Doit cliquer sur le tableau pour changer l'ordre

#-----------------------------------------------------------------------------------------------------
#Tableau

app = QApplication([])

tableau = QTableWidget()
tableau.setRowCount(len(data))
tableau.setColumnCount(len(data[0])) # 0 pour la premiere ligne (seulement la premiere boite)
tableau.setHorizontalHeaderLabels(list(data[0].keys()))

for i in range(len(data)):
    item = data[i]
    list(item.keys())
    for t in range(len(list(data[i].keys()))):
        tableau.setItem(i, t, QTableWidgetItem(str(item[list(item.keys())[t]])))# str pour pouvoir mettre des nombres

trier(tableau)

window = QMainWindow();

window.resize(tableau.horizontalHeader().length() + tableau.verticalHeader().width() + 30, 500)

window.setCentralWidget(tableau)

window.show()
sys.exit(app.exec())
