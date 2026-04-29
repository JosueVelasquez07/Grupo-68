from modelos.cliente import Cliente
from modelos.reserva import Reserva

def simular():
    print("\n--- SIMULACIÓN DEL SISTEMA ---")

    cliente = Cliente(1, "Juan", "juan@ejemplo.com", "3001234567")


    reserva = Reserva(1, cliente, servicio, 2)

    print(reserva.mostrar_info())

    reserva.procesar_reserva()
    reserva.cancelar()