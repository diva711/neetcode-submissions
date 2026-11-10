class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = defaultdict(int)
        for i in range (len(numbers)):
            diff = target - numbers[i]
            if s[diff]:
                return [s[diff], i+1]
            s[numbers[i]] = i + 1
        return []