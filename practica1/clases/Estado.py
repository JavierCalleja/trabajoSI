from practica1.clases import Interseccion


class Estado:
    def __init__(self, current_location):
        """
        Inicializa un estado en el espacio de búsqueda, ubicación actual

        """
        if not isinstance(current_location, Interseccion):
            raise TypeError("La ubicación actual debe ser una instancia de la clase Interseccion.")

        self.current_location = current_location

    def __eq__(self, other):
        """
        Compara si dos estados son iguales en base a su ubicación actual.

        """
        return isinstance(other, Estado) and self.current_location.identifier == other.current_location.identifier

        ##true si son iguales
    def __hash__(self):
        """
        hash de un estado, basado en su ubicación
        uso en conjuntos y diccionarios.

        """
        return hash(self.current_location.identifier)

    def __repr__(self):
        return f"Estado(ubicacion_actual={self.current_location.identifier})"