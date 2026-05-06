#importaciones 
import datetime
import logging
from .base import Entidad
from excepciones.errores import ReservaError

# Configuracion del logger:
logger = logging.getLogger(__name__)

class Reserva(Entidad):
    # esta clase es el puente entre entre cliente y servicios.

    def __init__(self, id_reserva, cliente, servicio, duracion_horas):
        # encapsulamiento:
        self.__id_reserva = id_reserva
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion_horas = duracion_horas
        self.__estado = "Pendiente"
        self.__fecha_creacion = datetime.datetime.now()

    # --- METODOS HEREDADOS DE ENTIDAD ---

    def mostrar_info(self):
        """Implementación obligatoria para mostrar el resumen de la reserva."""
        try:
            # Verificacion de existencia de objetos antes de llamar a sus metodos
            nombre_cliente = self.__cliente.get_nombre() if self.__cliente else "N/A"
            nombre_servicio = self.__servicio.get_nombre() if self.__servicio else "N/A"

            info = (
                f"RESERVA #{self.__id_reserva} | "
                f"CLIENTE: {nombre_cliente} | "
                f"SERVICIO: {nombre_servicio} | "
                f"ESTADO: {self.__estado} | "
                f"FECHA: {self.__fecha_creacion.strftime('%d/%m/%Y %H:%M')}"
            )

            logger.info(f"Información consultada para Reserva {self.__id_reserva}")
            return info

        except Exception as e:
            logger.error(f"Error mostrando reserva {self.__id_reserva}: {str(e)}")
            return "Error mostrando información"

    def actualizar_info(self, **kwargs):
        """Actualización dinámica de atributos con validación rigurosa."""
        try:
            if "duracion_horas" in kwargs:
                nueva_duracion = kwargs["duracion_horas"]
                if nueva_duracion <= 0:
                    raise ReservaError("La duración debe ser mayor a 0", "ERR_DURACION")
                self.__duracion_horas = nueva_duracion

            if "estado" in kwargs:
                self.set_estado(kwargs["estado"])

            logger.info(f"Reserva {self.__id_reserva} actualizada exitosamente.")

        except ReservaError as e:
            logger.error(f"{str(e)} | Código: {e.codigo_error}")

        except Exception as e:
            logger.critical(f"Fallo inesperado al actualizar ID {self.__id_reserva}: {str(e)}")

    # --- GETTERS Y SETTERS ---

    def set_estado(self, nuevo_estado):
        """Validador de estados permitidos."""
        estados_validos = ["Pendiente", "Confirmada", "Cancelada", "Fallida"]
        if nuevo_estado in estados_validos:
            self.__estado = nuevo_estado
        else:
            raise ReservaError(f"Estado inválido: {nuevo_estado}", "ERR_ESTADO")

    def get_estado(self):
        return self.__estado

    # --- logica principal ---

    def procesar_reserva(self):
        
        #Ejecuta la confirmacion de la reserva y el calculo de costos.
        
        logger.info(f"Iniciando procesamiento de Reserva {self.__id_reserva}")

        try:
            # 1. Validaciones preventivas
            if self.__duracion_horas <= 0:
                raise ReservaError("Duración inválida para el cálculo", "ERR_DURACION")
            if self.__cliente is None:
                raise ReservaError("Cliente no asignado", "ERR_CLIENTE")
            if self.__servicio is None:
                raise ReservaError("Servicio no asignado", "ERR_SERVICIO")

            
            total = self.__servicio.calcular_costo(self.__duracion_horas)

            logger.info(f"Reserva {self.__id_reserva} confirmada. Total: ${total}")
            self.__estado = "Confirmada"

        except ReservaError as e:
            # Errores controlados
            logger.error(f"Reserva {self.__id_reserva} fallida: {str(e)} | Código: {e.codigo_error}")
            self.__estado = "Fallida"

        except Exception as e:
            # Errores inesperados
            logger.critical(f"Error crítico en sistema (ID {self.__id_reserva}): {str(e)}")
            self.__estado = "Fallida"
            raise RuntimeError(f"Fallo crítico en el hilo de reserva {self.__id_reserva}") from e

        finally:
            # Registro de finalizacion independientemente del resultado
            logger.info(f"Operación finalizada para ID {self.__id_reserva}. Estado final: {self.__estado}")

    # --- Otros metodos ---

    def cancelar(self):
        """Permite anular una reserva confirmada."""
        try:
            if self.__estado == "Confirmada":
                self.__estado = "Cancelada"
                logger.info(f"Reserva {self.__id_reserva} cancelada satisfactoriamente.")
            else:
                raise ReservaError(
                    f"No se puede cancelar una reserva en estado: {self.__estado}",
                    "ERR_CANCEL"
                )
        except ReservaError as e:
            logger.warning(f"Intento de cancelación fallido (ID {self.__id_reserva}): {str(e)}")

    def __str__(self):
        #Representacion simplificada del objeto
        return f"Reserva {self.__id_reserva} - Estado: {self.__estado}"
""