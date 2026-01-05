"""
Given two binary strings a and b, return their sum as a binary string.
Example 1:
Input: a = "11", b = "1"
Output: "100"
"""
#solution:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        while len(a)!=n:
            a = '0'+a
        while len(b)!=n:
            b = '0'+b
        carry = 0
        s = ''
        for i in range(n-1, -1, -1):
            l = int(a[i])
            m = int(b[i])
            t = l+m+carry
            carry = 0
            if t>=2:
                carry = 1
                t = t%2
            s = str(t)+s
            if i == 0:
                if carry > 0:
                    s = '1'+s
        return s



        