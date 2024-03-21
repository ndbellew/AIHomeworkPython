import numpy as np
import random


class DifferentialEvolution:
    def __init__(self, n, populationSize, iterations, F, CR):
        self.n = n
        self.populationSize = populationSize
        self.iterations = iterations
        self.F = F
        self.CR = CR
        self.population = self.initPopulation()

    def initPopulation(self):
        population = []
        for _ in range(self.populationSize):
            individual = np.random.permutation(self.n)
            population.append(individual)
        return population

    def selectThreeRandomVectors(self, index):
        indices = list(range(self.populationSize))
        indices.remove(index)
        selectedIndices = random.sample(indices, 3)  # selecting three random vectors
        A, B, C = [self.population[i] for i in selectedIndices]
        return A, B, C

    def mutate(self, A, B, C, F):
        V = [0] * self.n
        for i in range(self.n):
            diff = (B[i] - C[i]) % self.n
            V[i] = (A[i] + int(F * diff)) % self.n
        return V

    def crossover(self, target, mutant):
        trial = [0] * self.n
        randIndex = random.randint(0, self.n - 1)
        for i in range(self.n):
            if random.random() < self.CR or i == randIndex:
                trial[i] = mutant[i]
            else:
                trial[i] = target[i]
        return trial


    def evaluate(self, individual):
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                # Check if queens are in the same row or on the same diagonal
                if individual[i] == individual[j] or abs(individual[i] - individual[j]) == abs(i - j):
                    conflicts += 1
        return conflicts


    def solutionFound(self):
        # Check if any individual in the population is a solution (0 conflicts)
        return any(self.evaluate(individual) == 0 for individual in self.population)


    def bestSolution(self):
        # Return the individual with the lowest number of conflicts
        return min(self.population, key=self.evaluate)


    def printBoard(self, Method=""):
        solution = self.bestSolution()
        if not solution:
            print("No solution found.")
        else:
            for row in range(self.n):
                for col in range(self.n):
                    if solution[col] == row:
                        print(' Q ')
                    else:
                        print(' . ')
                print()

    def run(self):
        self.differentialEvolution()

    def differentialEvolution(self):
        for generation in range(self.iterations):
            for individual in range(self.populationSize):
                target = self.population[individual]
                a, b, c = self.selectThreeRandomVectors(individual)
                mutant = self.mutate(a, b, c, self.F)
                trial = self.crossover(target, mutant)
                if self.evaluate(trial) < self.evaluate(target):
                    self.population[individual] = trial
                if self.solutionFound():
                    break
        return self.bestSolution()
