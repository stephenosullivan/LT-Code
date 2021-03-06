__author__ = 'stephenosullivan'

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        return self.combineRecursive(k, range(1, n + 1))

    def combineRecursive(self, k, numbers):
        if k == 1:
            return [[x] for x in numbers]
        else:
            return [row + [x] for row in self.combineRecursive(k - 1, numbers) for x in numbers if x > row[-1]]

    def combineIterative(self, n, k):
        output = []
        if k > 0:
            for n_index in range(1, n - k + 2):
                output.append([n_index])

            for k_index in range(k-1):
                new_output = []
                for comb in output:
                    for n_index in range(2 + k_index, n - k + k_index + 3):
                        if n_index > comb[-1]:
                            new_output.append(comb + [n_index])
                output = new_output[:]

        return output

if __name__ == '__main__':
    sol = Solution()
    print(sol.combine(3, 3))
