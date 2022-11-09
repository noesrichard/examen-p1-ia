from path import Path
from random import randrange, shuffle

class PathAlgorithm:

    def __init__(self) -> None:
        self.MAX_POPULATION = 8
        self.MUTATION_RATE = 50 

        # Generacion de la poblacion inicial
        self.population = self.__generate_population()
        self.population.sort(key=lambda x: x.fitness(), reverse=True)
        self.children = []

        self.solution = None

    # Algoritmo genetico
    def solve(self):
        i = 0
        while not self.__is_solved():

            #self.population.append(Board([7, 3, 8, 2, 5, 1, 6, 4]))

            self.population.sort(key= lambda x: x.fitness(), reverse=True)
            # Imprimir individuos en la poblacion
            print(f"\n************* ITERATION: {i} *************")
            self.__print_individuos(*self.population)

            # Seleccion de padres
            father, mother = self.__select_parents()

            # Crossover, generacion de hijos
            child_one, child_two = self.__crossover(father, mother)

            # Mutacion de hijos
            child_one, child_two = self.__mutation(child_one, child_two)

            # Modificar la poblacion, para generar la proxima generacion
            self.__next_generation(child_one, child_two)


            # Imprimir padres
            print("\n---------------- PADRES ----------------")
            self.__print_individuos(father, mother)

            # Imprimir hijos
            print("\n---------------- HIJOS -----------------")
            self.__print_individuos(child_one, child_two)

            i += 1

        print("\n\n************* SOLUCION **************")
        self.solution = self.search_solution()
        if self.solution:
            print(self.solution)
            self.solution.clean()
            print(self.solution)


    def __generate_population(self) -> list[Path]:
        # Generamos la poblacion inicial 
        population = [Path.generate() for _ in range(self.MAX_POPULATION)]
        #population.sort(key=lambda x: x.fitness(), reverse=True)
        return population

    def __select_parents(self):

        # Acumulacion total del puntaje de ajuste
        total_score = 0
        for ind in self.population:
            total_score += abs(ind.fitness())

        self.population.sort(key= lambda x: x.fitness(), reverse=True)

        bag = []
        total_ranks = 0
        total_prob = 0
        for i, ind in enumerate(self.population):
            total_ranks += i+1

        for i, ind in enumerate(self.population):
            ind.prob = total_ranks / (i+1)
            total_prob += ind.prob

        for ind in self.population:
            probability = (ind.prob * 100) / total_prob
            for _ in range(round(probability)):
                bag.append(ind)

        print(len(bag))
        # Randomizamos la posicion de los individuos en la bolsa
        shuffle(bag)

        # Elejimos a los padres de una manera randomica
        father: Path = bag[randrange(0, len(bag))]
        mother: Path = bag[randrange(0, len(bag))]
        while father == mother:
            mother: Path = bag[randrange(0, len(bag))]

        return father, mother


    def __crossover(self, father: Path, mother: Path):
        # Punto de cruce o corte
        if len(father.path) >= len(mother.path):
            cut = randrange(1, len(mother.path))
        else:
            cut = randrange(1, len(father.path))
        print(f" CUT: {cut}")

        # Cruce de los genes
        child_one_queens: list[int] = father.path[:cut] + mother.path[cut:]
        child_two_queens: list[int] = mother.path[:cut] + father.path[cut:]

        # Generacion de dos hijos con dichos genes
        child_one = Path(child_one_queens)
        child_two = Path(child_two_queens)

        return child_one, child_two


    def __mutation(self, child_one: Path, child_two):
        if randrange(0, 100) < self.MUTATION_RATE:
            if randrange(0,2) == 1:
                child_one.path[randrange(1, len(child_one.path)-1)] = randrange(1, 17)
                print("MUTO HIJO 1")
            else: 
                child_two.path[randrange(1, len(child_two.path)-1)] = randrange(1, 17)
                print("MUTO HIJO 2")
        return child_one, child_two


    def __next_generation(self,child_one, child_two):
        # ordena la poblacion 
        self.population.sort(key=lambda x: x.fitness())

        # elimina los que tienen menor valor de ajuste
        del self.population[0]
        del self.population[1]

        # agrega los hijos a la poblacion
        self.population.append(child_one)
        self.population.append(child_two)

    def __is_solved(self):
        for ind in self.population:
            if ind.fitness() == 0:
                self.solution = ind
                return True
        return False
    
    def search_solution(self):
        for ind in self.population:
            if ind.fitness() == 0:
                return ind
        return None
 

    def __print_individuos(self, *individuos: Path):
        for ind in individuos:
            print(ind)


