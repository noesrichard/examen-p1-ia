ORIGEN = 0
DESTINO = 1
COSTE = 2
H = 3
class Node:
    def __init__(self, parent, name, coste, h) -> None:
        self.parent: Node = parent
        self.name = name
        self.coste = coste
        self.children: list[Node] = []
        self.h_value = h

    def append_child(self,node):
        self.children.append(node)

    def generate_children(self, routes):
        if self.name == "MALL":
            return self
        for r in routes: 
            # generamos los hijos que tienen como origen el nodo actual
            if r[ORIGEN] == self.name:

                # si este nodo tiene padre y el destion es diferente del padre se genera un hijo
                if self.parent and r[DESTINO] != self.parent.name:
                    child = Node(self, r[DESTINO], r[COSTE], r[H] )
                    self.children.append(child)

                # en caso de que el nodo sea la raiz
                elif self.parent is None: 
                    self.children.append(Node(self, r[DESTINO], r[COSTE], r[H]))
        return None


    # buscar nodos menor o igual que el nodo actual en f(n)
    def search_leaf_node_lower_or_equal_than(self, lowest):
        # si el nodo es una hoja y si es menor o igual al nodo menor se retorna a si mismo
        if self.is_leaf() and self.lower_or_equal_f_than(lowest):
            return self
        # si tiene hijos busca en sus hijos con recursivdidad
        if self.children:
            for child in self.children:
                lowest = child.search_leaf_node_lower_or_equal_than(lowest)
        return lowest

    def search_leaf_node_lower_than(self, lowest):
        # si el nodo es una hoja y si es menor o igual al nodo menor se retorna a si mismo
        if self.is_leaf() and self.lower_f_than(lowest):
            return self
        # si tiene hijos busca en sus hijos con recursivdidad
        if self.children:
            for child in self.children:
                lowest = child.search_leaf_node_lower_than(lowest)
        return lowest

    # comparacion entre f(n) del nodo actual y del menor
    def lower_or_equal_f_than(self, other) -> bool:
        return self.f() <= other.f()

    def lower_f_than(self, other) -> bool:
        return self.f() < other.f()

    def g(self):
        cost = self.coste
        p = self.parent
        while p:
            cost += p.coste
            p = p.parent
        return cost

    def h(self):
        return self.h_value

    def f(self):
        return self.g() + self.h()

    def depth(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def is_leaf(self):
        if self.children:
            return False
        return True


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
        text += spaces +  str(self.name) + f' f(n) = {self.f()}, g(n) = {self.g()}, h(n) = {self.h()}'
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
