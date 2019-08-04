"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1:
            return s

        strings = [s[0]]

        pal_list = {}
        
        for char in s[1:]:
            for index, string in enumerate(strings):
                string += char
                strings[index] = string
            strings.append(char)
            
            for contender in strings:
                if contender == contender[::-1]:
                    pal_list[len(contender)] = contender



        return pal_list[max(pal_list.keys())]

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome('cbbd'))
