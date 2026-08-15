# Ejemplo de else y finally
try:
    numero = int(input("Escribe un número: "))
except ValueError:
    print("Eso no es un número válido.")
else:
    # Se ejecuta SOLO si no hubo ningún error en el try
    print(f"Perfecto, ingresaste: {numero}")
finally:
    # Se ejecuta SIEMPRE, haya error o no
    print("Intento de lectura terminado.")