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
        (FISEI, N1, 383),
        (FISEI, N2, 286),
        (FISEI, N4, 288),
        (FISEI, N5, 312),

        (N1, N3, 237),

        (N2, N6, 90),
        (N2, N7, 175),

        (N3, N8, 90),
        (N3, N4, 130),

        (N4, N3, 130),
        (N4, N9, 100),
        (N4, N5, 150),


        (N5, N4, 150),
        (N5, N10, 100),
        (N5, N6, 150),

        (N6, N5, 150),
        (N6, N2, 90),
        (N6, N11, 115),
        (N6, N7, 135),

        (N7, N6, 135),
        (N7, N2, 175),
        (N7, N12, 130),

        (N8, N3, 90),
        (N8, N13, 220),
        (N8, N9, 125),

        (N9, N8, 125),
        (N9, N10, 165),
        (N9, N4, 100),
        (N9, N14, 230),

        (N10, N9, 165),
        (N10, N5, 100),
        (N10, N11, 135),
        (N10, N15, 150),

        (N11, N10, 135),
        (N11, N12, 145),
        (N11, N6, 115),
        (N11, N16, 105),

        (N12, N7, 130),
        (N12, N11, 145),
        (N12, MALL, 155),

        (N13, N8, 220),
        (N13, N14, 115),

        (N14, N13, 115),
        (N14, N9, 230),
        (N14, N15, 240),

        (N15, N14, 240),
        (N15, N10, 150),
        (N15, N16, 100),

        (N16, N15, 100),
        (N16, N11, 105),
        (N16, MALL, 165),
    ]

if __name__ == "__main__":
    graph = generate_graph()
    tree = Tree(Node(None, "FISEI", 0), graph)
    tree.generate()

