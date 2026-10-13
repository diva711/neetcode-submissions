class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t =[0]*2001
        for i in range(len(nums)):
            t[nums[i]+1000] +=1
        s =[] 
        for j in range(k):
            idx= t.index(max(t))
            num = idx-1000
            s.append(num)
            t[idx]=0
        return s
        
