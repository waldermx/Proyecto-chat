from conexiones import ConexionCliente
from conversacion import Conversacion
from comandos import procesar_comando
from usuario import Usuario

def iniciar_cliente(usuario_local):
    host = '127.0.0.1'
    puerto = 12345

    conexion = ConexionCliente(host, puerto)
    if not conexion.conectar():
        return

    chat = Conversacion(usuario_local)
    conexion.iniciar_hilo_recepcion(chat)

    while True:
        entrada = input("> ")
        if entrada.startswith("/"):
            comando = procesar_comando(entrada, chat)
            comando.ejecutar()
        else:
            conexion.enviar_mensaje(entrada)
