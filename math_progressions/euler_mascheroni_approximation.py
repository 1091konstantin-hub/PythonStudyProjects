# Approximate Euler-Mascheroni constant using harmonic series
from math import log

n = int(input())
harmonic_sum = 0

for i in range(1, n + 1):
    harmonic_sum += 1 / i
    result = harmonic_sum - log(n)

print(result)
