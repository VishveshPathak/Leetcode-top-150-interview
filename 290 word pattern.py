"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.
Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:
    'a' maps to "dog".
    'b' maps to "cat".
"""
#solution:.
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        counter = 0
        word = ''
        list1 = []
        list2 = []
        for i in range(len(s)):
            if s[i] == ' ' or i == len(s)-1:
                if i == len(s)-1:
                    word = word + s[len(s)-1] 
                if word != '':
                    if word not in hashmap1:
                        hashmap1[word] = counter
                        counter = counter + 1
                    list1.append(hashmap1[word])
                    word = ''
            else:
                word = word + s[i]
        counter = 0
        for i in range(len(pattern)):
            if pattern[i] not in hashmap2:
                hashmap2[pattern[i]] = counter
                counter = counter + 1
            list2.append(hashmap2[pattern[i]])
        print(list1)
        print(list2)
        if len(list1) != len(list2):
            return False
        else:
            for i in range(len(list1)):
                if list1[i] != list2[i]:
                    return False
            return True