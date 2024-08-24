import socket
import threading
from cifrado import cifrar_mensaje, descifrar_mensaje

class ConexionCliente:
    def __init__(self, host, puerto):
        self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.puerto = puerto

    def conectar(self):
        try:
            self.cliente_socket.connect((self.host, self.puerto))
            print("Conexión establecida con el servidor.")
        except Exception as e:
            print(f"Error de conexión: {e}")
            return False
        return True

    def enviar_mensaje(self, mensaje):
        mensaje_cifrado = cifrar_mensaje(mensaje)
        try:
            self.cliente_socket.send(mensaje_cifrado.encode('utf-8'))
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")

    def recibir_mensajes(self, chat):
        while True:
            try:
                mensaje_cifrado = self.cliente_socket.recv(1024).decode('utf-8')
                if mensaje_cifrado:
                    mensaje = descifrar_mensaje(mensaje_cifrado)
                    chat.agregar_mensaje(chat.usuario_local, mensaje)
            except Exception as e:
                print(f"Error al recibir mensaje: {e}")
                break

    def iniciar_hilo_recepcion(self, chat):
        hilo_recibir = threading.Thread(target=self.recibir_mensajes, args=(chat,))
        hilo_recibir.start()
