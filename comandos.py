from comando import SalirComando, UsuariosComando, MensajeComando, ComandoNoReconocido

def procesar_comando(comando, chat):
    if comando == "/salir":
        return SalirComando(chat)
    elif comando == "/usuarios":
        return UsuariosComando(chat)
    elif comando.startswith("/msg "):
        partes = comando.split(" ", 2)
        if len(partes) < 3:
            print("Uso: /msg <usuario> <mensaje>")
            return ComandoNoReconocido(chat, comando)
        else:
            nombre_usuario = partes[1]
            contenido_mensaje = partes[2]
            return MensajeComando(chat, nombre_usuario, contenido_mensaje)
    else:
        return ComandoNoReconocido(chat, comando)
