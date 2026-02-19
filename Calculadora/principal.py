from modelo_usuario import Usuario
from modelo_calculadora import Calculadora
from modelo_numero import Numero

calc = Calculadora("2026-02-17")

datos = [
    ("1020345678", "Juan Garcia Lopez", 10, 23, "suma"),
    ("1020345678", "Juan Garcia Lopez", 69, 45, "resta"),
    ("1020345678", "Juan Garcia Lopez", 70, 3, "multiplicacion"),
    ("1020345678", "Juan Garcia Lopez", 17, 2, "division"),

    ("1020345679", "Maria Lopez Perez", 10, 5, "suma"),
    ("1020345679", "Maria Lopez Perez", 10, 5, "resta"),
    ("1020345679", "Maria Lopez Perez", 10, 5, "multiplicacion"),
    ("1020345679", "Maria Lopez Perez", 10, 5, "division"),

    ("1020345680", "Carlos Rodriguez Sanchez", 500, 8, "suma"),
    ("1020345680", "Carlos Rodriguez Sanchez", 203, 8, "resta"),
    ("1020345680", "Carlos Rodriguez Sanchez", 422, 32, "division")
]

for cedula, nombre, n1, n2, oper in datos:
    usuario = Usuario(nombre, cedula)
    num1 = Numero(n1)
    num2 = Numero(n2)

    resultado = calc.hacer_operacion(num1, num2, oper)
    calc.guardar_info(usuario, n1, n2)

# mostramos la tabla
calc.mostrar_tabla()

