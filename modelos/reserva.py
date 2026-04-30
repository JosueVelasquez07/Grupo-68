
import datetime
import logging

#Importaciones segun la estructura del equipo
from .base import entidad 
from excepciones.errores import ReservaError

# Configuracion de logs para el archivo solicitado
logging.basicConfig(
    filename='sistema_errores.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Reserva(entidad):
    def __init__(self, id_reserva, cliente, servicio, duracion_horas):
        # Encapsulacion con atributos privados
        self.__id_reserva = id_reserva
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion_horas = duracion_horas
        self.__estado = "Pendiente"
        self.__fecha_creacion = datetime.datetime.now()

    # --- IMPLEMENTACION DE METODOS DE LA CLASE ENTIDAD ---

    def mostrar_info(self):

        #Muestra la información integrada de la reserva

        resumen = (f"RESERVA #{self.__id_reserva} | "
                   f"CLIENTE: {self.__cliente.nombre} | "
                   f"SERVICIO: {self.__servicio.nombre} | "
                   f"ESTADO: {self.__estado}")
        print(resumen)
        return resumen

    def actualizar_info(self, **kwargs):
        #Actualiza los  atributos dinamicamente
        try:
            for key, value in kwargs.items():
                if key == "duracion":
                    if value <= 0: raise ReservaError("Duración inválida", "ERR_VAL")
                    self.__duracion_horas = value
                elif key == "estado":
                    self.set_estado(value)
            print(f"Reserva {self.__id_reserva} actualizada correctamente.")
        except Exception as e:
            logging.error(f"Error actualizando Reserva {self.__id_reserva}: {e}")

    # --- METODOS GETTER Y SETTER ---

    def set_estado(self, nuevo_estado):
        estados_validos = ["Pendiente", "Confirmada", "Cancelada", "Fallida"]
        if nuevo_estado in estados_validos:
            self.__estado = nuevo_estado
        else:
            raise ReservaError(f"Estado '{nuevo_estado}' no válido.", "ERR_ESTADO_INV")

    def get_estado(self):
        return self.__estado

    # --- LÓGICA DE PROCESAMIENTO CON EXCEPCIONES ---

    def procesar_reserva(self):
        """
        Calcula costos y procesa la reserva. 
        Implementa polimorfismo y manejo robusto de errores.
        """
        print(f"\n[SISTEMA FJ] Iniciando procesamiento: {self.__id_reserva}")
        
        try:
            # Validaciones de entrada
            if self.__duracion_horas <= 0:
                raise ReservaError("La duracion debe ser mayor a cero.", "ERR_DURACION")

            
            # Si el servicio no tiene el metodo, se captura el error para no detener el sistema
            if hasattr(self.__servicio, 'calcular_costo'):
                total = self.__servicio.calcular_costo(self.__duracion_horas)
            else:
                # Calculo de respaldo basado en el precio base de la clase Servicio
                total = self.__servicio.precio * self.__duracion_horas
                logging.warning(f"Servicio {self.__servicio.nombre} no implementó calcular_costo.")

            print(f"Validación exitosa para {self.__cliente.nombre}.")
            print(f"Monto total: ${total}")

        except ReservaError as e:
            # Error de logica de negocio
            logging.error(f"ID {self.__id_reserva} - Fallo de negocio: {e.mensaje} | Código: {e.codigo_error}")
            self.__estado = "Fallida"
            
        except Exception as e:
            # Error crítico o inesperado
            logging.critical(f"ID {self.__id_reserva} - Error Inesperado: {str(e)}")
            self.__estado = "Fallida"
            # Encadenamiento de excepciones
            raise RuntimeError(f"Error sistemico en reserva {self.__id_reserva}") from e

        else:
            # Se ejecuta si no hubo excepciones
            self.__estado = "Confirmada"
            logging.info(f"Reserva {self.__id_reserva} procesada con exito.")
            print(">>> OPERACIÓN COMPLETADA CON ÉXITO <<<")

        finally:
            # Se ejecuta siempre
            print(f"[LOG] Transacción cerrada. Estado: {self.__estado}")

    def __str__(self):
        return f"Reserva {self.__id_reserva} - {self.__estado}"