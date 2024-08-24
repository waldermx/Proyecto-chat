from usuario import Usuario
from interaccionchat import InteraccionChat

async def iniciar_cliente():
    usuario_local = Usuario("NombreUsuario", "127.0.0.1")
    host = '127.0.0.1'
    puerto = 12345

    chat = InteraccionChat(usuario_local, host, puerto)
    await chat.iniciar()
