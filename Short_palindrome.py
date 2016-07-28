import string

s = 'cacac'
total = 0


# forward: abba baab baab
# backward: abba

def nCr(n, r):
    if n < r or n == 0:
        return 0
    total = 1
    cnt = min(r, n - r)
    for _ in range(cnt):
        total *= n
        n -= 1

    # print('first:', total, n, r)
    for i in range(2, cnt + 1):
        total /= i
        # print(total, 'c', r)

    # print('second', total)

    return int(total)


# print(nCr(6,4))

alphaToNum = {letter: index for index, letter in enumerate(string.ascii_lowercase)}
# values denote (number of letters found, contribution since last letter)
# counter = {k:(None, set()) for k in string.ascii_lowercase}
Npairs = [0] * 26
# nested + 1: answer += Nletter (additive)


counter = dict()
for letter in s:
    # Add letter to pairing list
    for item in counter:
        print(counter[item])
        if item != letter:
            # print(letter, alphaToNum[letter], len(counter[item][0]), counter[item])
            counter[item][1][alphaToNum[letter]] += 1

    if letter in counter:
        total += sum(map(lambda x: nCr(x, 2), counter[letter][1])) * counter[letter][0]
        counter[letter][0] += 1
        counter[letter][1] = Npairs[:]
    else:
        counter[letter] = [1, Npairs[:]]

for item in counter.values():
    print(item)
    # if item[0] > 1:
    total += nCr(item[0], 4)
print(total)

counter = dict()
for letter in s[::-1]:
    # Add letter to pairing list
    print('called')
    for item in counter:
        print(counter[item])
        if item != letter:
            counter[item][1][alphaToNum[letter]] += 1

    if letter in counter:
        total += sum(map(lambda x: nCr(x, 2), counter[letter][1])) * (counter[letter][0] - 1)
        counter[letter][0] += 1
        counter[letter][1] = Npairs[:]
        # counter[letter] = (counter[letter][0]+1, counter[letter][1])
    else:
        counter[letter] = [1, Npairs[:]]

# if counter[letter][0]:
#        answer += counter[letter][1]*(number_of_palindromes_since_last_letter_found)
#        counter[letter] = (counter[letter][0]+1, set())
#    else:
#        counter[letter] = (1,0)

print(total % (10 ** 9 + 7))
