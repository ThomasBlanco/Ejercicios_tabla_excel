class Usuario:
    def __init__ (self, nombre, cedula, tipo_usuario):
        self.nombre = nombre
        self.cedula = cedula
        self.tipo_usuario = tipo_usuario

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cedula(self):
        return self.cedula

    def set_cedula(self, cedula):
        self.cedula = cedula

    def get_tipo_usuario(self):
        return self.tipo_usuario

    def set_tipo_usuario(self, tipo_usuario):
        self.tipo_usuario = tipo_usuario

    def mostrar_info(self):
        return f"Cedula Usuario: {self.cedula}, Nombre Usuario: {self.nombre}, Tipo Usuario: {self.tipo_usuario} "
