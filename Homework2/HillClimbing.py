from random import randint
import time

class HillClimbing:
    def __init__(self, numberOfQueens):
        self.n = numberOfQueens
        self.board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.state = [randint(0, self.n-1) for _ in range(self.n)]
        self.bestState = None
        self.updateBoard()

    def updateBoard(self):
        for i in range(self.n):
            for j in range(self.n):
                self.board[j][i] = 0
            self.board[self.state[i]][i] = 1

    def numOfAttacks(self):
        attacks = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                # Checking for horizontal attacks
                if self.state[i] == self.state[j]:
                    attacks += 1
                # Checking for diagonal attacks
                if abs(i - j) == abs(self.state[i] - self.state[j]):
                    attacks += 1
        # No need to check vertical attacks since each queen is in a unique column
        return attacks

    def getNeighbors(self):
        bestState = self.state.copy()
        minAttacks = self.numOfAttacks()
        for col in range(self.n):
            originalRow = self.state[col]
            for row in range(self.n):
                if self.state[col] == row:
                    continue
                self.state[col] = row
                currentAttacks = self.numOfAttacks()
                if currentAttacks < minAttacks:
                    minAttacks = currentAttacks
                    bestState = self.state[:]
                self.state[col] = originalRow  # Revert state
        self.state = bestState
        self.updateBoard()

    def get(self):
        solution = self.state
        if self.numOfAttacks() > 0:
            return None
        else:
            return solution

    def printBoard(self, method=""):
        if method:
            print(f"{method=}\n")
        for state in self.board:
            line = ""
            for val in state:
                if val == 1:
                    line += " Q "
                else:
                    line += " . "
            print(line)
        print("\n")

    def hillClimbing(self):
        currentAttacks = self.numOfAttacks()
        while True:
            self.getNeighbors()
            if currentAttacks <= self.numOfAttacks():
                break
            currentAttacks = self.numOfAttacks()
        return self.state

    def get(self):
        return self.bestState

    def run(self, max_restarts=100):
        start_time = time.time()
        num_restarts = 0
        while num_restarts < max_restarts:
            self.state = [randint(0, self.n-1) for _ in range(self.n)]
            self.updateBoard()
            self.bestState = self.hillClimbing()
            if not self.numOfAttacks():  # Check if all queens are in safe positions
                print(f"Restart #{num_restarts + 1} - Solution found")
                print(f"Restart #{num_restarts + 1} - Solution state: {self.bestState}")
                print(f"Restart #{num_restarts + 1} - Time taken: {time.time() - start_time:.4f} seconds")
                return self.bestState
            num_restarts += 1
        self.printBoard(f"Restart #{num_restarts + 1} - No solution found")
        print(f"Restart #{num_restarts + 1} - Time taken: {time.time() - start_time:.4f} seconds")
        return None

    def isEmpty(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    return False
        return True