# Ejemplo básico de try/except
try:
    numero = int(input("Escribe un número: "))
    print(f"El doble es: {numero * 2}")
except ValueError:
    print("Eso no es un número válido.")