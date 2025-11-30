nivel_jugador = 15
oro_disponible = 500
nivel_minimo = 10
costo_entrada = 300
puede_entrar = (nivel_jugador >= nivel_minimo) and (oro_disponible >= costo_entrada)
print(f"¿Puede entrar al dungeon? {puede_entrar}")

vida_actual = 30
tiene_pocion = True
tiene_hechizo = False
vida_critica = 50
necesita_curacion = vida_actual < vida_critica
puede_curarse = (tiene_pocion or tiene_hechizo) and necesita_curacion
print(f"¿Puede curarse? {puede_curarse}")

esta_envenenado = False
tiene_antidoto = True
puede_luchar = not esta_envenenado
print(f"¿Puede luchar? {puede_luchar}")
