def ejecutar_comando(comando, chat):
    if comando == "/salir":
        print("Saliendo del chat...")
        exit(0)
    elif comando == "/usuarios":
        print("Usuarios conectados:")
        for usuario in chat.usuarios:
            print(f"- {usuario.nombre} ({usuario.ip})")
    elif comando.startswith("/msg "):
        partes = comando.split(" ", 2)
        if len(partes) < 3:
            print("Uso: /msg <usuario> <mensaje>")
        else:
            nombre_usuario = partes[1]
            contenido_mensaje = partes[2]
            for usuario in chat.usuarios:
                if usuario.nombre == nombre_usuario:
                    chat.agregar_mensaje(chat.usuario_local, f"Privado a {nombre_usuario}: {contenido_mensaje}")
                    break
            else:
                print(f"Usuario '{nombre_usuario}' no encontrado.")
    else:
        print(f"Comando '{comando}' no reconocido.")

def procesar_entrada(entrada, chat):
    if entrada.startswith("/"):
        ejecutar_comando(entrada, chat)
    else:
        chat.agregar_mensaje(chat.usuario_local, entrada)
