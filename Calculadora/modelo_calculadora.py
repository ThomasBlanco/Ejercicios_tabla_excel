class Calculadora:
    def __init__(self, fecha):
        self.fecha = fecha
        self.tipo_operacion = ""
        self.resultado = ""
        self.texto_tabla = ""  

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha
        return self.fecha

    def hacer_operacion(self, numero1, numero2, tipo_operacion):
        self.tipo_operacion = tipo_operacion.capitalize()

        n1 = numero1.get_numero()
        n2 = numero2.get_numero()

        if self.tipo_operacion == "Suma":
            self.resultado = n1 + n2
        elif self.tipo_operacion == "Resta":
            self.resultado = n1 - n2
        elif self.tipo_operacion == "Multiplicacion":
            self.resultado = n1 * n2
        elif self.tipo_operacion == "Division":
            self.resultado = n1 / n2 if n2 != 0 else "Error: División por cero"
        else:
            self.resultado = "Operación no válida"

        return self.resultado

    def guardar_info(self, obj_usuario):
        self.texto_tabla += (
            f"{obj_usuario.get_cedula():<12} "
            f"{obj_usuario.get_nombre():<25} "
            f"{self.tipo_operacion:<18} "
            f"{self.resultado:<10} "
            f"{self.fecha}\n"
        )

    def mostrar_tabla(self):
        print("----- TABLA DE OPERACIONES -----")
        print(f"{'Cedula':<12} {'Nombre Usuario':<25} {'Numero1':<8} {'Numero2':<8} {'Tipo de Operacion':<18} {'Resultado':<10} {'Fecha'}")
        print("-" * 100)
        print(self.texto_tabla)

    def guardar_info(self, obj_usuario, n1, n2):
        self.texto_tabla += (
            f"{obj_usuario.get_cedula():<12} "
            f"{obj_usuario.get_nombre():<25} "
            f"{n1:<8} "
            f"{n2:<8} "
            f"{self.tipo_operacion:<18} "
            f"{self.resultado:<10} "
            f"{self.fecha}\n"
        )

    def mostrar_info(self):
        return f"Fecha: {self.fecha}, Tipo de operación: {self.tipo_operacion}, Resultado: {self.resultado}"

