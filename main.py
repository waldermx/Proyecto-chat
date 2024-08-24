from usuario import Usuario
from cliente import iniciar_cliente

if __name__ == "__main__":
    usuario_local = Usuario("Usuario1", "127.0.0.1")
    iniciar_cliente(usuario_local)
