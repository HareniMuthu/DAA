import sys
sys.setrecursionlimit(10**6)  # Set recursion limit to a higher value

import time
import matplotlib.pyplot as plt

def iterative_sum(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

N_values = [10, 100, 1000, 10000]
iterative_times = []
recursive_times = []

for N in N_values:
    start_time = time.time()
    iterative_sum(N)
    iterative_times.append(time.time() - start_time)

    start_time = time.time()
    recursive_sum(N)
    recursive_times.append(time.time() - start_time)

plt.plot(N_values, iterative_times, label='Iterative')
plt.plot(N_values, recursive_times, label='Recursive')
plt.xlabel('N')
plt.ylabel('Time (s)')
plt.legend()
plt.show()
