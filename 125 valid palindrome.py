"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

#solution: primitive
class Solution:
    def checkallowed(self, c):
        allowed = '0123456789abcdefghijklmnopqrstuvwxyz'
        for i in range(len(allowed)):
            if c == allowed[i]:
                return True
        return False
    def isPalindrome(self, s: str) -> bool:
        sclean = ''
        s=s.lower()
        for i in range(len(s)):
            if self.checkallowed(s[i]) == True:
                sclean = sclean+s[i]
        if sclean == sclean[::-1]:
            return True
        else:
            return False

            
#solution 2: conceptually faster but slower in actual execution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        while i<len(s):
            x = ord(s[i])
            if not ((x>=48 and x<=57) or (x>=65 and x<=90) or (x>=97 and x<=122)):
                s = s[:i] + s[i+1:]
                i = i - 1
            else:
                if x>=65 and x<=90:
                    x = x-65+97
                    s = s[:i]+chr(x)+s[i+1:]
                    i = i-1
            i = i+1

        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left = left + 1
            right = right - 1
        return True
            
            
#solution 3: in C to avoid calling ord function.
bool isPalindrome(char* s) {
    int x = 0;
    char c;
    int i = 0;
    int n =strlen(s);
    while (i<n) {
        c = s[i];
        x = c;
        if ((x>=48 && x<=57) || (x>=65 && x<=90) || (x>=97 && x<=122))
        {
            if (x>=65 && x<=90){
                x = x-65+97;
                c = x;
                s[i] = c; 
            }
        }
        else{
            s[i] = ' ';
        }
        i++;
    }
    int left = 0;
    int right = n-1;
    while(left<right) {
        if (s[left]!=s[right]) {
            if (s[left] != ' ' && s[right] != ' '){
                return false;
            }
            if (s[left] == ' ') {
                left = left + 1;
            }
            if (s[right] == ' ') {
                right = right - 1;
            }
        }
        else {
            left = left + 1;
            right = right - 1;
        }
    }
    return true;   
}