"""
Reverse bits of a given 32 bits signed integer.
Example 1:
Input: n = 43261596
Output: 964176192
Explanation:
Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000
"""
#solution: 
class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        while len(s)!=32:
            s = '0'+s
        s = s[::-1]
        s = '0b'+s
        return int(s,2)
        
