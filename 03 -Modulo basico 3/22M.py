@log_actividad
@medir_tiempo
@validar_nivel
def calcular_poder_total(nivel, ataque_base=20):
    poder = (nivel ** 2) + (ataque_base * nivel) + 100
    return poder

try:
    poder = calcular_poder_total(30, ataque_base=25)
    print(f"Poder total calculado: {poder}")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
