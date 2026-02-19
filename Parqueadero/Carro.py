class Carro:
    def __init__(self, placa, tipo, color):
        self.placa = placa
        self.tipo = tipo
        self.color= color

    def get_placa(self):
        return self.placa
    
    def set_placa(self, placa):
        self.placa = placa

    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_tipo_carro(self):
        return self.get_tipo()

    def set_tipo_carro(self, tipo):
        return self.set_tipo(tipo)

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def mostrar_info(self):
        return f"{self.placa} - {self.tipo} - {self.color}" 