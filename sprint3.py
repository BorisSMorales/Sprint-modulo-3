import random

#la secuencia es , els istema pedira los numeros de contacto para cada usuario, al ingresarlos todos generara las contrasenas para todos.

# Primero se crea lista de nombres de usuarios
usuarios = ["Usuario1", "Usuario2", "Usuario3", "Usuario4", "Usuario5", "Usuario6", "Usuario7", "Usuario8", "Usuario9", "Usuario10"]

# función para crear una cuenta de usuario
def crear_cuenta(nombre_usuario):
    # generar una contraseña aleatoria
    longitud_contraseña = 8
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" # para el criterio de mayusculas, minusculas y numeros 
    contraseña = "".join(random.choice(caracteres) for i in range(longitud_contraseña))
    # pedir número de teléfono
    while True:
        telefono = input(f"Ingrese el número de teléfono para {nombre_usuario}: ")
        if telefono.isdigit() and len(telefono) == 8:
            break
        else:
            print("El número de teléfono debe tener 8 dígitos numéricos.")
    # guardar cuenta de usuario y contraseña en un diccionario
    cuenta_usuario = {"usuario": nombre_usuario, "contraseña": contraseña, "teléfono": telefono}
    return cuenta_usuario

# crear cuentas de usuario para todos los usuarios en la lista
cuentas = []
for usuario in usuarios:
    cuenta = crear_cuenta(usuario)
    cuentas.append(cuenta)

# imprimir cuentas de usuario y contraseñas
print("Cuentas de usuario creadas:")
for cuenta in cuentas:
    print(f"Usuario: {cuenta['usuario']}, Contraseña: {cuenta['contraseña']}, Teléfono: {cuenta['teléfono']}")

#José Ramos
#Boris Morales