import asyncio
from conexiones import ConexionCliente
from conversacion import Conversacion
from comandos import procesar_comando

class InteraccionChat:
    def __init__(self, usuario_local, host, puerto):
        self.conexion = ConexionCliente(host, puerto)
        self.chat = Conversacion(usuario_local)

    async def iniciar(self):
        if not await self.conexion.conectar():
            return

        asyncio.create_task(self.conexion.recibir_mensajes(self.chat))
        await self.ciclo_principal()

    async def ciclo_principal(self):
        while True:
            entrada = await self.leer_entrada_usuario()
            if entrada.startswith("/"):
                comando = procesar_comando(entrada, self.chat)
                comando.ejecutar()
            else:
                await self.conexion.enviar_mensaje(entrada)

    async def leer_entrada_usuario(self):
        return await asyncio.get_event_loop().run_in_executor(None, input, "> ")

