from practica1.clases import Segmento


class Accion:
    def __init__(self, segment):
        """
        Inicializa una acción, representa el movimiento a través de un segmento entre dos intersecciones.

        """
        if not isinstance(segment, Segmento):
            raise TypeError("El parámetro debe ser una instancia de la clase Segmento.")

        self.segment = segment
        self.costo = segment.tiempo_viaje()

    def __repr__(self):
        return f"Accion(segmento={self.segment}, costo={self.costo})"