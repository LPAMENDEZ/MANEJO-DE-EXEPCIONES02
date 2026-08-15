# Ejemplo de validación de datos usando excepciones
def solicitar_edad():
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if edad < 0:
                raise ValueError("La edad no puede ser negativa")
            return edad
        except ValueError as error:
            print(f"Dato inválido: {error}. Intenta de nuevo.")


edad = solicitar_edad()
print(f"Tu edad registrada es: {edad}")