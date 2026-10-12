class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in strs:
            k = [0] * 26
            for j in i:
                k[ord(j) - ord('a')] += 1
            if dic.get(tuple(k)):
                dic[tuple(k)].append(i)
            else:
                dic[tuple(k)] =[i]
        return list(dic.values())
            