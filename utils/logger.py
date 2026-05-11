import logging

def configurar_logger():
    logger = logging.getLogger()

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("sistema_errores.log", encoding="utf-8")

    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
