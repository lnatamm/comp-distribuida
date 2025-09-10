import matplotlib.pyplot as plt
import numpy as np
import math

from stochastic import StochasticSimulator

# Fórmula para calcular a disponibilidade de um sistema
def availability(n, k, p):
    total = 0
    for i in range(k, n+1):
        total += (1-p)**i * p**(n-i) * math.comb(n, i)
    print("Availability for k =", k, "is", total)
    return total

n = 100
k = np.arange(1, n + 1)
p = 0.5

# 1. Availability vs k e Stochastic Simulation vs k
plt.figure(1)
plt.title("Availability vs k")
plt.plot(k, [availability(n, ki, p) for ki in k], marker='o', label='Analytical', color='orange')
plt.plot(k, [StochasticSimulator(n, ki, p).availability() for ki in k], marker='x', alpha=.5, label='Stochastic', color='blue')
plt.xlabel('k')
plt.ylabel('Availability')
plt.legend()

# 2. Availability For K = 1 vs n e Stochastic Simulation For K = 1 vs n
# Nesses exemplos vamos aumentando n de 1 a 100
n_range = np.arange(1, n + 1)
plt.figure(2)
plt.title("Availability For K = 1 vs n")
plt.plot(n_range, [availability(nv, 1, p) for nv in n_range], marker='o', label='Analytical', color='orange')
plt.plot(n_range, [StochasticSimulator(nv, 1, p).availability() for nv in n_range], marker='x', alpha=.5, label='Stochastic', color='blue')
plt.xlabel('n')
plt.ylabel('Availability')
plt.legend()

# 3. Availability For K = n/2 vs n e Stochastic Simulation For K = n/2 vs n
plt.figure(3)
plt.title("Availability For K = n/2 vs n")
plt.plot(n_range, [availability(nv, nv//2, p) for nv in n_range], marker='o', label='Analytical', color='orange')
plt.plot(n_range, [StochasticSimulator(nv, nv//2, p).availability() for nv in n_range], marker='x', alpha=.5, label='Stochastic', color='blue')
plt.xlabel('n')
plt.ylabel('Availability')
plt.legend()

# 4. Availability For K = n vs n e Stochastic Simulation For K = n vs n
plt.figure(4)
plt.title("Availability For K = n vs n")
plt.plot(n_range, [availability(nv, nv, p) for nv in n_range], marker='o', label='Analytical', color='orange')
plt.plot(n_range, [StochasticSimulator(nv, nv, p).availability() for nv in n_range], marker='x', alpha=.5, label='Stochastic', color='blue')
plt.xlabel('n')
plt.ylabel('Availability')
plt.legend()

plt.show()