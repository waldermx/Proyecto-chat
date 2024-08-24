from mensaje import Mensaje
import time

class Conversacion:
    def __init__(self, remitente, destinatario):
        self.remitente = remitente
        self.destinatario = destinatario
        self.mensajes = []

    def agregar_mensaje(self, remitente, contenido, destinatario):
        mensaje = Mensaje(remitente, contenido, destinatario)
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
