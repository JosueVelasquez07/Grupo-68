class Cliente:
    def __init__(self, id_cliente, nombre, correo, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def mostrar_perfil(self):
        """Muestra la información básica del cliente."""
        print("-" * 30)
        print(f"PERFIL DEL CLIENTE #{self.id_cliente}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Teléfono: {self.telefono}")
        print("-" * 30)

# Simulación de ejecución
if __name__ == "__main__":
    print("SISTEMA DE GESTIÓN DE CLIENTES")
    
    # Creando una instancia de ejemplo
    nuevo_cliente = Cliente(1, "Dairo Marrugo", "dairo@ejemplo.com", "3001234567")
    
    # Ejecutando un método
    nuevo_cliente.mostrar_perfil()
