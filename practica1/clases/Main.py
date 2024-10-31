from practica1.clases.Interseccion import Interseccion
from practica1.clases.Estado import Estado
from practica1.clases.Segmento import Segmento
from practica1.clases.ProblemaRuta import ProblemaRuta
from practica1.clases.BusquedaEstrella import BusquedaEstrella

class Main:
    @staticmethod
    def main():
        # ejemplo
        intersecciones = {
            1: Interseccion(1, 38.994, -1.858),
            2: Interseccion(2, 38.995, -1.859),
            3: Interseccion(3, 38.996, -1.860),
            4: Interseccion(4, 38.997, -1.861)
        }


        segmentos = [
            Segmento(intersecciones[1], intersecciones[2], distance=15.8, speed=50),
            Segmento(intersecciones[2], intersecciones[3], distance=18.3, speed=40),
            Segmento(intersecciones[3], intersecciones[4], distance=8.5, speed=30),
            Segmento(intersecciones[4], intersecciones[1], distance=11.7, speed=60)
        ]

        # Definir estado inicial y estado objetivo
        estado_inicial = Estado(intersecciones[1])
        estado_objetivo = Estado(intersecciones[4])

        # crear el problema de ruta
        problema_ruta = ProblemaRuta(estado_inicial, estado_objetivo, intersecciones, segmentos)


        busqueda = BusquedaEstrella(problema_ruta)
        busqueda.buscar()


if __name__ == "__main__":
    Main.main()
