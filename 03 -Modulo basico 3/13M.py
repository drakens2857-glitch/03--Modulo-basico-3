niveles = [1, 5, 10, 15, 20, 25, 30]

experiencia = [nivel * 100 for nivel in niveles]
mensajes = [f"Nivel {nivel} alcanzado" for nivel in niveles]
vida_maxima = [50 + nivel * 10 for nivel in niveles]

print("Experiencia:", experiencia)
print("Mensajes:", mensajes[:3])
print("Vida máxima:", vida_maxima)
