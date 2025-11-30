import json

def cargar_perfil_jugador(archivo="perfil.json"):
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            perfil = json.load(file)
            jugador = {}
            jugador.update(perfil["informacion_basica"])
            jugador.update(perfil["estadisticas"])
            jugador.update(perfil["inventario"])
            jugador.update(perfil["progreso"])
            return jugador
    except FileNotFoundError:
        print("No se encontró archivo de perfil. Creando nuevo jugador...")
        return None
    except json.JSONDecodeError:
        print("Error al leer el archivo. Archivo corrupto.")
        return None


jugador_cargado = cargar_perfil_jugador()
if jugador_cargado:
    print(f"¡Bienvenido de vuelta, {jugador_cargado['nombre']}!")
    print(f"Nivel: {jugador_cargado['nivel']}")
    print(f"Oro disponible: {jugador_cargado['oro']}")
