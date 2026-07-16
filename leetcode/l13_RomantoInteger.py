"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

My First Solution:
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        romannumbers = { #fist i create a dictionary relating roman numbers and their values
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        res = 0
        for ind in range(len(s)): # checking each character
            #print(s[ind])
            if ind + 1 < len(s): #verifying if the next character exist
                if romannumbers[s[ind]] < romannumbers[s[ind+1]]: #checking if the next character is bigger than the current one
                    res -= romannumbers[s[ind]] #then we rest
                else: #if not we add
                    res += romannumbers[s[ind]]
            else:
                res += romannumbers[s[ind]] #last letter always gets added
        return res

"""
also i look for other solutions and found this one, that is actually faster than mine
"""
values = {'I':(1,-1),'V':[5],'X':(10,-10),'L':[50],'C':(100,-100),'D':[500],'M':[1000]} #save the values in a dictionary, but also save the negative value
class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        for index,k in enumerate(s): #enumerate gives me the index and the value of each character
            v = values[k]
            if len(v) == 1 or index == len(s)-1 : # if the length of the value is 1, or if its the last character, we add the value
                sum +=v[0]
            else:
                #determine if the next character is bigger than the current one, if it is we add the negative value, if not we add the positive value
                if (k == 'I' and (s[index+1] == 'V' or s[index+1] == 'X')) or  (k == 'X' and (s[index+1] == 'L' or s[index+1] == 'C')) or   (k == 'C' and (s[index+1] == 'D' or s[index+1] == 'M') ):
                    sum +=v[1]
                else:
                    sum +=v[0]
        return sum
