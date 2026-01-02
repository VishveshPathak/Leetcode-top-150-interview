"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.
"""

#solution: 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap2 = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in hashmap:
                if t[i] not in hashmap[s[i]]:
                    hashmap[s[i]].append(t[i])
            else:
                hashmap[s[i]] = []
                hashmap[s[i]].append(t[i])
            if t[i] in hashmap2:
                if s[i] not in hashmap2[t[i]]:
                    hashmap2[t[i]].append(s[i])
            else:
                hashmap2[t[i]] = []
                hashmap2[t[i]].append(s[i])
        for i in range(len(s)):
            if len(hashmap[s[i]]) > 1:
                return False
        for i in range(len(t)):
            if len(hashmap2[t[i]]) > 1:
                return False
        return True