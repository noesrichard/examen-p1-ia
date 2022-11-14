from node import Node

class Tree:

    def __init__(self, root: Node, routes):
        self.root = root
        self.routes = routes
        self.expanded_nodes = []
        self.current = root
        self.leafs = [self.root]
        self.solution = None


    def generate(self):
        depth = 0
        while self.solution is None:


            print(f"************** {depth} ************")
            # genera por profundiad o primero amplitud
            self.solution = self.root.generate_by_depth(self.routes, depth)

            depth += 1

            # imprime los nodos
            self.root.print_node()

            # rompe el ciclo cuando encuentra la solucion
            if self.solution is not None:
                break

        # imprime todo el arbol
        self.root.print_node()

        # busca todas las soluciones
        bests = self.search_best_solution()

        # ordena
        bests.sort(key=lambda x: x[1])

        # escoge el menor costo
        best_cost = bests[0][1]

        # elige las que tienen un costo menor o igual al menor costo
        bests = [b for b in bests if b[1] <= best_cost]

        # imprime las soluciones
        for b in bests:
            print(f"\n\n****** RUTA: {b[1]} ******")
            b[0].print_path()


    def search_best_solution(self):
        solutions = []
        return self.root.search_best_solution(solutions)


