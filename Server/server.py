# server.py
import asyncio
from ..cifrado import cifrar_mensaje, descifrar_mensaje

class ServidorChat:
    def __init__(self, host='192.168.1.10', puerto=5000):
        self.host = host
        self.puerto = puerto
        self.clientes = set()  # Conjunto de escritores de clientes conectados

    async def manejar_cliente(self, reader, writer):
        # Añadir el nuevo cliente al conjunto de clientes
        self.clientes.add(writer)
        addr = writer.get_extra_info('peername')
        print(f"Cliente conectado: {addr}")

        try:
            while True:
                datos = await reader.read(1024)
                if not datos:
                    break  # No hay datos, el cliente se ha desconectado
                mensaje_cifrado = datos.decode('utf-8')
                mensaje = descifrar_mensaje(mensaje_cifrado)
                print(f"Mensaje recibido de {addr}: {mensaje}")

                # Retransmitir el mensaje a todos los demás clientes
                await self.retransmitir(mensaje, writer)
        except Exception as e:
            print(f"Error con el cliente {addr}: {e}")
        finally:
            print(f"Cliente desconectado: {addr}")
            self.clientes.remove(writer)
            writer.close()
            await writer.wait_closed()

    async def retransmitir(self, mensaje, remitente_writer):
        mensaje_cifrado = cifrar_mensaje(mensaje)
        datos = mensaje_cifrado.encode('utf-8')
        for writer in self.clientes:
            if writer != remitente_writer:
                try:
                    writer.write(datos)
                    await writer.drain()
                except Exception as e:
                    print(f"Error al enviar mensaje a un cliente: {e}")

    async def iniciar_servidor(self):
        server = await asyncio.start_server(self.manejar_cliente, self.host, self.puerto)
        addr = server.sockets[0].getsockname()
        print(f"Servidor iniciado en {addr}")

        async with server:
            await server.serve_forever()

if __name__ == "__main__":
    servidor = ServidorChat()
    asyncio.run(servidor.iniciar_servidor())
