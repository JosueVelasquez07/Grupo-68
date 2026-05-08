from servicio import Servicio
from excepciones.errores import ServicioError

class Sala(Servicio):

    def calcular_costo(self, duracion):
        if duracion <= 0:
            raise ServicioError("Duración inválida", "ERR_DURACION")

        return duracion * self._precio
