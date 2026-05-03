from .base import entidad
from excepciones.errores import ReservaError

class AlquilerEquipo(entidad):
  def _init_(self, nombre, precio_base, dias):
    super(). _init_(nombre)

    # Validacion del Precio
     if precio_base <=0:
       raise ReservaError("El precio base debe ser mayor a 0")

    # Validacion de dias 
    if dias <=0:
      raise ReservaError("Los dias deben ser mayores a 0")

    self.precio_base = precio_base
    self.dias = dias

def calcular_costo(self):
  return self.precio_base * self.dias
