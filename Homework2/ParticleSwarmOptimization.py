import numpy as np

class Particle:
    def __init__(self, dimension, posBounds=(-10, 10), velBounds=(-1, 1)):
        posLower, posUpper = posBounds
        velLower, velUpper = velBounds
        self.position = np.random.uniform(low=posLower, high=posUpper, size=dimension)
        self.velocity = np.random.uniform(low=velLower, high=velUpper, size=dimension)
        self.bestPosition = np.copy(self.position)
        self.bestFitness = np.inf
        self.fitness = np.inf

    def evaluateSolution(self, solution):
        n = self.dimension
        attacks = 0
        for i in range(n):
            for j in range(i + 1, n):
                if solution[i] == solution[j] or abs(solution[i] - solution[j]) == j - 1:
                    attacks += 1
        return attacks

class ParticleSwarmOptimization:
    def __init__(self, objectiveFunction, dimension, swarmSize, maxIter, w=0.5, c1=1.5, c2=1.5, posBounds=(-10, 10), velBounds=(-1, 1)):
        self.objectiveFunction = objectiveFunction
        self.dimension = dimension
        self.swarmSize = swarmSize
        self.maxIter = maxIter
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.posBounds = posBounds
        self.velBounds = velBounds

        self.swarm = [Particle(dimension, posBounds, velBounds) for _ in range(swarmSize)]
        self.gBestPosition = None
        self.gBestFitness = np.inf

        self.evaluateSwarm() # should initialize swarm

    def evaluateSwarm(self):
        for particle in self.swarm:
            particle.fitness = self.objectiveFunction(particle.position)
            if particle.fitness < particle.bestFitness:
                particle.bestFitness = particle.fitness
                particle.bestPosition = particle.position
            if particle.fitness < self.gBestFitness:
                self.gBestFitness = particle.fitness
                self.gBestPosition = particle.position
                self.gBestPosition = particle.position


    def updateParticles(self):
        for particle in self.swarm:
            r1, r2 = np.random.rand(self.dimension), np.random.rand(self.dimension)
            pbc = self.c1 * r1 * (particle.bestPosition - particle.position)
            gbc = self.c2 * r2 * (self.gBestPosition - particle.position)
            particle.velocity = self.w * particle.velocity + pbc + gbc
            particle.position += particle.velocity

    def updateGlobal(self):
        for particle in self.swarm:
            if particle.fitness < self.gBestFitness:
                self.gBestFitness = particle.fitness
                self.gBestPosition = np.copy(particle.position)

    def optimize(self):
        for _ in range(self.maxIter):
            self.evaluateSwarm()
            self.updateParticles()


    def particleSwarmOptimization(self):
        swarm = initSwarm()
        for particle in swarm:
            fitness = calcFitness()
            updateBestPosition(particle, fitness)
        updateBestPosition(Global, Globalfitness)
