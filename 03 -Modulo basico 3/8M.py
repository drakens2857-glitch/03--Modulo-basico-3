def agregar_al_ranking(nombre, puntos, archivo="ranking.txt"):
    with open(archivo, 'a') as file:
        file.write(f"{nombre},{puntos}\n")


def mostrar_ranking(archivo="ranking.txt"):
    try:
        with open(archivo, 'r') as file:
            jugadores = []
            for linea in file:
                nombre, puntos = linea.strip().split(',')
                jugadores.append((nombre, int(puntos)))
            jugadores.sort(key=lambda x: x[1], reverse=True)
            print("=== RANKING DE JUGADORES ===")
            for i, (nombre, puntos) in enumerate(jugadores[:10], 1):
                print(f"{i:2d}. {nombre:<15} {puntos:>6} puntos")
    except FileNotFoundError:
        print("No hay ranking disponible aún.")
