import random

objetos_ids = [f"item_{i:03d}" for i in range(1, 11)]
stats_aleatorias = [random.randint(10, 50) for _ in range(10)]
inventario = ["espada", "pocion", "escudo", "arco", "pocion", "gema"]
inventario_limpio = [item.title() for item in inventario if item != "pocion"]

print("IDs de objetos:", objetos_ids[:5])
print("Stats aleatorias:", stats_aleatorias[:5])
print("Inventario limpio:", inventario_limpio)
