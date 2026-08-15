try:
# Ejemplo de manejo de varias excepciones específicas
try:
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    resultado = a / b
    print(f"Resultado: {resultado}")
except ValueError:
    print("Debes ingresar solo números enteros.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
