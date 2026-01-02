"""
Given an integer x, return true if x is a, and false otherwise.
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""
#solution:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x = str(x)
        left = 0
        right = len(x)-1
        while left < right:
            if x[left] != x[right]:
                return False
            left = left + 1
            right = right - 1
        return True