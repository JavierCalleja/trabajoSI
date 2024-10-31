from practica1.clases.Interseccion import Interseccion

class Segmento:
    def __init__(self, origin, destination, distance, speed):
        """
        Inicializa un segmento entre dos intersecciones, con la distancia y velocidad permitida.
        """
        if not isinstance(origin, Interseccion) or not isinstance(destination, Interseccion):
            raise TypeError("Origen y destino deben ser instancias de la clase Interseccion.")
        if not (isinstance(distance, (int, float)) and distance > 0):
            raise ValueError("La distancia debe ser un número positivo.")
        if not (isinstance(speed, (int, float)) and speed > 0):
            raise ValueError("La velocidad debe ser un número positivo.")

        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.speed = speed

    def tiempo_viaje(self):
        """
        Calcula el tiempo aproximado en este segmento.
        """
        return self.distance / self.speed

    def conecta_intersecciones(self, interseccion1, interseccion2):
        """
        Verifica si el segmento conecta dos intersecciones dadas.
        """
        return (self.origin == interseccion1 and self.destination == interseccion2) or \
               (self.origin == interseccion2 and self.destination == interseccion1)

    def __repr__(self):
        return f"Segmento(origen={self.origin.identifier}, destino={self.destination.identifier}, distancia={self.distance}, velocidad={self.speed})"
