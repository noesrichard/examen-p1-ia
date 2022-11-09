from tree import Tree
from node import Node


def generate_graph():

    NAME = 0
    H = 1

    FISEI = "FISEI", 525
    MALL = "MALL", 0
    N1 = "N1", 740
    N2 = "N2", 370
    N3 = "N3", 620
    N4 = "N4", 510
    N5 = "N5", 390
    N6 = "N6", 310
    N7 = "N7", 285
    N8 = "N8", 590
    N9 = "N9", 470
    N10 = "N10", 315
    N11 = "N11", 215
    N12 = "N12", 155
    N13 = "N13", 570
    N14 = "N14", 465
    N15 = "N15", 245
    N16 = "N16", 160
    return [
        (FISEI[NAME], N1[NAME], 383, N1[H]),
        (FISEI[NAME], N2[NAME], 286, N2[H]),
        (FISEI[NAME], N4[NAME], 288, N4[H]),
        (FISEI[NAME], N5[NAME], 312, N5[H]),
        (N1[NAME], N3[NAME], 237, N3[H]),
        (N2[NAME], N6[NAME], 90, N6[H]),
        (N2[NAME], N7[NAME], 175, N7[H]),
        (N3[NAME], N8[NAME], 90, N8[H]),
        (N3[NAME], N4[NAME], 130, N4[H]),
        (N4[NAME], N3[NAME], 130, N3[H]),
        (N4[NAME], N9[NAME], 100, N9[H]),
        (N4[NAME], N5[NAME], 150, N5[H]),
        (N5[NAME], N4[NAME], 150, N4[H]),
        (N5[NAME], N10[NAME], 100, N10[H]),
        (N5[NAME], N6[NAME], 150, N6[H]),
        (N6[NAME], N5[NAME], 150, N5[H]),
        (N6[NAME], N11[NAME], 115, N11[H]),
        (N6[NAME], N7[NAME], 135, N7[H]),
        (N7[NAME], N6[NAME], 135, N6[H]),
        (N7[NAME], N2[NAME], 175, N2[H]),
        (N7[NAME], N12[NAME], 130, N12[H]),
        (N8[NAME], N3[NAME], 90, N3[H]),
        (N8[NAME], N13[NAME], 220, N13[H]),
        (N8[NAME], N9[NAME], 125, N9[H]),
        (N9[NAME], N8[NAME], 125, N8[H]),
        (N9[NAME], N10[NAME], 165, N10[H]),
        (N9[NAME], N4[NAME], 100, N4[H]),
        (N9[NAME], N14[NAME], 230, N14[H]),
        (N10[NAME], N9[NAME], 165, N9[H]),
        (N10[NAME], N5[NAME], 100, N5[H]),
        (N10[NAME], N11[NAME], 135, N11[H]),
        (N10[NAME], N15[NAME], 150, N15[H]),
        (N11[NAME], N10[NAME], 135, N10[H]),
        (N11[NAME], N12[NAME], 145, N12[H]),
        (N11[NAME], N6[NAME], 115, N6[H]),
        (N11[NAME], N16[NAME], 105, N16[H]),
        (N12[NAME], N7[NAME], 130, N7[H]),
        (N12[NAME], N11[NAME], 145, N11[H]),
        (N12[NAME], MALL[NAME], 155, MALL[H]),
        (N13[NAME], N8[NAME], 220, N8[H]),
        (N13[NAME], N14[NAME], 115, N14[H]),
        (N14[NAME], N13[NAME], 115, N13[H]),
        (N14[NAME], N9[NAME], 230, N9[H]),
        (N14[NAME], N15[NAME], 240, N15[H]),
        (N15[NAME], N14[NAME], 240, N14[H]),
        (N15[NAME], N10[NAME], 150, N10[H]),
        (N15[NAME], N16[NAME], 100, N16[H]),
        (N16[NAME], N15[NAME], 100, N15[H]),
        (N16[NAME], N11[NAME], 105, N11[H]),
        (N16[NAME], MALL[NAME], 165, MALL[H]),
    ]


if __name__ == "__main__":
    graph = generate_graph()
    tree = Tree(Node(None, "FISEI", 0, 525), graph)
    tree.generate()
