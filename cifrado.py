# cifrado.py
from cryptography.fernet import Fernet

# Genera una clave y guárdala en un lugar seguro
# Solo debe hacerse una vez y la clave debe ser compartida entre el cliente y el servidor
# Para este ejemplo, vamos a generar una clave fija
clave = Fernet.generate_key()
cifrador = Fernet(clave)

def cifrar_mensaje(mensaje):
    mensaje_bytes = mensaje.encode('utf-8')
    mensaje_cifrado = cifrador.encrypt(mensaje_bytes)
    return mensaje_cifrado.decode('utf-8')

def descifrar_mensaje(mensaje_cifrado):
    mensaje_cifrado_bytes = mensaje_cifrado.encode('utf-8')
    mensaje_bytes = cifrador.decrypt(mensaje_cifrado_bytes)
    return mensaje_bytes.decode('utf-8')
