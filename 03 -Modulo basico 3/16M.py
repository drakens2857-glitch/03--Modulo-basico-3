palabras = ["python", "programacion", "juego", "aventura", "codigo"]

longitudes = [len(palabra) for palabra in palabras]
palabras_largas = [palabra.upper() if len(palabra) > 5 else palabra for palabra in palabras]
diccionario_longitudes = {palabra: len(palabra) for palabra in palabras}

print("Longitudes:", longitudes)
print("Palabras largas:", palabras_largas)
print("Diccionario:", diccionario_longitudes)
