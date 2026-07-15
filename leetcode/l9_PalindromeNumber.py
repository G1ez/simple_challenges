"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0: #verifying the number is positive
            invr = int(str(x)[::-1]) #reversing that number
            return invr == x #checking and returning if theyre equal
        else:
            return False #false if is negative