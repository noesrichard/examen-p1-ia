from path import Path
from algorithm import PathAlgorithm
if __name__ == "__main__":

    path = Path([ 0, 4, 5, 6, 11, 12, 11, 10, 10, 10, 9, 4, 9, 10, 11, 16, 17])
    path.clean()
    print(path)
    algo = PathAlgorithm()
    algo.solve()

