"""
Given an array of strings strs, group the together. You can return the answer in any order.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
"""
#solution: works but output limit exceeded
class Solution:
    def checkAnagramSingle(self, s, t):
        hashmap = {}
        print(s, t)
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] = hashmap[s[i]]+1
            else:
                hashmap[s[i]] = 1
        for i in range(len(t)):
            if t[i] in hashmap:
                hashmap[t[i]] = hashmap[t[i]] -1
            else:
                return False
        for i in hashmap:
            if hashmap[i] != 0:
                return False
        return True
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap1 = {}
        added = False
        for i in strs:
            added = False
            for j in hashmap1:
                if self.checkAnagramSingle(hashmap1[j][0], i) == True:
                    hashmap1[j].append(i)
                    added = True
                    break
            if added == False:
                hashmap1[i] = []
                hashmap1[i].append(i)
        sol = []
        for i in hashmap1:
            sol.append(hashmap1[i])
        return sol        
    
#solution 2: reducing input size but still output limit
class Solution:
    def checkAnagramSingle(self, s, t):
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] = hashmap[s[i]]+1
            else:
                hashmap[s[i]] = 1
        for i in range(len(t)):
            if t[i] in hashmap:
                hashmap[t[i]] = hashmap[t[i]] -1
            else:
                return False
        for i in hashmap:
            if hashmap[i] != 0:
                return False
        return True
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i = 0
        j = 1
        sol = []
        solsingle = []
        while i<len(strs):
            j = 0
            solsingle = []
            x = strs[i]
            solsingle.append(strs[i])
            strs.remove(strs[i])
            while j < len(strs):
                if self.checkAnagramSingle(x,strs[j]) == True:
                    solsingle.append(strs[j])
                    strs.remove(strs[j])
                    j = j - 1
                j = j + 1
            sol.append(solsingle)
            i = -1
            i = i + 1
        print(sol)
        return sol
    
#solution: accepted
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            x = ''.join(sorted(i))
            if x in hashmap:
                hashmap[x].append(i)
            else:
                hashmap[x] = [i]
        sol = []
        for i in hashmap:
            sol.append(hashmap[i])
        return sol