class Solution:

    def encode(self, strs: List[str]) -> str:
        r=[]
        for s in strs:
            r.append(str(len(s)))
            r.append("#")
            r.append(s)
        return "".join(r) 
    def decode(self, s: str) -> List[str]:
        a=[]
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            a.append(s[i:j])
            i = j
        return a