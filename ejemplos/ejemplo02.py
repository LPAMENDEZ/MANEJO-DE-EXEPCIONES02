# Ejemplo de excepción personalizada
class SaldoInsuficienteError(Exception):
    """Se lanza cuando se intenta retirar más dinero del disponible."""
    pass


def retirar(saldo, cantidad):
    if cantidad > saldo:
        raise SaldoInsuficienteError("No hay fondos suficientes para este retiro")
    return saldo - cantidad


try:
    retirar(100, 500)
except SaldoInsuficienteError as error:
    print(f"Error: {error}")
    