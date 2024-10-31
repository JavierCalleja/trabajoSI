from math import radians, cos, sin, sqrt, atan2

class Interseccion:
    def __init__(self, identifier, longitude, latitude):
        """
        Inicializa una intersección con su identificador y coordenadas de ubicación.
        """
        if not isinstance(identifier, int):
            raise TypeError("El identificador debe ser un entero.")
        if not (-180 <= longitude <= 180) or not (-90 <= latitude <= 90):
            raise ValueError("La longitud debe estar entre -180 y 180 y la latitud entre -90 y 90.")

        self.identifier = identifier
        self.longitude = longitude
        self.latitude = latitude

    def distancia_geodesica(self, otra_interseccion):
        """
        distancia geodésica entre esta intersección y otra, en kilómetros.
        """
        if not isinstance(otra_interseccion, Interseccion):
            raise TypeError("El parámetro debe ser una instancia de la clase Interseccion.")

        # Convertir grados a radianes
        lon1, lat1, lon2, lat2 = map(
            radians,
            [self.longitude, self.latitude, otra_interseccion.longitude, otra_interseccion.latitude]
        )

        # Calcular distancia entre los dos puntos formula de haversine
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        radio_tierra = 6371  # Radio de la Tierra en kilómetros
        return radio_tierra * c

    def __repr__(self):
        return f"Interseccion(id={self.identifier}, lon={self.longitude}, lat={self.latitude})"
