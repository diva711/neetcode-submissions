class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (s.remove(" ")) == s.reverse() :
            return true
        else :
            return false