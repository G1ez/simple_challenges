""" 
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

#solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shorter = len(min(strs, key=len))  #shorter string in array
        prefix = ""
        for i in range(shorter): #iterate through each character from shorter string
            letter = strs[0][i] #taking the first letter as reference
            for word in strs: #comparing the letter with each word in the array
                if word[i] != letter:
                    return prefix #when a letter is different we end
            prefix += letter
        return prefix #if all letters are the same we return the prefix

