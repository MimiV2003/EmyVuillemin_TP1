#TP1 EmyVuillemin
#Importe

import sys
import json

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem
)


#Commencer par le data_small.json

json_file = sys.argv[1]

print("JSON FILE >>>>>>>> " + json_file +  "<<<<<<<<<<")

try:
    file = open(json_file)
    data = json.load(file)
    print(type(data))
except:
    print(f"Could not load data from {json_file}")

for i in data:
    print("Keys\n")
    for k in i.keys():
        print(f"     - {k}")
    print("\n")
    print("Values\n")
    for v in i.values():
        print(f"     - {v}")
    print("\n")
    print("items\n")
    for e in i.items():
        print(f"     - {e}")
    print("\n")

app = QApplication([])

tableau = QTableWidget()
tableau.setRowCount(3)
tableau.setColumnCount(3)
tableau.setHorizontalHeaderLabels(["name", "price", "type"])

# fill the form
for i in range(len(data)):
    item = data[i]
    tableau.setItem(i, 0, QTableWidgetItem(item["name"]))
    tableau.setItem(i, 1, QTableWidgetItem(item["price"]))
    tableau.setItem(i, 2, QTableWidgetItem(item["type"]))

window = QMainWindow();
window.setCentralWidget(tableau)
window.show()
sys.exit(app.exec())
