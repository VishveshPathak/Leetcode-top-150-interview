"""
Implement the RandomizedSet class:
    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]
"""

#solution: very weird problem. apparently wants to create a new array of size one and then based on random sets of insert delete expects some result
import random
class RandomizedSet:
    def __init__(self):
        self.array = [math.pow(2,31)]

    def insert(self, val: int) -> bool:
        if val in self.array:
            return False
        else:
            self.array.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.array:
            self.array.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        if len(self.array) > 2:
            r = random.randint(1, len(self.array)-1)
            return self.array[r]
        else:
            return self.array[1]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()