import random

class GeneticAlgorithm:
    def __init__(self, n, populationSize, generations, mutationRate):
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.populationSize = populationSize
        self.generations = generations
        self.mutationRate = mutationRate
        self.bestSolution = None
        self.bestFitness = float('-inf')
        self.population = self.generateInitialPopulation()

    def generateInitialPopulation(self):
        population = []
        for _ in range(self.populationSize):
            individual = random.sample(range(self.n), self.n)
            population.append(individual)
        return population

    def selectParent(self, pop):
        # tournament selection
        selection = random.sample(pop, self.populationSize)
        winner = max(selection, key=lambda individual: self.fitness(individual))
        return winner
        # Roulette Selection
        # fitnessTotal = sum(individual.fitness for individual in pop)
        # selection = random.unifrom(0, fitnessTotal)
        # curr = 0
        # for individual in pop:
        #     curr += individual.fitness
        #     if curr >= selection:
        #         return individual

    def crossover(self, parent1, parent2):
        lengthP1 = len(parent1)
        lengthP2 = len(parent2)
        if lengthP1 != lengthP2:
            raise ValueError("Parent chromosomes must have the same length")

        crossoverP1 = random.randint(1, lengthP1 - 2)
        crossoverP2 = random.randint(crossoverP1 + 1, lengthP2 - 1)

        offspring1 = parent1[:crossoverP1] + parent2[crossoverP1:crossoverP2] + parent1[crossoverP2:]
        offspring2 = parent2[:crossoverP1] + parent1[crossoverP1:crossoverP2] + parent2[crossoverP2:]
        return offspring1, offspring2

    def mutate(self, child, rate):
        for i in range(len(child)):
            if random.random() < rate:
                newPos = random.choice([x for x in range(len(child)) if x != child[i]])
                child[i] = newPos
        return child

    def fitness(self, node):
        attacks = 0
        for i in range(len(node)):
            for j in range(i + 1, len(node)):
                if node[i] == node[j] or abs(node[i] - node[j]) == j - i:
                    attacks += 1
        return -attacks

    def getBestSolution(self, pop):
        bestSolve = pop[0]
        bestFitness = self.fitness(bestSolve)
        for i in pop:
            currFitness = self.fitness(i)
            if currFitness > bestFitness:
                bestSolve = i
                bestFitness = currFitness
        return bestSolve, bestFitness

    def printBoard(self, method=""):
        def printing(p):
            for row in range(self.n):
                line = ""
                for col in range(self.n):
                    if col == p[row]:
                        line += " Q "
                    else:
                        line += " . "
                print(line)
            print("\n")
        solution = None
        if self.bestSolution:
            printing(self.bestSolution)
            print(f"{method=}\n")
        else:
            pass
            # board = 1
            # for individual in self.population:
            #     print(f"Individual: {board}")
            #     printing(individual)
            #     board += 1


    def geneticAlgorithm(self):

        for generation in range(self.generations):
            newPopulation = []
            for individual in range(self.populationSize // 2):
                parent1 = self.selectParent(self.population)
                parent2 = self.selectParent(self.population)
                children = self.crossover(parent1, parent2)
                for child in children:
                     newPopulation.append(self.mutate(child, self.mutationRate))
            population = newPopulation
        self.bestSolution, self.bestFitness = self.getBestSolution(self.population)
        return self.bestSolution


    def run(self):
        geneticAlgorithm = self.geneticAlgorithm()
        return geneticAlgorithm
