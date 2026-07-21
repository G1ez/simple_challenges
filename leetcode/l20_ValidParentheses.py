"""
Problem: 20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

#solution
class Solution:
    def isValid(self, s: str) -> bool:
        pair = { #dictionary to store the pairs of brackets
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        for c in s: #iterate through each character in the string
            #print(c)          
            if c not in pair: #if the character is not a closing bracket, we add it to the stack
                stack.append(c)
            else:
                if not stack: #if the stack is empty, there is no matching opening bracket
                    return False
                last = stack.pop()
                if last != pair[c]: #if the last element in the stack is not the corresponding opening bracket
                    return False
        return len(stack) == 0 #check if the stack is empty, if it is, then all brackets are matched and closed properly