class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        bucket= [[] for i in range(len(nums)+1)]
        
        for n in nums :
            if count.get(n):
                count[n] +=1
            else:
                count[n] =1
        for value,fre in count.items():
            bucket[fre].append(value)
        r=[]        
        for m in range(len(bucket) -1 , 0 , -1):
            for o in bucket[m]:
                r.append(o)
                if len(r)==k:
                    return r