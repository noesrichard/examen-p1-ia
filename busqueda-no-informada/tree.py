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

            self.solution = self.root.generate_by_depth(self.routes, depth)

            depth += 1

            self.root.print_node()
        
            if self.solution is not None:
                break

        self.root.print_node()

        bests = self.search_best_solution()

        bests.sort(key=lambda x: x[1])

        best_cost = bests[0][1]

        bests = [b for b in bests if b[1] <= best_cost]

        for b in bests:
            print(f"\n\n****** RUTA: {b[1]} ******")
            b[0].print_path()


    def search_best_solution(self):
        solutions = []
        return self.root.search_best_solution(solutions)


