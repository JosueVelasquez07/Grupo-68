from simulacion.pruebas import simular
from utils.logger import configurar_logger

def main():
    configurar_logger()
    
    print("=== SISTEMA SOFTWARE FJ ===")
    simular()

if __name__ == "__main__":
    main()
