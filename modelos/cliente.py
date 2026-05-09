class SistemaError(Exception):
    def __init__(self, mensaje, codigo_Error):
        super().__init__(mensaje)
        self.codigo = codigo_Error


class ClienteError(SistemaError):
    pass
    def __init__(self, id_cliente, nombre, correo, telefono):
 
        # Validaciones
        if not nombre:
            raise ClienteError("El nombre no puede estar vacío", "ERR_NOMBRE")
 
        if "@" not in correo:
            raise ClienteError("Correo inválido", "ERR_CORREO")
 
        if not telefono.isdigit():
            raise ClienteError("Teléfono inválido", "ERR_TELEFONO")
 
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
 
        # MÉTODOS DE ENTIDAD
    
 
    def mostrar_info(self):
        return (
            f"CLIENTE #{self.__id_cliente} | "
            f"NOMBRE: {self.__nombre} | "
            f"CORREO: {self.__correo} | "
            f"TELÉFONO: {self.__telefono}"
        )
 
    def actualizar_info(self, **kwargs):
        for key, value in kwargs.items():
 
            if key == "nombre":
                if not value:
                    raise ClienteError("Nombre inválido", "ERR_NOMBRE")
                self.__nombre = value
 
            elif key == "correo":
                if "@" not in value:
                    raise ClienteError("Correo inválido", "ERR_CORREO")
                self.__correo = value
 
            elif key == "telefono":
                if not value.isdigit():
                    raise ClienteError("Teléfono inválido", "ERR_TELEFONO")
                self.__telefono = value
 
    
    # GETTERS
    
 
    def get_nombre(self):
        return self.__nombre
 
    def get_id(self):
        return self.__id_cliente
