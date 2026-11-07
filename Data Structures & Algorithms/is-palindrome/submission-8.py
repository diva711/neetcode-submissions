class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower() 
        if s.isalnum():
            return s == s[::-1] 
        else : return False
        