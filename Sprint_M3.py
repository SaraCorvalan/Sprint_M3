#Sprint modulo 3 / Sara Corvalán
import random

# Lista de nombres de usuarios
nombres_usuarios = ["Daniel", "Romina", "José", "Demian", "Sara", "María", "Carlos", "Kristel", "Tomas", "Rebeca"]

# Función para crear las cuentas
def crear_cuenta(nombre):
    # Genera una contraseña aleatoria con mayúsculas, minúsculas y números
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    longitud = 8
    password = "".join(random.choice(caracteres) for _ in range(longitud))
    
    # Pide número telefónico para cada usuario de 8 dígitos
    while True:
        telefono = input(f"Ingrese el número telefónico para {nombre}: ")
        if len(telefono) == 8 and telefono.isdigit():
            break
        else:
            print("El número telefónico debe tener 8 dígitos numéricos.")
    
    # Variable para guardar las cuentas
    cuenta = {
        "nombre": nombre,
        "contraseña": password,
        "telefóno": telefono
    }
    
    return cuenta

# Crea cuentas para cada usuario
cuentas = []
for nombre in nombres_usuarios:
    cuenta = crear_cuenta(nombre)
    cuentas.append(cuenta)

# Imprimir las cuentas creadas
print("----------------------------------")
print("        Cuentas de Usuarios       ")
print("----------------------------------")

for cuenta in cuentas:
    print("----------------------------------")
    print("Nombre: ", cuenta["nombre"])
    print("Contraseña: ", cuenta["contraseña"])
    print("Teléfono: ", cuenta["telefóno"])
print("----------------------------------")
