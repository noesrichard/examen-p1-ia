from random import randrange

LINKS = {
    0: [1, 2, 4, 5],
    1: [3, 0],
    2: [5, 0],
    3: [1, 8, 4],
    4: [3, 9, 5, 0],
    5: [2, 4, 10, 6],
    6: [5, 11, 7],
    7: [6, 12],
    8: [3, 9, 13],
    9: [8, 4, 14, 10],
    10: [9, 5, 15, 11],
    11: [10, 6, 16, 12],
    12: [11, 7, 17],
    13: [8, 14],
    14: [13, 9, 15],
    15: [14, 10, 16],
    16: [15, 11, 17],
}


class Path:
    def __init__(self, path: list[int]) -> None:
        self.path = path
        self.prob: float = 0
        self.links = {
            0: [1, 2, 4, 5],
            1: [3, 0, 1],
            2: [6, 0, 7, 2],
            3: [1, 8, 4, 3],
            4: [3, 9, 5, 0, 4],
            5: [0, 4, 10, 6, 5],
            6: [5, 11, 7, 2, 6],
            7: [6, 12, 2, 7],
            8: [3, 9, 13, 8],
            9: [8, 4, 14, 10, 9],
            10: [9, 5, 15, 11, 10],
            11: [10, 6, 16, 12, 11],
            12: [11, 7, 17, 12],
            13: [8, 14, 13],
            14: [13, 9, 15, 14],
            15: [14, 10, 16, 15],
            16: [15, 11, 17, 16],
            17: [12, 16, 17],
        }
        self.fitness_score = self.fitness()

    def fitness(self):
        fitness_val = 0 - self.disconnected_nodes()
        return fitness_val

    def clean(self):
        self.clean_vueltas()
        self.clean_repeateds()


    def clean_repeateds(self):
        i = 0
        while i < len(self.path)-1:
            current_node = self.path[i]
            next_node = self.path[i+1]
            if next_node == current_node:
                del self.path[i+1]
                i = 0
            i += 1

    def clean_vueltas(self):
        i = 0
        while i < len(self.path)-2:
            current_node = self.path[i]
            next_two_nodes = self.path[i+2]
            if next_two_nodes == current_node:
                del self.path[i+1]
                del self.path[i+1]
                i = 0
            i += 1

    def disconnected_nodes(self):
        count = 0
        for i in range(len(self.path) - 1):
            current_node = self.path[i]
            current_node_links = self.links[current_node]
            next_node = self.path[i+1]
            if current_node not in self.links:
                count += 1
            if next_node not in current_node_links:
                count += 1
        return count

    def is_valid(self):
        for i in range(len(self.path) - 1):
            current_node = self.path[i]
            current_node_links = self.links[current_node]
            next_node = self.path[i+1]
            if current_node not in self.links:
                return False
            if next_node not in current_node_links:
                return False
        return True

    def __str__(self) -> str:
        text = "[ "
        for i in self.path:
            text += str(i) + ", "
        text += f" fitness = {self.fitness()} ]"
        return text

    @classmethod
    def generate(cls):
        path = [0]
        while len(path) <= 17:
            next_point = randrange(1, 17)

            if len(path) == 17:
                next_point = 17

            path.append(next_point)
        path = Path(path)
        return path


    def __stand(self):
        points = 0
        for i in range(2,len(self.path) - 1):
            next_node = self.path[i+1]
            current_node = self.path[i]
            if next_node == current_node:
                points += 1
        return points

    def __vueltas(self):
        points = 0
        for i in range(2,len(self.path) - 1):
            next_node = self.path[i+1]
            previous_node = self.path[i-1]
            if next_node == previous_node:
                points += 1
        return points


