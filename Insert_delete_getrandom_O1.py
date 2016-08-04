import random


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = dict()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.store.keys():
            index = len(self.store)
            self.store[val] = index
            return True
        return False

    def remove(self, val):
        """
        Deletes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.store.keys():
            self.store.pop(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.store.keys())

        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.delete(val)
        # param_3 = obj.getRandom()param_3 = obj.getRandom()
