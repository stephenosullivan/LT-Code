__author__ = 'stephenosullivan'

memo = dict()


def binomial_coef(n, k):
    if n == k or k == 0:
        return 1
    else:
        return binomial_coef(n - 1, k - 1) + binomial_coef(n - 1, k)


def binomial_coef_faster(n, k):
    if n == k or k == 0:
        return 1
    elif (n, k) not in memo.keys():
        memo[(n, k)] = binomial_coef_faster(n - 1, k - 1) + binomial_coef_faster(n - 1, k)
    return memo[(n, k)]


def binomial_coef_faster_symm(n, k):
    if k > n // 2:
        k = n - k
    if k == 0:
        return 1
    elif (n, k) not in memo.keys():
        memo[(n, k)] = binomial_coef_faster_symm(n - 1, k - 1) + binomial_coef_faster_symm(n - 1, k)
    return memo[(n, k)]


if __name__ == '__main__':
    N = 9
    print([binomial_coef(9, i) for i in range(10)])
    print([binomial_coef_faster(9, i) for i in range(10)])
    print([binomial_coef_faster_symm(9, i) for i in range(10)])
