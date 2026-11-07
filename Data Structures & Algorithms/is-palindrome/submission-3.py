class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (s.replace(""," ")) == s.reverse() :
            return true
        else :
            return false