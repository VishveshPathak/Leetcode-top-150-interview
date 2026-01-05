"""
Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
"""
#solution:
class Solution:
    def trailingZeroes(self, n: int) -> int:
        hashmap5 = {0:0}
        i = 1
        while i <= n:
            count5 = 0
            if i%5 == 0:
                x = i
                while x%5 == 0:
                    count5 = count5 + 1
                    x = x / 5
            hashmap5[i] = count5 + hashmap5[i-1]
            i = i+1
        return hashmap5[n]
        