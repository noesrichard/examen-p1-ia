ORIGEN = 0
DESTINO = 1
COSTE = 2
class Node:
    def __init__(self, parent, name, coste) -> None:
        self.parent: Node = parent
        self.name = name
        self.coste = coste
        self.children: list[Node] = []

    def append_child(self,node):
        self.children.append(node)

    def generate_children(self, routes):
         for r in routes: 
            if r[ORIGEN] == self.name:
                if self.parent and r[DESTINO] != self.parent.name:
                    self.children.append(Node(self, r[DESTINO], r[COSTE]))
                elif r[DESTINO] == "MALL":
                    return Node(self, r[DESTINO], r[COSTE])
                elif self.parent is None: 
                    self.children.append(Node(self, r[DESTINO], r[COSTE]))


    # genera todos los hijos de una misma profundiada
    def generate_by_depth(self, routes, depth):
        # al inicio no hay solucion
        is_solution = None
        # si el nombre del nodo es MALL entonces es una solucion
        # y se retorna a si mismo
        if self.name == "MALL":
            return self

        # si este nodo esta en la profundidad deseada genera sus hijos
        if self.depth() == depth:
            self.generate_children(routes)

        # si el nodo tiene hijos ejecuta el metodo recursivamente
        if self.children:
            for child in self.children:
                solution = child.generate_by_depth(routes, depth)
                if solution and solution.name == "MALL":
                    is_solution = solution
        return is_solution
    
    def search_best_solution(self, solutions):
        if self.name == "MALL":
            solutions.append((self, self.total_cost()))
        else:
            if self.children: 
                for child in self.children: 
                    child.search_best_solution(solutions)
        return solutions

    def depth(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def total_cost(self):
        cost = self.coste
        p = self.parent
        while p:
            cost += p.coste
            p = p.parent
        return cost
 

    def is_leaf(self):
        if self.children:
            return True
        return False


     # impresion del Puzzle
    def print(self, spaces = ''): 
        text = ""
        text += spaces + "_____ \n"
        blanks = ""
        for i in range(len(spaces)):
            if i == len(spaces)-3:
                blanks += "|"
            else:
                blanks += " "
        text += spaces +  str(self.name) + ' COSTE: ' + str(self.total_cost())
        text += '\n'
        text += spaces + '_____ '
        return text

    def print_node(self):
        spaces = " " * self.depth() * 5
        prefix = spaces + "|__" if self.parent else ""
        #self.print_formatted_node_info(node, prefix)
        print(self.print(prefix))
        if self.children:
            for child in self.children:
                child.print_node()
    

    def print_path(self):
        path = [self]
        p = self.parent
        while p: 
            path.append(p)
            p = p.parent
        path.reverse()
        for ps in path:
            print(ps.print())
