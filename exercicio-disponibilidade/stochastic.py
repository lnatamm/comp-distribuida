import numpy as np
class StochasticSimulator:
    def __init__(self, n, k, p, rounds=500):
        self.n = n
        self.k = k
        self.p = p
        self.rounds = rounds

    def availability(self):
        results = []
        for _ in range(self.rounds):
            working = 0
            for _ in range(self.n):
                if np.random.rand() < self.p:
                    working += 1
            results.append(1 if working >= self.k else 0)
        return sum(results) / self.rounds