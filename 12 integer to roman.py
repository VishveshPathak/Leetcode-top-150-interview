"""Seven different symbols represent Roman numerals with the following values:
Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

    If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
    If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
    Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.

Given an integer, convert it to a Roman numeral."""

#solution:

class Solution:
    def getThousandDigit(self, n):
        if n == 1:
            return 'M'
        elif n == 2:
            return 'MM'
        elif n == 3:
            return 'MMM'
        else:
            return ''

    def getHundredDigit(self, n):
        if n == 9:
            return 'CM'
        elif n == 8:
            return 'DCCC'
        elif n == 7:
            return 'DCC'
        elif n == 6:
            return 'DC'
        elif n == 5:
            return 'D'
        elif n == 4:
            return 'CD'
        elif n == 3:
            return 'CCC'
        elif n == 2:
            return 'CC'
        elif n == 1:
            return 'C'
        else:
            return ''

    def getTenDigit(self, n):
        if n == 9:
            return 'XC'
        elif n == 8:
            return 'LXXX'
        elif n == 7:
            return 'LXX'
        elif n == 6:
            return 'LX'
        elif n == 5:
            return 'L'
        elif n == 4:
            return 'XL'
        elif n == 3:
            return 'XXX'
        elif n == 2:
            return 'XX'
        elif n == 1:
            return 'X'
        else:
            return ''

    def getLastDigit(self, n):
        if n == 9:
            return 'IX'
        elif n == 8:
            return 'VIII'
        elif n == 7:
            return 'VII'
        elif n == 6:
            return 'VI'
        elif n == 5:
            return 'V'
        elif n == 4:
            return 'IV'
        elif n == 3:
            return 'III'
        elif n == 2:
            return 'II'
        elif n == 1:
            return 'I'
        else:
            return ''
    def intToRoman(self, num: int) -> str:
        numstring = str(num)
        answer = ''
        if len(numstring) == 4:
            answer = answer + self.getThousandDigit(int(numstring[0]))
            answer = answer + self.getHundredDigit(int(numstring[1]))
            answer = answer + self.getTenDigit(int(numstring[2]))
            answer = answer + self.getLastDigit(int(numstring[3]))
        elif len(numstring) == 3:
            answer = answer + self.getHundredDigit(int(numstring[0]))
            answer = answer + self.getTenDigit(int(numstring[1]))
            answer = answer + self.getLastDigit(int(numstring[2]))
        elif len(numstring) == 2:
            answer = answer + self.getTenDigit(int(numstring[0]))
            answer = answer + self.getLastDigit(int(numstring[1]))
        else:
            return self.getLastDigit(int(numstring[0]))
        return answer