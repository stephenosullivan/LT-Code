__author__ = 'stephenosullivan'

memo = dict()
d = dict()


def partition(seq, j, k):
    if (j, k) not in memo:
        if k == 1 or j <= 1:
            memo[(j, k)] = sum(seq[:j])
            d[(j, k)] = j
        else:
            print(seq, j, k)
            print([(partition(seq, i, k - 1), sum(seq[i:])) for i in range(0, j)])
            memo[(j, k)], d[(j, k)] = min([(max(partition(seq, i, k - 1), sum(seq[i:j])), i) for i in range(0, j)])
    return memo[(j, k)]


def getPartitions(j, k):
    if k > 1:
        tmp = d[(j, k)]
        getPartitions(tmp, k - 1)
        print(tmp)


if __name__ == '__main__':
    seq = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    print(partition(seq, len(seq), 5))
    getPartitions(len(seq), 5)
