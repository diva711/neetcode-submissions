class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (s.lower() and s.isalnum() and s.replace(" ","")) == s[::-1] 