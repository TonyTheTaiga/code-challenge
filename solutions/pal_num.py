"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_copy = x
        rev = 0
        while x_copy > 0:
            rev += x_copy % 10
            x_copy = int(x_copy / 10)
            if x_copy == 0:
                break
            rev *= 10

        if x - rev == 0:
            return True

        return False
    
    def isPalindrome_str(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False


# if __name__ == "__main__":
#     sol = Solution()
#     ret = sol.isPalindrome(-121)