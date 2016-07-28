s = '2 4 10000000000000'

import bisect

a, b, t = map(int, s.strip().split())

output = 1
factor = int(a / 2 + b / 2)
currentdigit = factor

store = dict()
store[1] = factor
store[0] = 1
store[-1] = 1

ranking = [0, 1]


def power(i):
    if i not in store:
        store[i] = power(i // 2) * power(i - i // 2)
        print(i, power(i // 2), power(i - i // 2))
    return store[i]


def maxInStoreLessThan(i):
    index = bisect.bisect_left(ranking, i)
    print("index:", index)
    if index < len(ranking) and ranking[index] == i:
        return ranking[index]
    return ranking[index - 1]


def power_v2(i):
    print(i)
    if i not in store:
        currentmax = maxInStoreLessThan(i // 2)
        print('currentmax:', currentmax)
        print(store)
        print(store[currentmax] ** 2)
        store[currentmax * 2] = (store[currentmax] ** 2) % (10 ** 9 + 7)
        ranking.insert(bisect.bisect_left(ranking, currentmax * 2), currentmax * 2)
        store[i] = (store[currentmax * 2] * power_v2(i - currentmax * 2)) % (10 ** 9 + 7)
        ranking.insert(bisect.bisect_left(ranking, i), i)
    return store[i]


index = 0
lastindex = 0
binary = list(map(int, reversed(bin(t)[2:])))
# print(binary)
while index < len(binary):
    # print("output", output)
    pow_index = 2 ** index
    if binary[index]:
        if pow_index not in store:
            print("il", index, lastindex)
            store[pow_index] = (store[lastindex] * power_v2(pow_index - lastindex)) % (10 ** 9 + 7)
            ranking.insert(bisect.bisect_left(ranking, pow_index), pow_index)
        output *= store[pow_index]
        output = output % (10 ** 9 + 7)
        lastindex = pow_index
        index += 1
    else:
        while not binary[index]:
            index += 1

print(store)
print(len(store), len(binary))
print(output)
