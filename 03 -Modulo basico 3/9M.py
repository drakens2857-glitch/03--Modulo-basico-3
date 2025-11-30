import json

def guardar_perfil_jugador(jugador, archivo="perfil.json"):
    perfil = {
        "informacion_basica": {
            "nombre": jugador["nombre"],
            "nivel": jugador["nivel"],
            "experiencia": jugador["experiencia"]
        },
        "estadisticas": {
            "vida_maxima": jugador["vida_maxima"],
            "ataque": jugador["ataque"],
            "defensa": jugador["defensa"],
            "velocidad": jugador["velocidad"]
        },
        "inventario": {
            "armas": jugador["armas"],
            "armaduras": jugador["armaduras"],
            "pociones": jugador["pociones"],
            "oro": jugador["oro"]
        },
        "progreso": {
            "misiones_completadas": jugador["misiones_completadas"],
            "enemigos_derrotados": jugador["enemigos_derrotados"],
            "tiempo_jugado": jugador["tiempo_jugado"]
        }
    }
    with open(archivo, 'w', encoding='utf-8') as file:
        json.dump(perfil, file, indent=4, ensure_ascii=False)
    print(f"Perfil de {jugador['nombre']} guardado exitosamente")


mi_jugador = {
    "nombre": "DragonSlayer",
    "nivel": 25,
    "experiencia": 15420,
    "vida_maxima": 150,
    "ataque": 45,
    "defensa": 30,
    "velocidad": 25,
    "armas": ["Espada Flamígera", "Arco Élfico", "Daga Venenosa"],
    "armaduras": ["Casco de Hierro", "Peto de Cuero"],
    "pociones": ["Poción de Vida", "Poción de Maná"],
    "oro": 2500,
    "misiones_completadas": 12,
    "enemigos_derrotados": 89,
    "tiempo_jugado": "15 horas 30 minutos"
}

guardar_perfil_jugador(mi_jugador)
