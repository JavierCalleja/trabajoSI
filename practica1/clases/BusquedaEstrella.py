from queue import PriorityQueue

from practica1.clases import ProblemaRuta, Estado, Nodo



class BusquedaEstrella:
    def __init__(self, problema):
        """
        Inicializa el algoritmo A* para un problema de búsqueda en el espacio de estados.

        """
        if not isinstance(problema, ProblemaRuta):
            raise TypeError("El parámetro problema debe ser una instancia de la clase ProblemaRuta.")

        self.problema = problema
        self.frontera = PriorityQueue()  # cola de prioridad para la frontera
        self.explorados = set()  # Conjunto de estados explorados

    def heuristica(self, estado):
        """
        calcula la heurística para el estado dado

        """
        return estado.current_location.distancia_geodesica(self.problema.goal_state.current_location)

    def buscar(self):
        """
        Ejecuta el algoritmo A* para encontrar la ruta óptima desde el estado inicial al objetivo.

        return: Ruta óptima como lista de acciones, o None si no hay ruta
        """
        # Nodo inicial
        nodo_inicial = Nodo(
            estado=self.problema.initial_state,
            costo_acumulado=0,
            heuristica=self.heuristica(self.problema.initial_state)
        )
        self.frontera.put((nodo_inicial.costo_total, nodo_inicial))

        while not self.frontera.empty():
            # extraer el nodo de la frontera con el menor costo total
            _, nodo = self.frontera.get()

            # Si el nodo contiene el estado objetivo, reconstruir y retornar el camino
            if self.problema.es_estado_objetivo(nodo.estado):
                return self.reconstruir_camino(nodo)

            # estado explorado
            self.explorados.add(nodo.estado)

            # expandir nodo
            for accion in self.problema.acciones_posibles(nodo.estado):
                estado_resultante = Estado(
                    accion.segment.destination if accion.segment.origin == nodo.estado.current_location else accion.segment.origin
                )
                costo_nuevo = nodo.costo_acumulado + self.problema.costo_accion(accion)

                #nodo hijo
                nodo_hijo = Nodo(
                    estado=estado_resultante,
                    padre=nodo,
                    accion=accion,
                    costo_acumulado=costo_nuevo,
                    heuristica=self.heuristica(estado_resultante)
                )

                # Si estado resultante no es explorado o tiene costo menor, agregar a la frontera
                if estado_resultante not in self.explorados:
                    self.frontera.put((nodo_hijo.costo_total, nodo_hijo))

        return None

    def reconstruir_camino(self, nodo):
        """
        Reconstruye el camino desde el estado inicial al objetivo a través de los nodos padres
        """
        camino = []
        while nodo.padre is not None:
            camino.append(nodo.accion)
            nodo = nodo.padre
        return list(reversed(camino))  # Invertir el camino para que vaya desde el inicio hasta el objetivo

    def __repr__(self):
        return f"BusquedaEstrella(problema={self.problema})"
