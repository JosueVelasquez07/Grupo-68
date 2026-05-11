from abc import ABC, abstractmethod

class Entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass
    
    @abstractmethod
    def actualizar_info(self, **kwargs):
        pass