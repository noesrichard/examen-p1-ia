from random import randrange

LINKS = {
    0: [1, 2, 4],
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
        self.prob = 0
        self.links = {
            0: [1, 2, 4],
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
            17: [12, 16],
        }
        self.fitness_score = self.__calculate_fitness()

    def __calculate_fitness(self):

        fitness = 0 - self.disconnected_nodes()
        #if 17 in self.path:
            #fitness += 1
        # repeated = 0
        # for i in self.path:
        #     n = self.path.count(i)
        #     if n > 1:
        #         repeated += n * 0.01
        # return 1 - repeated
        return fitness

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
        text += f" fitness = {self.__calculate_fitness()} ]"
        return text

    @classmethod
    def generate(cls):
        path = [0]
        while len(path) < 17:
            # last_point = path[-1]
            #
            # possible_next_points = LINKS[last_point]

            # next_point = possible_next_points[randrange(0, len(possible_next_points))]
            next_point = randrange(1, 17)

            if len(path) == 16:
                next_point = 17

            # if next_point in path:
            #     possible_next_points.remove(next_point)
            #
            # if len(path) >= 2:
            #     if path[-2] in possible_next_points:
            #         possible_next_points.remove(path[-2])

            # next_point = possible_next_points[randrange(0, len(possible_next_points))]

            path.append(next_point)
        path = Path(path)
        return path
