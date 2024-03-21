from HillClimbing import HillClimbing as HC
from GeneticAlgorithm import GeneticAlgorithm as GA
from ParticleSwarmOptimization import ParticleSwarmOptimization as PSO
from DifferentialEvolution import DifferentialEvolution as DE

def ObjectiveFunction(position):
    attackingPairs = 0
    for i in range(len(position)):
        for j in range(i + 1, len(position)):
            if abs(position[i]-position[j]) == j - i:
                attackingPairs += 1
    return attackingPairs

def main():
    hc = HC(8)
    ga = GA(n=8, populationSize=100, generations=100, mutationRate=0.2)
    pso = PSO(objective_function=ObjectiveFunction, dimension=8, swarm_size=30, max_iter=100)
    de = DE(n=8, populationSize=100, iterations=1000, F=0.5, CR=0.7)

    methods = {"Hill Climb": hc, "Genetic Algorithm" : ga, "Particle Swarm Optimizer" : pso}# , de]
    for method in methods:
        methods[method].printBoard(method)
        print("\n")
        methods[method].run()
        methods[method].printBoard(method)
        print("\n")


if __name__ == '__main__':
    main()