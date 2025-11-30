tablero = [[0 for _ in range(5)] for _ in range(5)]
coordenadas = [(x, y) for x in range(5) for y in range(5)]
borde = [(x, y) for x in range(5) for y in range(5) if x == 0 or x == 4 or y == 0 or y == 4]

print("Tablero 5x5 creado")
print("Total coordenadas:", len(coordenadas))
print("Coordenadas del borde:", len(borde))
print("Primeras 5 coordenadas:", coordenadas[:5])
