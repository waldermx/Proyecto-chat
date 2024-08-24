from mensaje import Mensaje
import time

class Conversacion:
    def __init__(self, usuario_local):
        self.usuarios = [usuario_local]
        self.mensajes = []
        self.usuario_local = usuario_local

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_mensaje(self, remitente, contenido):
        mensaje = Mensaje(remitente, contenido)
        self.mensajes.append(mensaje)

    def mostrar_conversacion(self):
        for mensaje in self.mensajes:
            print(mensaje.mostrar())

    def escribir_conversacion(self, delay=0.1):
        for mensaje in self.mensajes:
            for letra in mensaje.mostrar():
                print(letra, end='', flush=True)
                time.sleep(delay)
            print()
            time.sleep(0.5)
