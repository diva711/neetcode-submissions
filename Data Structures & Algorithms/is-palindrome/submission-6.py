class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (s.lower() and s.isalnum() and s.replace(" ","")) == s[::-1] : return True