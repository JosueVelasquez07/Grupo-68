from abc import abstractmethod    
from .base import Entidad

# Clase que representa un servicio
class Servicio(Entidad):
# Clase que representa un servicio ofrecido 
    def __init__(self, id_servicio, nombre, precio):
        self._id_servicio = id_servicio
        self._nombre = nombre
        self._precio = precio

# Método para mostrar la información del servicio
    def mostrar_info(self):
        return f"Servicio: {self._nombre}, Precio base: {self._precio}"

# Método para actualizar la información del servicio
    def actualizar_info(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, f"_{key}"):
                setattr(self, f"_{key}", value)

# Este método es abstracto y debe ser implementado por las subclases
    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    # Getter
    @property
    def id_servicio(self):
        return self._id_servicio
    
    @property
    def nombre(self):
        return self._nombre 
    
    @property
    def precio(self):
        return self._precio