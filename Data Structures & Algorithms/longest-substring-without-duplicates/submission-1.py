class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        save=0
        for i in range(len(s)):

            x= ord(s[i]) +1
            if ord(s[i]) == x:
                c+=1
            if save < c:
                save = c
        return save