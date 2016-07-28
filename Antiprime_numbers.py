import bisect
import heapq

numQueries = 1

queries = [2000000]
test = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160,
        25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280,
        720720, 1081080, 1441440, 2162160]
maxquery = max(queries)
antiprimes = [1]
maxprimelen = 1


def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = [False] * ((n // 6 - k * k // 6 - 1) // k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = [False] * (
            (n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]


primes = primes2(10 ** 7)
priority = []
heapq.heappush(priority, (2, [1], 2))

visited = set()
visited.add(1)


def newfactors(factor):
    value, primecombo, product = factor
    if value * 2 not in visited:
        copycombo = primecombo[:]
        factorproduct = product * ((copycombo[0] + 2) / (copycombo[0] + 1))
        copycombo[0] += 1
        heapq.heappush(priority, (value * 2, copycombo, factorproduct))
        visited.add(value * 2)
    for i in range(len(primecombo) - 1):
        if primecombo[i] > primecombo[i + 1] and value * primes[i + 1] not in visited:
            copycombo = primecombo[:]
            factorproduct = product * ((copycombo[i + 1] + 2) / (copycombo[i + 1] + 1))
            copycombo[i + 1] += 1
            heapq.heappush(priority, (value * primes[i + 1], copycombo, factorproduct))
            visited.add(value * primes[i + 1])
    j = len(primecombo)
    if value * primes[j] not in visited:
        copycombo = primecombo[:] + [0]
        factorproduct = product * 2
        copycombo[j] += 1
        heapq.heappush(priority, (value * primes[j], copycombo, factorproduct))
        visited.add(value * primes[j])


while antiprimes[-1] < maxquery:
    value, factors, product = heapq.heappop(priority)
    print(value, factors, product)
    if product > maxprimelen:
        antiprimes.append(value)
        maxprimelen = product
    newfactors((value, factors, product))

print(antiprimes)
# print(primes[:10])
print(antiprimes == test)

for q in queries:
    index = bisect.bisect_left(antiprimes, q)
    print(antiprimes[index])
