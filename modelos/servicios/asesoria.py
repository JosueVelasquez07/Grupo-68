from .base import entidad
from excepciones.errores import ReservaError

class Asesoria(entidad):
  def _init_(self, nombre, precio_base, nivel):
    super()._init_(nombre)

# Validacion del precio 
if precio_base <= 0:
  raise ReservaError("El precio base debe ser mayor a 0")

# Validacion del nivel
if nivel not in ["basico", "intermedio", "avanzado"]:
  raise ReservaError("Nivel invalido")

self.precio_base = precio_base
self.nivel = nivel 

def calcular_costo(self):
  if self.nivel == "avanzado":
    return self.precio_base * 1.5
  elif self.nivel == "intermedio":
    return self.precio_base * 1.2
  return self.precio_base





  
