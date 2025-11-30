import time
import functools

def medir_tiempo(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print(f"{func.__name__} tardó {tiempo_transcurrido:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def calcular_estadisticas_guerrero(nivel, clase):
    time.sleep(0.1)
    stats_base = {"Guerrero": 100, "Mago": 80, "Arquero": 90}
    vida = stats_base.get(clase, 85) + (nivel * 10)
    ataque = (nivel * 3) + 15
    defensa = (nivel * 2) + 10
    return {"vida": vida, "ataque": ataque, "defensa": defensa}

stats = calcular_estadisticas_guerrero(25, "Guerrero")
print("Estadísticas:", stats)
