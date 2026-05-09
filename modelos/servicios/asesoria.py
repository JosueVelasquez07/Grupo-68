from ..servicio import Servicio
from excepciones.errores import ServicioError

class Asesoria(Servicio):

    def __init__(self, id_servicio, nombre, precio, nivel):
        super().__init__(id_servicio, nombre, precio)

        if nivel not in ["basico", "intermedio", "avanzado"]:
            raise ServicioError("Nivel inválido", "ERR_NIVEL")

        self._nivel = nivel

    def calcular_costo(self, duracion):
        if duracion <= 0:
            raise ServicioError("Duración inválida", "ERR_DURACION")

        if self._nivel == "avanzado":
            return duracion * self._precio * 1.5
        elif self._nivel == "intermedio":
            return duracion * self._precio * 1.2
        return duracion * self._precio
