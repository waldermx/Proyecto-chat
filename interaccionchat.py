from conexiones import ConexionCliente
from conversacion import Conversacion
from comandos import procesar_comando

class InteraccionChat:
    def __init__(self, usuario_local, host, puerto):
        self.conexion = ConexionCliente(host, puerto)
        self.chat = Conversacion(usuario_local)

    def iniciar(self):
        if not self.conexion.conectar():
            return

        self.conexion.iniciar_hilo_recepcion(self.chat)
        self.ciclo_principal()

    def ciclo_principal(self):
        while True:
            entrada = input("> ")
            if entrada.startswith("/"):
                comando = procesar_comando(entrada, self.chat)
                comando.ejecutar()
            else:
                self.conexion.enviar_mensaje(entrada)
