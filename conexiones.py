import socket
import asyncio
from cifrado import cifrar_mensaje, descifrar_mensaje

class ConexionCliente:
    def __init__(self, host, puerto):
        self.host = host
        self.puerto = puerto
        self.cliente_socket = None

    async def conectar(self):
        loop = asyncio.get_event_loop()
        self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente_socket.setblocking(False)
        try:
            await loop.sock_connect(self.cliente_socket, (self.host, self.puerto))
            print("Conexión establecida con el servidor.")
            return True
        except Exception as e:
            print(f"Error de conexión: {e}")
            return False

    async def enviar_mensaje(self, mensaje):
        mensaje_cifrado = cifrar_mensaje(mensaje)
        await asyncio.get_event_loop().sock_sendall(self.cliente_socket, mensaje_cifrado.encode('utf-8'))

    async def recibir_mensajes(self, chat):
        while True:
            try:
                mensaje_cifrado = await asyncio.get_event_loop().sock_recv(self.cliente_socket, 1024)
                if mensaje_cifrado:
                    mensaje = descifrar_mensaje(mensaje_cifrado.decode('utf-8'))
                    chat.agregar_mensaje(chat.usuario_local, mensaje)
            except Exception as e:
                print(f"Error al recibir mensaje: {e}")
                break
