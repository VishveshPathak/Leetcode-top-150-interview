"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
"""
#solution:
class Solution:
    def countPositive(self, nums, p):
        count = 0
        for i in nums:
            if i >= p:
                count = count + 1
        if count>=p:
            return True
        else:
            return False
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        j = n
        while j>0:
            if self.countPositive(citations, j) == True:
                return j
            j = j -1
        return 0
    