
# Manejo de Excepciones en Python

Proyecto de la actividad GA1-220501096-01-AA1-EV05, donde se estudia y
aplica el manejo de excepciones en Python: captura de errores, control
de flujo con `try`/`except`/`else`/`finally`, lanzamiento manual con
`raise` y creación de excepciones personalizadas.

## ¿Qué son las excepciones?

Una excepción es un error que ocurre **durante la ejecución** del
programa (a diferencia de un error de sintaxis, que Python detecta
antes de correr nada). Cuando algo falla —dividir entre cero, convertir
texto a número, acceder a una clave inexistente—, Python "lanza" una
excepción. Si no hay nada preparado para manejarla, el programa se
detiene y muestra el error. Usar `try`/`except` permite capturar esos
errores y decidir qué hacer en vez de que el programa se rompa.

## Diferencia entre `except`, `else` y `finally`

- **`except`**: se ejecuta **solo si ocurrió un error** dentro del
  bloque `try`. Aquí se maneja el problema (mostrar un mensaje, pedir
  el dato de nuevo, etc.).
- **`else`**: se ejecuta **solo si NO ocurrió ningún error** en el
  `try`. Sirve para separar el código que puede fallar del código que
  depende de que todo haya salido bien.
- **`finally`**: se ejecuta **siempre**, haya habido error o no. Se usa
  para acciones que deben pasar sin importar el resultado (por ejemplo,
  un mensaje de cierre o liberar recursos).

## Estructura del proyecto

excepciones/
├── ejemplos/
│ ├── ejemplo01.py
│ ├── ejemplo02.py
│ ├── ejemplo03.py
│ ├── ejemplo04.py
│ ├── ejemplo05.py
│ └── ejemplo06.py
├── reto/
│ └── dividir_numeros.py
└── README.md

## El reto: `dividir_numeros()`

Función que solicita dos números al usuario, los convierte a enteros y
realiza la división, manejando dos posibles errores:

- **`ValueError`**: si el usuario ingresa algo que no es un número.
- **`ZeroDivisionError`**: si el segundo número es 0.

Al final, un bloque `finally` imprime siempre `"Operación finalizada"`,
sin importar si hubo error o no.

## Ejemplos de ejecución
<img width="1917" height="1017" alt="CAPTURA_EJECUCION" src="https://github.com/user-attachments/assets/e49b88bc-4ad8-4351-bc65-e426990d22cc" />




 
