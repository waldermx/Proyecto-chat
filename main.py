from datetime import datetime
import time

class Usuario:
    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = ip

class Mensaje:
    def __init__(self, remitente, contenido):
        self.remitente = remitente
        self.contenido = contenido
        self.timestamp = datetime.now()  # Marca de tiempo del mensaje

    def mostrar(self):
        tiempo_formateado = self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        return f"[{tiempo_formateado}] {self.remitente}: {self.contenido}"

class Conversacion:
    def __init__(self, localUser):
        self.mensajes = []
        self.usuario = localUser

    def agregar_mensaje(self, remitente, contenido):
        mensaje = Mensaje(remitente, contenido)
        self.mensajes.append(mensaje)

    def mostrar_conversacion(self):
        for mensaje in self.mensajes:
            print(mensaje.mostrar())

    def escribir_conversacion(self, delay=0.01):
        for mensaje in self.mensajes:
            for letra in mensaje.mostrar():
                print(letra, end='', flush=True)
                time.sleep(delay)
            print()  # Nueva línea después de cada mensaje
            time.sleep(0.5)  # Pausa entre mensajes

def main():

    #gregar forma d easignar ip y nombre de usuario
    usuario_local = Usuario("Usuario1", "127.0.0.1")

    chat = Conversacion()
    
    chat.agregar_mensaje("Usuario1", "Hola, ¿cómo estás?")
    chat.agregar_mensaje("Usuario2", "¡Hola! Estoy bien, ¿y tú?")
    chat.agregar_mensaje("Usuario1", "Todo bien, gracias.")

    
    chat.escribir_conversacion()

if __name__ == "__main__":
    main()
