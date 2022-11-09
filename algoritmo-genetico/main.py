from path import Path
from algorithm import PathAlgorithm
if __name__ == "__main__":
    #paths = [Path.generate() for _ in range(8)]
    paths = []
    paths.append(Path([0, 9, 3, 8, 9, 10, 11, 16, 17]))
    # paths.append(Path([0,4, 9, 14, 15, 16, 17]))

    algo = PathAlgorithm()
    algo.solve()

    for p in paths:
        print(p)

