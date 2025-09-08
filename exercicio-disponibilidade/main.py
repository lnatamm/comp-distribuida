import matplotlib.pyplot as plt
import numpy as np
import math

from stochastic import StochasticSimulator

# Fórmula para calcular a disponibilidade de um sistema
def availability(n, k, p):
    sum = 0
    for i in range(k, n+1):
        sum += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    print("Availability for k =", k, "is", sum)
    return sum

n = 100
k = np.arange(1, n + 1)
p = 0.5

plt.figure(1)
plt.title("Availability vs k")
plt.plot(k, [availability(n, ki, p) for ki in k], marker='o')
plt.figure(2)
plt.title("Stochastic Simulation vs k")
plt.plot(k, [StochasticSimulator(n, ki, p).availability() for ki in k], marker='o')


plt.show()