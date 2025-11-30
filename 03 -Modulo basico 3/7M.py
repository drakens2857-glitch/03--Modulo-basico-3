def cargar_jugador(archivo="jugador.txt"):
    try:
        with open(archivo, 'r') as file:
            lineas = file.readlines()
            datos = {}
            for linea in lineas:
                clave, valor = linea.strip().split(": ")
                if clave in ["Nivel", "Puntos"]:
                    datos[clave] = int(valor)
                else:
                    datos[clave] = valor
            return datos
    except FileNotFoundError:
        print("Archivo no encontrado. Creando nuevo jugador...")
        return None


datos_jugador = cargar_jugador()
if datos_jugador:
    print(f"Bienvenido de vuelta, {datos_jugador['Nombre']}!")
