import datetime
from queue import PriorityQueue

from practica1.clases.ProblemaRuta import ProblemaRuta
from practica1.clases.Nodo import Nodo
from practica1.clases.Estado import Estado

class BusquedaEstrella:
    def __init__(self, problema):
        """
        Inicializa el algoritmo A*
        """
        if not isinstance(problema, ProblemaRuta):
            raise TypeError("El parámetro problema debe ser una instancia de la clase ProblemaRuta.")

        self.problema = problema
        self.frontera = PriorityQueue()  # cola de prioridad para la frontera
        self.explorados = set()  # Conjunto de estados explorados
        self.nodos_generados = 0
        self.nodos_expandidos = 0

    def heuristica(self, estado):
        """
        Calcula la heurística para el estado
        """
        # Distancia al objetivo
        return estado.current_location.distancia_geodesica(self.problema.goal_state.current_location)

    def buscar(self):
        """
        Ejecuta el algoritmo A* para encontrar la ruta óptima desde el estado inicial al objetivo.
        return: Ruta óptima como lista de acciones, o None si no hay
        """
        start_time = datetime.datetime.now()  # Inicia el temporizador

        nodo_inicial = Nodo(
            estado=self.problema.initial_state,
            costo_acumulado=0,
            heuristica=self.heuristica(self.problema.initial_state)
        )
        self.frontera.put((nodo_inicial.costo_total, nodo_inicial))
        self.nodos_generados += 1

        while not self.frontera.empty():
            _, nodo = self.frontera.get()
            self.nodos_expandidos += 1

            if self.problema.es_estado_objetivo(nodo.estado):
                end_time = datetime.datetime.now()  # Finaliza el temporizador
                return self.mostrar_resultado(nodo, start_time, end_time)

            self.explorados.add(nodo.estado)

            for accion in self.problema.acciones_posibles(nodo.estado):
                estado_resultante = Estado(
                    accion.segment.destination if accion.segment.origin == nodo.estado.current_location else accion.segment.origin
                )
                costo_nuevo = nodo.costo_acumulado + self.problema.costo_accion(accion)

                nodo_hijo = Nodo(
                    estado=estado_resultante,
                    padre=nodo,
                    accion=accion,
                    costo_acumulado=costo_nuevo,
                    heuristica=self.heuristica(estado_resultante)
                )

                if estado_resultante not in self.explorados:
                    self.frontera.put((nodo_hijo.costo_total, nodo_hijo))
                    self.nodos_generados += 1

        return None

    def mostrar_resultado(self, nodo, start_time, end_time):
        """
        Muestra el resultado de la búsqueda A*.
        nodo: Nodo objetivo
        return: lista de acciones que llevan desde el estado inicial hasta el estado objetivo.
        """
        camino = self.reconstruir_camino(nodo)
        solucion = [f"{accion.segment.origin} → {accion.segment.destination} ({accion.costo:.5f})" for accion in camino]

        print(f"Generated nodes: {self.nodos_generados}")
        print(f"Expanded nodes: {self.nodos_expandidos}")
        print(f"Execution time: {end_time - start_time}")
        print(f"Solution length: {len(camino)}")
        print(f"Solution cost: {nodo.costo_acumulado:.5f}")
        print(f"Solution: {solucion}")

        return camino

    def reconstruir_camino(self, nodo):
        """
        Reconstruye el camino desde el estado inicial hasta el objetivo a través de los nodos padres.
        nodo: Nodo objetivo para reconstruir el camino
        return: lista de acciones que llevan desde el estado inicial hasta el estado objetivo.
        """
        camino = []
        while nodo.padre is not None:
            camino.append(nodo.accion)
            nodo = nodo.padre
        return list(reversed(camino))  # Invertir el camino para que vaya desde el inicio hasta el objetivo
