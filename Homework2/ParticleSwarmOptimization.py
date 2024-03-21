import numpy as np

class Particle:
    def __init__(self, dimension):
        self.position = np.random.permutation(dimension)
        self.best_position = np.copy(self.position)
        self.fitness = self.evaluate()
        self.best_fitness = self.fitness

    def evaluate(self):
        attacking_pairs = 0
        for i in range(len(self.position)):
            for j in range(i + 1, len(self.position)):
                if abs(self.position[i] - self.position[j]) == j - i:
                    attacking_pairs += 1
        return attacking_pairs

    def update_position(self):
        # Swap operation to simulate "velocity"
        idx1, idx2 = np.random.choice(len(self.position), 2, replace=False)
        self.position[idx1], self.position[idx2] = self.position[idx2], self.position[idx1]


class ParticleSwarmOptimization:
    def __init__(self, objective_function, dimension, swarm_size, max_iter):
        self.objective_function = objective_function
        self.dimension = dimension
        self.swarm = [Particle(dimension) for _ in range(swarm_size)]
        self.max_iter = max_iter
        self.g_best_position = None
        self.g_best_fitness = np.inf

        self.update_particles()

    def update_particles(self):
        for particle in self.swarm:
            particle.fitness = self.objective_function(particle.position)
            if particle.fitness < particle.best_fitness:
                particle.best_fitness = particle.fitness
                particle.best_position = np.copy(particle.position)
            if particle.fitness < self.g_best_fitness:
                self.g_best_fitness = particle.fitness
                self.g_best_position = np.copy(particle.position)

    def run(self):
        for _ in range(self.max_iter):
            self.update_particles()

    def printBoard(self, method=""):
        print(f"{method=}\n")
        n = len(self.g_best_position)
        for row in range(n):
            line = ""
            for col in range(n):
                if self.g_best_position[col] == row:
                    line += " Q "
                else:
                    line += " . "
            print(line)
        print("\n")