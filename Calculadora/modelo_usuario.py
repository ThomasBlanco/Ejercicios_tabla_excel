class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cedula(self):
        return self.cedula

    def set_cedula(self, cedula):
        self.cedula = cedula
    
    def mostrar_info(self):
        return f"Usuario: {self.nombre}, Cedula: {self.cedula}"
