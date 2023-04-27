"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Check if deleting the left character makes the rest of the string a palindrome
                if self.isPalindrome(s, left + 1, right):
                    return True
                # Check if deleting the right character makes the rest of the string a palindrome
                elif self.isPalindrome(s, left, right - 1):
                    return True
                else:
                    # Both substrings are not palindromes
                    return False
            left += 1
            right -= 1
        return True

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    s = "prakhar"
    sol = Solution()
    print(sol.validPalindrome(s))