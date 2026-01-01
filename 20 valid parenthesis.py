"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""

#solution : 
class Solution:
    def push(self, stack, c):
        stack.insert(0, c)
        return stack
    def pop(self, stack):
        stack.pop(0)
        return stack
    def top(self, stack):
        if len(stack) == 0:
            return -1
        return stack[0]
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }
        for i in range(len(s)):
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                stack = self.push(stack, s[i])
            else:
                print(s[i])
                if hashmap[s[i]] == self.top(stack):
                    stack = self.pop(stack)
                else:
                    stack = self.push(stack, s[i])
        if len(stack) == 0:
            return True
        else:
            return False