from datetime import datetime

class Mensaje:
    def __init__(self, remitente, contenido):
        self.remitente = remitente
        self.contenido = contenido
        self.timestamp = datetime.now()

    def mostrar(self):
        tiempo_formateado = self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        return f"[{tiempo_formateado}] {self.remitente.nombre}: {self.contenido}"
