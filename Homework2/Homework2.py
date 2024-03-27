from HillClimbing import HillClimbing as HC
from GeneticAlgorithm import GeneticAlgorithm as GA
from ParticleSwarmOptimization import ParticleSwarmOptimization as PSO
from DifferentialEvolution import DifferentialEvolution as DE

def runMethods(methods, willPrintBoard=False):
        for method in methods:
            print(method)
            print("\n")
            methods[method].run()
            if willPrintBoard:
                methods[method].printBoard()
                print("\n")
            with open('Output.txt', 'a') as file:
                file.write(f"{method}\n")
                file.write(f"{methods[method].get()}\n")

def main():
    hc = HC(8)
    ga = GA(n=8, populationSize=100, generations=100, mutationRate=0.2)
    pso = PSO(dimension=8, swarmSize=30, maxIter=100)
    de = DE(n=8, populationSize=100, iterations=1000, F=0.5, CR=0.7)

    methods = {"Hill Climb": hc, "Genetic Algorithm" : ga, "Particle Swarm Optimizer" : pso, "Differential Evolution" : de}
    runMethods(methods, True)
    # input("Finished with 8-Queens\n if you are ready to continue press [Enter]\n -->  ")
    hc = HC(32)
    ga = GA(n=32, populationSize=100, generations=100, mutationRate=0.2)
    # pso = PSO( dimension=32, swarmSize=64, maxIter=128, w0=0.9, w1=0.4, c1=2.0, c2=2.0)
    pso = PSO(dimension=32, swarmSize=64, maxIter=128, w0=0.9, w1=0.4, c1=2.3, c2=1.6)
    de = DE(n=32, populationSize=100, iterations=1000, F=0.5, CR=0.7)
    methods = {"Hill Climb": hc, "Genetic Algorithm": ga, "Particle Swarm Optimizer": pso, "Differential Evolution": de}
    runMethods(methods, True)

    #hc = HC(128)
    ga = GA(n=128, populationSize=100, generations=450, mutationRate=0.65)
    pso = PSO( dimension=128, swarmSize=30, maxIter=100)
    de = DE(n=128, populationSize=100, iterations=1000, F=0.5, CR=0.7)
    methods = {"Hill Climb": hc, "Genetic Algorithm": ga, "Particle Swarm Optimizer": pso, "Differential Evolution": de}
    runMethods(methods)

if __name__ == '__main__':
    main()