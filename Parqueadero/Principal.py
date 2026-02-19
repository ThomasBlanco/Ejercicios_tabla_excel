from Usuario import Usuario
from Carro import Carro
from Parqueadero import RegistroParqueadero

def main():

    registros = []  # Lista  

    #creamos los obj

    obj_usuario1 = Usuario("1020345678", "Juan García", "Administrador")
    obj_carro1 = Carro("ABC123", "Sedan", "Negro")
    obj_registro1 = RegistroParqueadero(obj_usuario1, obj_carro1, "A-01")

    obj_usuario2 = Usuario("1020345679", "María López", "Cliente")
    obj_carro2 = Carro("XYZ789", "SUV", "Blanco")
    obj_registro2 = RegistroParqueadero(obj_usuario2, obj_carro2, "B-05")

    obj_usuario3 = Usuario("1020345680", "Carlos Rodríguez", "Cliente")
    obj_carro3 = Carro("KLM456", "Pickup", "Azul")
    obj_registro3 = RegistroParqueadero(obj_usuario3, obj_carro3, "C-12")
    obj_registro3.registrar_salida()

    obj_usuario4 = Usuario("1020345681", "Ana Martínez", "Administradora")
    obj_carro4 = Carro("DEF321", "Hatchback", "Rojo")
    obj_registro4 = RegistroParqueadero(obj_usuario4, obj_carro4, "A-03")

    registros.extend([obj_registro1, obj_registro2, obj_registro3, obj_registro4])

    #imprimimos la tablita

    print("\n" + "-" * 140)
    print(f"{'Cédula':<12} {'Nombre':<20} {'Tipo Usuario':<15} {'Placa':<10} "
        f"{'Tipo Carro':<12} {'Color':<10} {'Puesto':<8} "
        f"{'Fecha Entrada':<15} {'Hora Entrada':<12} "
        f"{'Hora Salida':<12} {'Estado':<10}")
    print("-" * 140)

    for r in registros:
        print(f"{r.get_usuario().get_cedula():<12} "
            f"{r.get_usuario().get_nombre():<20} "
            f"{r.get_usuario().get_tipo_usuario():<15} "
            f"{r.get_carro().get_placa():<10} "
            f"{r.get_carro().get_tipo_carro():<12} "
            f"{r.get_carro().get_color():<10} "
            f"{r.get_puesto():<8} "
            f"{str(r.get_fecha_entrada()):<15} "
            f"{r.get_hora_entrada():<12} "
            f"{str(r.get_hora_salida() if r.get_hora_salida() else ''):<12} "
            f"{r.get_estado():<10}")

    print("-" * 140)

if __name__ == "__main__":
    main()