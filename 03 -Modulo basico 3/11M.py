guerreros = [
    {"nombre": "Thor", "nivel": 25, "ataque": 45},
    {"nombre": "Legolas", "nivel": 30, "ataque": 40},
    {"nombre": "Gandalf", "nivel": 50, "ataque": 35}
]

por_nivel = sorted(guerreros, key=lambda x: x["nivel"], reverse=True)
por_ataque = sorted(guerreros, key=lambda x: x["ataque"], reverse=True)
por_nombre = sorted(guerreros, key=lambda x: x["nombre"])

print("Por nivel:", [g["nombre"] for g in por_nivel])
print("Por ataque:", [g["nombre"] for g in por_ataque])
print("Por nombre:", [g["nombre"] for g in por_nombre])

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))
mayores_5 = list(filter(lambda x: x > 5, numeros))
guerreros_elite = list(filter(lambda g: g["nivel"] >= 30, guerreros))

print("Números pares:", pares)
print("Mayores a 5:", mayores_5)
print("Guerreros elite:", [g["nombre"] for g in guerreros_elite])

poder_total = list(map(lambda g: g["nivel"] + g["ataque"], guerreros))
mensajes = list(map(lambda g: f"{g['nombre']} (Nivel {g['nivel']})", guerreros))
cuadrados = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))

print("Poder total:", poder_total)
print("Mensajes:", mensajes)
print("Cuadrados:", cuadrados)

