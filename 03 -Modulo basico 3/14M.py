guerreros = [
    {"nombre": "Thor", "nivel": 25, "clase": "Guerrero"},
    {"nombre": "Legolas", "nivel": 30, "clase": "Arquero"},
    {"nombre": "Gandalf", "nivel": 50, "clase": "Mago"},
    {"nombre": "Gimli", "nivel": 28, "clase": "Guerrero"},
    {"nombre": "Aragorn", "nivel": 35, "clase": "Ranger"}
]

elite = [g["nombre"] for g in guerreros if g["nivel"] >= 30]
solo_guerreros = [g["nombre"] for g in guerreros if g["clase"] == "Guerrero"]
magos_rangers = [g["nombre"].upper() for g in guerreros if g["clase"] in ["Mago", "Ranger"]]

print("Elite:", elite)
print("Solo guerreros:", solo_guerreros)
print("Magos y Rangers:", magos_rangers)
