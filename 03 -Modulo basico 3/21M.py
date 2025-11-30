import functools
import random

def repetir(veces):
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            resultados = []
            for i in range(veces):
                resultado = func(*args, **kwargs)
                resultados.append(resultado)
            return resultados
        return wrapper
    return decorador

@repetir(3)
def lanzar_dado():
    return random.randint(1, 6)

@repetir(5)
def generar_stat_aleatoria():
    return random.randint(10, 20)

print("Lanzamientos de dado:", lanzar_dado())
print("Stats aleatorias:", generar_stat_aleatoria())
