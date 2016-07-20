class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.store = [0] + [-1] * (amount)
        # coins.sort()

        for current in range(1, amount + 1):
            for i, coin in enumerate(coins):
                tmp_current = float("inf")
                if current - coin >= 0:
                    if self.store[current - coin] != -1:
                        tmp_current = min(tmp_current, 1 + self.store[current - coin])
            if tmp_current != float("inf"):
                self.store[current] = tmp_current

        # if self.store[amount] == float("inf"):
        #     return -1
        # return self.store[amount]
        return self.store[amount]

    def coinChangeDP_v1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        self.amount = amount
        self.store = {0: 0}
        self.current = 1
        self.coins = coins

        self.helper()
        if amount in self.store:
            return self.store[amount]
        return -1

    def helper(self):
        for self.current in range(1, self.amount + 1):
            val_list = [self.store[self.current - coin] for coin in self.coins if (self.current - coin) in self.store]
            if val_list:
                self.store[self.current] = 1 + min(val_list)

    def coinChange_recursive(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        else:
            x1 = [self.coinChange_recursive(coins, amount - coin) for coin in coins]
            x = [val for val in x1 if val >= 0]
            if len(x) > 0:
                return 1 + min(x)
            else:
                return -1
