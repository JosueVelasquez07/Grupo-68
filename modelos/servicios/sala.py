from .base import entidad
from excepciones.errores import ReservaError

class ReservaSala(entidad):
  def _init_(self, nombre, precio_base, horas):
    super()._init_(nombre)

# Validacion del precio
if precio_base <= 0:
  raise ReservaError("El precio base debe ser mayor  0")

# Validacion de horas
if horas <=0:
  raise ReservaError("Las horas deben ser mayores a 0")

self.precio_base = precio_base
self.horas = horas 

def calcular_costo(self):
  return sefl.precio_base * self.horas
