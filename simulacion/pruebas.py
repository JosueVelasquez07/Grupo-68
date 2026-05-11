from modelos.cliente import Cliente
from modelos.reserva import Reserva
from modelos.servicios.sala import Sala
from modelos.servicios.equipo import Equipo
from modelos.servicios.asesoria import Asesoria
from excepciones.errores import SistemaError


def simular():

    try:
        # Cliente
        c1 = Cliente(
            1,
            "Juan",
            "juan@mail.com",
            "3001234567"
        )

        # Servicios
        s1 = Sala(1, "Sala VIP", 50000)
        s2 = Equipo(2, "Proyector", 30000)
        s3 = Asesoria(3, "Consultoría", 80000, "avanzado")

        # Reservas
        reservas = [
            Reserva(1, c1, s1, 2),
            Reserva(2, c1, s2, -1),  # Error intencional
            Reserva(3, c1, s3, 3)
        ]

        # Procesamiento
        for r in reservas:

            r.procesar_reserva()

            print(r.mostrar_info())

    except SistemaError as e:

        print(
            f"Error del sistema: {e} "
            f"| Código: {e.codigo_error}"
        )

    except Exception as e:

        print(f"Error inesperado: {e}")