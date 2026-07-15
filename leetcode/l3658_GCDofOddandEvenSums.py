"""
You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:

sumOdd: the sum of the smallest n positive odd numbers.

sumEven: the sum of the smallest n positive even numbers.

Return the GCD of sumOdd and sumEven.
"""

#answer
import math #just to use gcd function
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = n ** 2 # in explanation we found "sumOdd = 1 + 3 + 5 + 7 = 16" so we can use that formula
        sumEven = (n*n)+n #another formula for even numbers
        result = math.gcd(sumOdd, sumEven) #getting gcd of both sums
        return result # :)