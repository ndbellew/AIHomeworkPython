from HillClimbing import HillClimbing as HC
from GeneticAlgorithm import GeneticAlgorithm as GA

def main():
    hc = HC(8)
    ga = GA(n=8, populationSize=100, generations=100, mutationRate=0.2)
    methods = [hc, ga]#, pso, de]
    for method in methods:
        method.printBoard()
        print("\n")
        method.run()
        method.printBoard()
        print("\n")


if __name__ == '__main__':
    main()