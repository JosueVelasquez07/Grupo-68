class SistemaError(Exception):
    def __init__(self, mensaje, codigo_error):
        super().__init__(mensaje)
        self.codigo_error = codigo_error


class ClienteError(SistemaError):
    pass


class ServicioError(SistemaError):
    pass


class ReservaError(SistemaError):
    pass