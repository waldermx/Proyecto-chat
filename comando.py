from abc import ABC, abstractmethod

class Comando(ABC):
    def __init__(self, chat):
        self.chat = chat

    @abstractmethod
    def ejecutar(self):
        pass

class SalirComando(Comando):
    def ejecutar(self):
        print("Saliendo del chat...")
        exit(0)

class UsuariosComando(Comando):
    def ejecutar(self):
        print("Usuarios conectados:")
        for usuario in self.chat.usuarios:
            print(f"- {usuario.nombre} ({usuario.ip})")

class MensajeComando(Comando):
    def __init__(self, chat, nombre_usuario, contenido_mensaje):
        super().__init__(chat)
        self.nombre_usuario = nombre_usuario
        self.contenido_mensaje = contenido_mensaje

    def ejecutar(self):
        for usuario in self.chat.usuarios:
            if usuario.nombre == self.nombre_usuario:
                self.chat.agregar_mensaje(self.chat.usuario_local, f"Privado a {self.nombre_usuario}: {self.contenido_mensaje}")
                break
        else:
            print(f"Usuario '{self.nombre_usuario}' no encontrado.")

class ComandoNoReconocido(Comando):
    def __init__(self, chat, comando):
        super().__init__(chat)
        self.comando = comando

    def ejecutar(self):
        print(f"Comando '{self.comando}' no reconocido.")
