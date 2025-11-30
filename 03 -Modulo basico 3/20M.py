import functools

def validar_nivel(func):
    @functools.wraps(func)
    def wrapper(nivel, *args, **kwargs):
        if not isinstance(nivel, int):
            raise TypeError("El nivel debe ser un número entero")
        if nivel < 1 or nivel > 100:
            raise ValueError("El nivel debe estar entre 1 y 100")
        return func(nivel, *args, **kwargs)
    return wrapper

@validar_nivel
def subir_nivel(nivel, nombre_guerrero):
    experiencia_necesaria = nivel * 1000
    return f"{nombre_guerrero} subió al nivel {nivel}. Experiencia necesaria: {experiencia_necesaria}"

try:
    print(subir_nivel(25, "Thor"))
    print(subir_nivel(150, "Legolas"))
except (TypeError, ValueError) as e:
    print(f"Error de validación: {e}")
