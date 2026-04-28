
import datetime
import logging

# Configuración del log (Registro de eventos y errores)
logging.basicConfig(
    filename='sistema_errores.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ReservaError(Exception):
    """Excepción personalizada para errores específicos de la reserva."""
    def __init__(self, mensaje, codigo_error):
        super().__init__(mensaje)
        self.codigo_error = codigo_error

class Reserva:
    def __init__(self, id_reserva, cliente, servicio, duracion_horas):
        # Atributos privados siguiendo el principio de encapsulación
        self.__id_reserva = id_reserva
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion_horas = duracion_horas
        self.__estado = "Pendiente"
        self.__fecha_creacion = datetime.datetime.now()

    # --- MÉTODOS GETTER Y SETTER TRADICIONALES ---

    def get_estado(self):
        return self.__estado

    def set_estado(self, nuevo_estado):
         estados_validos = ["Pendiente", "Confirmada", "Cancelada", "Fallida", "Error"]
         if nuevo_estado in estados_validos:
             self.__estado = nuevo_estado
         else:
             raise ReservaError(f"Estado '{nuevo_estado}' no es válido.", "ERR_ESTADO_INVALIDO")

    def get_id_reserva(self):
        return self.__id_reserva

    # --- LÓGICA DE NEGOCIO ---

    def procesar_reserva(self):
        """
        Gestiona la lógica de confirmación con manejo robusto de excepciones.
        """
        print(f"\n[SISTEMA] Iniciando procesamiento de Reserva ID: {self.__id_reserva}")
        
        try:
            # 1. Validaciones de parámetros
            if self.__duracion_horas <= 0:
                raise ReservaError("La duración del servicio debe ser mayor a 0 horas.", "ERR_PARAMETROS")
            
            if self.__cliente is None or self.__servicio is None:
                raise ValueError("Cliente o Servicio no pueden ser nulos (Parámetros faltantes).")

            # 2. Cálculo de costos (Polimorfismo: llama al método del servicio especializado)
            # Nota: Se asume que tus compañeros implementarán 'calcular_costo' en sus clases.
            costo_total = self.__servicio.calcular_costo(self.__duracion_horas)
            print(f"-> Costo total calculado: ${costo_total}")

        except ReservaError as e:
            # Manejo de error de lógica de negocio
            logging.error(f"Reserva {self.__id_reserva} fallida: {e} | Código: {e.codigo_error}")
            self.set_estado("Fallida")
            print(f"Error controlado: {e}")

        except Exception as e:
            # Manejo de errores inesperados (Encadenamiento de excepciones)
            logging.critical(f"Fallo crítico en Reserva {self.__id_reserva}: {str(e)}")
            self.set_estado("Error")
            # Encadenamos para no perder el rastro del error original
            raise RuntimeError(f"El sistema no pudo procesar la reserva {self.__id_reserva}") from e

        else:
            # Se ejecuta si el bloque try fue exitoso
            self.set_estado("Confirmada")
            logging.info(f"Reserva {self.__id_reserva} confirmada exitosamente.")
            print(f"¡Éxito! Reserva confirmada para {self.__cliente.get_nombre()}.")

        finally:
            # Bloque que siempre se ejecuta para limpieza o logs de cierre
            print(f"[LOG] Finalizó el intento de procesamiento. Estado actual: {self.__estado}")

    def cancelar(self):
        """Método para cancelar la reserva con validación."""
        if self.__estado == "Confirmada":
            self.set_estado("Cancelada")
            print("La reserva ha sido cancelada satisfactoriamente.")
        else:
            logging.warning(f"Intento de cancelación fallido en ID {self.__id_reserva}. Estado: {self.__estado}")
            print("No se puede cancelar una reserva que no esté en estado 'Confirmada'.")

    def __str__(self):
        """Representación en texto del objeto."""
        return f"RESERVA: {self.__id_reserva} | CLIENTE: {self.__cliente.get_nombre()} | ESTADO: {self.__estado}"