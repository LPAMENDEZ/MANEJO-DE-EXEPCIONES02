def dividir_numeros():
    """
    Solicita dos números al usuario, realiza la división y maneja
    los errores más comunes: valores no numéricos y división entre cero.
    """
    try:
        numero1 = int(input("Ingresa el primer número: "))
        numero2 = int(input("Ingresa el segundo número: "))
        resultado = numero1 / numero2

    except ValueError:
        print("Error: debes ingresar solo números enteros.")

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")

    else:
        # Se ejecuta solo si no hubo ningún error
        print(f"El resultado de la división es: {resultado}")

    finally:
        # Se ejecuta siempre, haya error o no
        print("Operación finalizada")


if __name__ == "__main__":
    dividir_numeros()
