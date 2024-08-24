import socket
import threading
from conversacion import Conversacion
from comandos import procesar_entrada

def cifrar_mensaje(mensaje):
    return mensaje[::-1]

def descifrar_mensaje(mensaje):
    return mensaje[::-1]

def recibir_mensajes(cliente_socket, chat):
    while True:
        try:
            mensaje_cifrado = cliente_socket.recv(1024).decode('utf-8')
            if mensaje_cifrado:
                mensaje = descifrar_mensaje(mensaje_cifrado)
                print("\n" + mensaje)
        except Exception as e:
            print(f"Error al recibir mensaje: {e}")
            break

def iniciar_cliente(usuario_local):
    host = '127.0.0.1'
    puerto = 12345

    try:
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect((host, puerto))
    except Exception as e:
        print(f"Error de conexión: {e}")
        return

    chat = Conversacion(usuario_local)

    # Hilo para recibir mensajes
    hilo_recibir = threading.Thread(target=recibir_mensajes, args=(cliente_socket, chat))
    hilo_recibir.start()

    while True:
        entrada = input("> ")
        try:
            procesar_entrada(entrada, chat)
            if not entrada.startswith("/"):
                mensaje_cifrado = cifrar_mensaje(entrada)
                cliente_socket.send(mensaje_cifrado.encode('utf-8'))
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")
