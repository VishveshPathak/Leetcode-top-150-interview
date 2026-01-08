"""
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
Example 1:
Input: left = 5, right = 7
Output: 4
"""
#solution
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        l = bin(left)[2:]
        r = bin(right)[2:]
        n = len(l)
        for i in range(n-1, -1, -1):
            if l == r:
                while len(l)!=n:
                    l = l+'0'
                return int('0b'+l,2)
            l = l[:-1]
            r = r[:-1]
        return 0