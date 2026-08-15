# Ejemplo de lanzamiento manual de excepciones con raise
def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    print(f"Edad válida: {edad}")


try:
    verificar_edad(-5)
except ValueError as error:
    print(f"Error: {error}")