def guardar_jugador(nombre, nivel, puntos, archivo="jugador.txt"):
    with open(archivo, 'w') as file:
        file.write(f"Nombre: {nombre}\n")
        file.write(f"Nivel: {nivel}\n")
        file.write(f"Puntos: {puntos}\n")
    print(f"Datos de {nombre} guardados exitosamente")


guardar_jugador("Thor", 25, 15420)
