from tree import Tree
from node import Node
def generate_graph(): 
    FISEI = "FISEI"
    MALL = "MALL"
    N1 = "N1"
    N2 = "N2"
    N3 = "N3"
    N4 = "N4"
    N5 = "N5"
    N6 = "N6"
    N7 = "N7"
    N8 = "N8"
    N9 = "N9"
    N10 = "N10"
    N11 = "N11"
    N12 = "N12"
    N13 = "N13"
    N14 = "N14"
    N15 = "N15"
    N16 = "N16"
    return [
        (FISEI, N1, 100),
        (FISEI, N2, 90),
        (FISEI, N4, 150),
        (N1, N3, 100),
        (N2, N5, 50),
        (N4, N3, 80),
        (N4, N5, 70),
        (N4, N9, 100),
        (N3, N4, 80),
        (N3, N8, 100),
        (N5, N4, 70),
        (N5, N10, 100),
        (N5, N6, 100),
        (N6, N5, 100),
        (N6, N11, 100),
        (N6, N7, 120),
        (N7, N6, 120),
        (N7, N12, 100),
        (N8, N3, 100),
        (N8, N13, 150),
        (N8, N9, 80),
        (N9, N8, 80),
        (N9, N10, 65),
        (N9, N4, 100),
        (N9, N14, 100),
        (N10, N9, 65),
        (N10, N5, 100),
        (N10, N11, 80),
        (N10, N15, 100),
        (N11, N10, 80),
        (N11, N12, 120),
        (N11, N6, 100),
        (N11, N16, 100),
        (N12, N7, 100),
        (N12, MALL, 120),
        (N13, N8, 150),
        (N13, N14, 180),
        (N14, N13, 180),
        (N14, N9, 100),
        (N14, N15, 60),
        (N15, N14, 60),
        (N15, N10, 100),
        (N15, N16, 80),
        (N16, N15, 80),
        (N16, N11, 100),
        (N16, MALL, 70),
    ]

if __name__ == "__main__":
    graph = generate_graph()
    tree = Tree(Node(None, "FISEI", 0), graph)
    tree.generate()

