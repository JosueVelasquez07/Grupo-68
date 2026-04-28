import logging

def configurar_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("sistema_errores.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger
