operaciones = {
    "sumar": lambda x, y: x + y,
    "restar": lambda x, y: x - y,
    "multiplicar": lambda x, y: x * y,
    "dividir": lambda x, y: x / y if y != 0 else "Error: División por cero"
}

print("5 + 3 =", operaciones["sumar"](5, 3))
print("10 - 4 =", operaciones["restar"](10, 4))
print("6 * 7 =", operaciones["multiplicar"](6, 7))
print("15 / 3 =", operaciones["dividir"](15, 3))
