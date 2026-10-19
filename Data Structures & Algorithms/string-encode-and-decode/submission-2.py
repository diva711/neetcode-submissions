class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [] :
            return "None"
        m= "@".join(strs)
        return m
    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        n= s.split("@")
        return n