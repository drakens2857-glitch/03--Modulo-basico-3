import datetime
import functools

def log_actividad(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Ejecutando: {func.__name__}")
        try:
            resultado = func(*args, **kwargs)
            print(f"[{timestamp}] {func.__name__} completada exitosamente")
            return resultado
        except Exception as e:
            print(f"[{timestamp}] Error en {func.__name__}: {e}")
            raise
    return wrapper

@log_actividad
def crear_guerrero(nombre, clase):
    if not nombre or not clase:
        raise ValueError("Nombre y clase son requeridos")
    guerrero = {"nombre": nombre, "clase": clase, "nivel": 1, "experiencia": 0}
    return guerrero

try:
    nuevo_guerrero = crear_guerrero("Thorin", "Guerrero")
    print("Guerrero creado:", nuevo_guerrero)
    guerrero_error = crear_guerrero("", "Mago")
except ValueError as e:
    print(f"Error capturado: {e}")
