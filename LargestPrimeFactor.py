# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import math

n = input('Input number:')

nroot = round(math.sqrt(int(n)))
a = [0] * nroot
for i in range(nroot):
    a[i] = i

# Search for prime numbers by the sieve of Eratosthenes

a[1] = 0
m = 2
while m < nroot:
    if a[m] != 0:
        j = m ** 2
        while j < nroot:
            a[j] = 0
            j += m
    m += 1

# Filling the list with primes

b = []
for i in a:
    if a[i] != 0:
        b.append(a[i])
b.reverse()

# Search for the largest prime divisor of n

for i in range(0,len(b)):
    if (int(n) % b[i]) == 0:
        print(b[i])
        break
