class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (s.replace(""," ")) == s[::-1] :
            return True
        else :
            return False