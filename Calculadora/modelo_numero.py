class Numero:
    def __init__(self, numero):
        self.valor = numero

    def get_numero(self):
        return self.valor
    
    def set_numero(self, nuevo_numero):
        self.valor = nuevo_numero

    def mostrar_info(self):
        return f"El numero es: {self.valor}"
