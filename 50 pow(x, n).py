"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000
"""
#solution: terrible corner case management, do at a later date
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = n*-1
        if n == 0:
            return 1
        if n == 1:
            return x
        if x == 1:
            return 1
        if x == -1:
            if n%2 == 0:
                return x*x
            else:
                return x

        i = 2
        answer = x*x
        while i < n:
            if answer == 0:
                return 0
            if i<math.floor(n/2):
                answer = answer*answer
                i = i*2
            else:
                answer = answer*x
                i = i+1
        return answer
        