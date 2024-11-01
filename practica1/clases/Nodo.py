from practica1.clases.Estado import Estado

class Nodo:
    def __init__(self, estado, padre=None, accion=None, costo_acumulado=0, heuristica=0):
        """
        Inicializa un nodo en el espacio de búsqueda.

        """
        if not isinstance(estado, Estado):
            raise TypeError("El estado debe ser una instancia de la clase Estado.")

        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.costo_acumulado = costo_acumulado
        self.heuristica = heuristica
        self.costo_total = costo_acumulado + heuristica  # f(n) = g(n) + h(n)

    def __lt__(self, other):
        """
        Comparación de nodos por costo total
        """
        return self.costo_total < other.costo_total

    def __repr__(self):
        return f"Nodo(estado={self.estado}, costo_total={self.costo_total}, heuristica={self.heuristica})"
