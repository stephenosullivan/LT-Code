__author__ = 'stephenosullivan'

memo = dict()


def string_compare(pattern, text, i, j):
    if (i, j) not in memo:
        opt = [None] * 3

        if i == 0:
            memo[(i, j)] = j
            return j

        if j == 0:
            memo[(i, j)] = i
            return i

        opt[0] = string_compare(pattern, text, i - 1, j - 1) + 1 - int(pattern[i - 1] == text[j - 1])
        opt[1] = string_compare(pattern, text, i, j - 1) + 1
        opt[2] = string_compare(pattern, text, i - 1, j) + 1
        # print(opt)
        memo[(i, j)] = min(opt)

    return memo[(i, j)]


if __name__ == '__main__':
    # pattern = "sentence"
    # text = "This is a sentence"
    # for i in range(0, len(text)-len(pattern)+1):
    #     memo = dict()
    #     print(string_compare(pattern, text[i:len(pattern)+i], len(pattern)-1, len(pattern)-1))

    memo = dict()
    pattern = "you should not"
    text = "thou shalt not"
    print(string_compare(pattern, text, len(pattern), len(text)))
    for j in range(len(pattern)):
        print([memo[(i, j)] for i in range(len(text))])
