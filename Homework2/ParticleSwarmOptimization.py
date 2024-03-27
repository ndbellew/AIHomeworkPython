import numpy as np
from random import uniform

class Particle:
    def __init__(self, dimension):
        self.position = np.random.permutation(dimension)
        self.best_position = np.copy(self.position)
        self.fitness = self.evaluate()
        self.best_fitness = self.fitness
        self.ultimatePosition = None

    def evaluate(self):
        attacking_pairs = 0
        for i in range(len(self.position)):
            for j in range(i + 1, len(self.position)):
                if abs(self.position[i] - self.position[j]) == j - i or self.position[i] == self.position[j]:
                    attacking_pairs += 1
        return attacking_pairs

    def update_position(self, best_global_position, c1=1.5, c2=1.5):
        randomSwap = uniform(0.001, 1.999) ## assuming i stay between 0-2 for c1 and c2.
        if randomSwap < c1:  # Influence of the particle's own best position
            idx1 = np.random.choice(len(self.position))
            idx2 = np.where(self.position == self.best_position[idx1])[0][0]
        elif randomSwap < c2:  # Influence of the global best position
            idx1 = np.random.choice(len(self.position))
            idx2 = np.where(self.position == best_global_position[idx1])[0][0]
        else:  # Random swap
            idx1, idx2 = np.random.choice(len(self.position), 2, replace=False)

        self.position[idx1], self.position[idx2] = self.position[idx2], self.position[idx1]


class ParticleSwarmOptimization:
    def __init__(self, dimension, swarmSize, maxIter, w0=0.9, w1=0.4, c1=2.0, c2=2.0):
        self.dimension = dimension
        self.swarm = [Particle(dimension) for _ in range(swarmSize)]
        self.maxIter = maxIter
        self.wPrime = w0
        self.wFinal = w1
        self.c1 = c1
        self.c2 = c2
        self.ultimatePosition = None
        self.ultimateFitness = np.inf

        self.update_particles()

    def updateInertia(self, iteration):
        # Dynamically adjusted
        self.wPrime = self.wFinal + (self.wPrime - self.wFinal) * (1 - iteration / self.maxIter)

    def update_particles(self):
        for particle in self.swarm:
            particle.fitness = particle.evaluate()
            if particle.fitness < particle.best_fitness:
                particle.best_fitness = particle.fitness
                particle.best_position = np.copy(particle.position)
            if particle.fitness < self.ultimateFitness:
                self.ultimateFitness = particle.fitness
                self.ultimatePosition = np.copy(particle.position)

    def particleSwarmOptimization(self):
        for _ in range(self.maxIter):
            for particle in self.swarm:
                particle.update_position(self.ultimatePosition)
                particle.fitness = particle.evaluate()
                if particle.fitness < particle.best_fitness:
                    particle.best_fitness = particle.fitness
                    particle.best_position = np.copy(particle.position)
                if particle.fitness < self.ultimateFitness:
                    self.ultimateFitness = particle.fitness
                    self.ultimatePosition = np.copy(particle.position)

    def run(self):
        self.particleSwarmOptimization()

    def get(self):
        if len(self.ultimatePosition) == 0 or self.ultimatePosition is None:
            return None
        else:
            return self.ultimatePosition

    def printBoard(self):
        n = len(self.ultimatePosition)
        for row in range(n):
            line = ""
            for col in range(n):
                if self.ultimatePosition[col] == row:
                    line += " Q "
                else:
                    line += " . "
            print(line)
        print("\n")

if __name__ == "__main__":
    testnum = 0
    for i in range(20):
        pso = ParticleSwarmOptimization(dimension=32, swarmSize=64, maxIter=128, w0=1.9, w1=0.4, c1=2.3, c2=1.7)
        pso.run()
        test = set(list(pso.ultimatePosition))
        testnum = pso.dimension - len(test)
        if testnum > 0:
            print(testnum)
            print(pso.ultimateFitness)
            print(pso.ultimatePosition)
            pso.printBoard()
    # No need to check vertical attacks since each queen is in a unique column
