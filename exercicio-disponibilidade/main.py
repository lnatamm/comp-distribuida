import matplotlib.pyplot as plt
import numpy as np
import math

from stochastic import StochasticSimulator

# Fórmula para calcular a disponibilidade de um sistema
def availability(n, k, p):
    total = 0
    for i in range(k, n+1):
        total += (p)**i * (1-p)**(n-i) * math.comb(n, i)
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

# 5. Availability vs p for n=100, k=1
n_fixed = 100
p_range = np.linspace(0, 1, 51)  # 51 pontos de 0 a 1
plt.figure(5)
plt.title("Availability vs p (n=100, k=1)")
plt.plot(p_range, [availability(n_fixed, 1, pv) for pv in p_range], marker='o', label='Analytical', color='orange')
plt.plot(p_range, [StochasticSimulator(n_fixed, 1, pv).availability() for pv in p_range], marker='x', alpha=.5, label='Stochastic', color='blue')
plt.xlabel('p')
plt.ylabel('Availability')
plt.legend()
plt.grid(True, alpha=0.3)

# 6. Availability vs p for n=100, k=n/2
plt.figure(6)
plt.title("Availability vs p (n=100, k=50)")
plt.plot(p_range, [availability(n_fixed, n_fixed//2, pv) for pv in p_range], marker='o', label='Analytical', color='orange')
plt.plot(p_range, [StochasticSimulator(n_fixed, n_fixed//2, pv).availability() for pv in p_range], marker='x', alpha=.5, label='Stochastic', color='blue')
plt.xlabel('p')
plt.ylabel('Availability')
plt.legend()
plt.grid(True, alpha=0.3)

# 7. Availability vs p for n=100, k=n
plt.figure(7)
plt.title("Availability vs p (n=100, k=100)")
plt.plot(p_range, [availability(n_fixed, n_fixed, pv) for pv in p_range], marker='o', label='Analytical', color='orange')
plt.plot(p_range, [StochasticSimulator(n_fixed, n_fixed, pv).availability() for pv in p_range], marker='x', alpha=.5, label='Stochastic', color='blue')
plt.xlabel('p')
plt.ylabel('Availability')
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()