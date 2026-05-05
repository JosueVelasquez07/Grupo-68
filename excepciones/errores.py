
import datetime

# -----------------------------------
# REGISTRO DE ERRORES (LOGS)
# -----------------------------------
def registrar_log(error):
    try:
        with open("logs.txt", "a") as archivo:
            archivo.write(f"{datetime.datetime.now()} - {type(error).__name__}: {error}\n")
    except Exception as e:
        print("Error crítico al escribir en log:", e)


# -----------------------------------
# EXCEPCIONES PERSONALIZADAS
# -----------------------------------
class SistemaError(Exception):
    """Excepción base del sistema"""
    pass

class ClienteError(SistemaError):
    pass

class ServicioError(SistemaError):
    pass

class ReservaError(SistemaError):
    pass

class DatoInvalidoError(SistemaError):
    pass


# -----------------------------------
# VALIDACIONES
# -----------------------------------
def validar_texto(valor, campo):
    if not valor or not str(valor).strip():
        raise DatoInvalidoError(f"{campo} no puede estar vacío")


def validar_numero(valor, campo):
    try:
        valor = float(valor)
        if valor <= 0:
            raise DatoInvalidoError(f"{campo} debe ser mayor a 0")
        return valor
    except ValueError as e:
        raise DatoInvalidoError(f"{campo} debe ser numérico") from e


# -----------------------------------
# FUNCIONES CON MANEJO DE EXCEPCIONES
# -----------------------------------

def registrar_cliente(nombre, documento):
    try:
        validar_texto(nombre, "Nombre")
        validar_texto(documento, "Documento")

    except Exception as e:
        registrar_log(e)
        print("Error al registrar cliente:", e)

    else:
        print("Cliente registrado correctamente")

    finally:
        print("Proceso de cliente finalizado")


def registrar_servicio(nombre, precio):
    try:
        validar_texto(nombre, "Nombre del servicio")
        precio = validar_numero(precio, "Precio")

    except Exception as e:
        registrar_log(e)
        print("Error en servicio:", e)

    else:
        print("Servicio registrado correctamente")

    finally:
        print("Proceso de servicio finalizado")


def crear_reserva(cliente, servicio):
    try:
        if not cliente:
            raise ClienteError("Cliente no existe")

        if not servicio:
            raise ServicioError("Servicio no disponible")

    except (ClienteError, ServicioError) as e:
        registrar_log(e)
        print("Error en reserva:", e)

    else:
        print("Reserva creada correctamente")

    finally:
        print("Proceso de reserva finalizado")


# -----------------------------------
# ENCADENAMIENTO DE EXCEPCIONES
# -----------------------------------
def calcular_total(precio, descuento):
    try:
        try:
            precio = validar_numero(precio, "Precio")

            total = precio - descuento
            if total < 0:
                raise ArithmeticError("El total no puede ser negativo")

            return total

        except Exception as e:
            raise SistemaError("Error en cálculo de pago") from e

    except SistemaError as e:
        registrar_log(e)
        print("Error en cálculo:", e)


# -----------------------------------
# PRUEBA
# -----------------------------------
if __name__ == "__main__":

    registrar_cliente("", "123")            # ERROR
    registrar_servicio("Lavado", -10)       # ERROR
    crear_reserva(None, "Lavado")           # ERROR
    calcular_total(100, 200)                # ERROR