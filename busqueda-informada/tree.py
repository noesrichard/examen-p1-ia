from node import Node

class Tree:

    def __init__(self, root: Node, routes):
        self.root = root
        self.routes = routes
        self.expanded_nodes = []
        self.current = root
        self.leafs = [self.root]
        self.solution = None
        self.solutions: list[Node] = []
        self.open_nodes = 0
        self.iter = 0


    def generate(self):
        self.current = self.root

        # mientras no haya solucion o la solucion no sea la menor del arbol
        while (self.solution is None 
            or self.solution is not self.root.search_leaf_node_lower_or_equal_than(self.solution)):
            self.iter += 1
            print(f"Busqueda: {self.iter}")

            # escoje la hoja de menor valor
            leaf_node = self.leafs[0]
            # busca una hoja de menor valor
            self.current = self.root.search_leaf_node_lower_or_equal_than(leaf_node)

            if self.current:
                # genera los hijos (acciones, movimientos)
                self.solution = self.current.generate_children(self.routes)

                if self.solution:
                    self.solutions.append(self.solution)

                if self.current.children:

                    #elimina el nodo abierto de las hojas
                    self.leafs.remove(self.current)
                    self.open_nodes += 1

                    # agrega los nodos hijos a los nodos hojas
                    for child in self.current.children:
                        if child.name == "MALL":
                            self.solutions.append(child)
                        self.leafs.append(child)

            self.leafs.sort(key=lambda hoja: hoja.f())

            self.root.print_node()

        self.solutions.sort(key= lambda x: x.f())

        self.solutions[0].print_path()



