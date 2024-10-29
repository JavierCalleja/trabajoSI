from practica1.clases import Estado, Interseccion, Segmento, Accion



class ProblemaRuta:
    def __init__(self, initial_state, goal_state, intersecciones, segmentos):
        """
        Inicializa el problema de búsqueda de rutas en el espacio de estados.

        """
        if not isinstance(initial_state, Estado) or not isinstance(goal_state, Estado):
            raise TypeError("Los estados inicial y final deben ser instancias de la clase Estado.")
        if not isinstance(intersecciones, dict) or not all(
                isinstance(k, int) and isinstance(v, Interseccion) for k, v in intersecciones.items()):
            raise TypeError(
                "Intersecciones debe ser un diccionario con identificadores como claves y objetos Interseccion como valores.")
        if not isinstance(segmentos, list) or not all(isinstance(s, Segmento) for s in segmentos):
            raise TypeError("Segmentos debe ser una lista de instancias de la clase Segmento.")

        self.initial_state = initial_state
        self.goal_state = goal_state
        self.intersecciones = intersecciones
        self.segmentos = segmentos

    def es_estado_objetivo(self, estado):
        """
        Determina si el estado dado es el estado objetivo.

        """
        return estado == self.goal_state

    ##true si es estado objetivo

    def acciones_posibles(self, estado):
        """
        Devuelve una lista de acciones posibles desde un estado

        """
        acciones = []
        for segmento in self.segmentos:
            if segmento.origin == estado.current_location or segmento.destination == estado.current_location:
                acciones.append(Accion(segmento))
        return acciones

    ##lista de acciones posibles

    def costo_accion(self, accion):
        """
        Calcula el coste de una acción, basado en el tiempo de viaje del segmento.

        """
        return accion.costo

    def __repr__(self):
        return f"ProblemaRuta(inicio={self.initial_state}, objetivo={self.goal_state})"