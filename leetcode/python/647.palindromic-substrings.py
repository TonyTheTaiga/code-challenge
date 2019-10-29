#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start

'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

abba



'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        count = 0

        for index in range(len(s)):
            string = ""
            for x in s[index::]:
                string += x
                print(string)
                if string == string [::-1]:
                    count +=1

        return count


sol = Solution()

print(sol.countSubstrings("abba"))


# @lc code=end

