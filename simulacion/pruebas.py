from modelos.cliente import Cliente
from modelos.reserva import Reserva
from modelos.sala import Sala
from modelos.equipo import Equipo
from modelos.asesoria import Asesoria

def simular():

    try:
        c1 = Cliente(1, "Juan", "juan@mail.com", "300123")
        s1 = Sala(1, "Sala", 50000)
        s2 = Equipo(2, "Proyector", 30000)
        s3 = Asesoria(3, "Consultoría", 80000, "avanzado")

        reservas = [
            Reserva(1, c1, s1, 2),
            Reserva(2, c1, s2, -1),  # error
            Reserva(3, c1, s3, 3)
        ]

        for r in reservas:
            r.procesar_reserva()
            print(r.mostrar_info())

    except Exception as e:
        print("Error en simulación:", e)