from HillClimbing import HillClimbing as HC
from GeneticAlgorithm import GeneticAlgorithm as GA
from ParticleSwarmOptimization import ParticleSwarmOptimization as PSO
from DifferentialEvolution import DifferentialEvolution as DE

def runMethods(methods):
    for method in methods:
        print(method)
        print("\n")
        methods[method].run()
        methods[method].printBoard()
        print("\n")

def main():
    hc = HC(8)
    ga = GA(n=8, populationSize=100, generations=100, mutationRate=0.2)
    pso = PSO(dimension=8, swarmSize=30, maxIter=100)
    de = DE(n=8, populationSize=100, iterations=1000, F=0.5, CR=0.7)

    methods = {"Hill Climb": hc, "Genetic Algorithm" : ga, "Particle Swarm Optimizer" : pso, "Differential Evolution" : de}
    runMethods(methods)
    input("Finisehd with 8-Queens\n if you are ready to continue press [Enter]\n -->  ")
    hc = HC(32)
    ga = GA(n=32, populationSize=100, generations=100, mutationRate=0.2)
    pso = PSO( dimension=32, swarmSize=64, maxIter=128)
    de = DE(n=32, populationSize=100, iterations=1000, F=0.5, CR=0.7)
    methods = {"Hill Climb": hc, "Genetic Algorithm": ga, "Particle Swarm Optimizer": pso, "Differential Evolution": de}
    runMethods(methods)

    # hc = HC(4096)
    # ga = GA(n=4096, populationSize=100, generations=100, mutationRate=0.2)
    # pso = PSO( dimension=4096, swarmSize=30, maxIter=100)
    # de = DE(n=4096, populationSize=100, iterations=1000, F=0.5, CR=0.7)
    # methods = {"Hill Climb": hc, "Genetic Algorithm": ga, "Particle Swarm Optimizer": pso, "Differential Evolution": de}
    # runMethods(methods)

if __name__ == '__main__':
    main()