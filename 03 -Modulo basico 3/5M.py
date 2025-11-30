def clasificar_guerrero(nivel):
    if nivel >= 50:
        categoria = "Legendario"
        bonificacion = 100
    elif nivel >= 30:
        categoria = "Experto"
        bonificacion = 50
    elif nivel >= 15:
        categoria = "Veterano"
        bonificacion = 25
    elif nivel >= 5:
        categoria = "Novato"
        bonificacion = 10
    else:
        categoria = "Principiante"
        bonificacion = 0
    return categoria, bonificacion


nivel_jugador = 22
categoria, bonus = clasificar_guerrero(nivel_jugador)
print(f"Nivel {nivel_jugador}: {categoria} (Bonus: +{bonus} puntos)")


def evaluar_combate(vida_jugador, vida_enemigo, tiene_pocion):
    if vida_jugador <= 0:
        return "¡Has sido derrotado! Game Over"
    elif vida_enemigo <= 0:
        return "¡Victoria! Has derrotado al enemigo"
    elif vida_jugador < 20 and tiene_pocion:
        return "Vida crítica - Recomendación: Usar poción"
    elif vida_jugador < 20 and not tiene_pocion:
        return "Vida crítica - ¡Busca una poción urgente!"
    else:
        return "Combate en progreso - Continúa luchando"


print(evaluar_combate(15, 45, True))
print(evaluar_combate(15, 45, False))
print(evaluar_combate(80, 0, True))
