from collections import defaultdict
class Solution:
    def romanToInt(self, s: str) -> int:
        a = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum = 0
        i = len(s) - 1
        while i >= 0:
            if i > 0 and s[i] == "V" and s[i-1] == "I":
                sum += 4
                i -= 2
            elif i > 0 and s[i] == "X" and s[i-1] == "I":
                sum += 9
                i -= 2
            elif i > 0 and s[i] == "L" and s[i-1] == "X":
                sum += 40
                i -= 2
            elif i > 0 and s[i] == "C" and s[i-1] == "X":
                sum += 90
                i -= 2
            elif i > 0 and s[i] == "D" and s[i-1] == "C":
                sum += 400
                i -= 2
            elif i > 0 and s[i] == "M" and s[i-1] == "C":
                sum += 900
                i -= 2
            else:
                sum += a[s[i]]
                i -= 1
        return sum