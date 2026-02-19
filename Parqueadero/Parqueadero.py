from datetime import datetime

class RegistroParqueadero:
    def __init__(self, usuario, carro, puesto):
        self.usuario = usuario
        self.carro = carro
        self.puesto = puesto
        self.fecha_entrada = datetime.now().date()
        self.hora_entrada = datetime.now().strftime("%H:%M")
        self.hora_salida = None
        self.estado = "Entrada"
    
    def get_usuario(self):
        return self.usuario

    def get_carro(self):
        return self.carro

    def get_puesto(self):
        return self.puesto

    def get_fecha_entrada(self):
        return self.fecha_entrada

    def get_hora_entrada(self):
        return self.hora_entrada

    def get_hora_salida(self):
        return self.hora_salida

    def get_estado(self):
        return self.estado

    # SETTERS
    
    def set_puesto(self, puesto):
        self.puesto = puesto

    def registrar_salida(self):
        self.hora_salida = datetime.now().strftime("%H:%M")
        self.estado = "Salida"

    def mostrar_registro(self):
        return [
            self.usuario.cedula,
            self.usuario.nombre,
            self.usuario.tipo_usuario,
            self.carro.placa,
            self.carro.tipo,
            self.carro.color,
            self.puesto,
            self.fecha_entrada,
            self.hora_entrada,
            self.hora_salida if self.hora_salida else "",
            self.estado
        ]