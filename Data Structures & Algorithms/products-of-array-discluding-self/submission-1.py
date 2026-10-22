class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=[]
        m = 1
        p= []
        flag = 0
        where = 0
        for i in nums:
            if i == 0:
                pass
            else:
                m *= i
        for j in range(len(nums)):
            n.append(m)
        for i in range(len(nums)):
            if nums[i] == 0:
                where = i
                flag +=1
            else:
                n[i] //= (nums[i])
            p.append(n[i])

        if flag == 1:
            p = [0]*len(nums)
            p[where]= m
            return p  
        else:
            return p