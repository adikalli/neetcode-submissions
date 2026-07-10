class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i in range(len(nums)):
            m[nums[i]]=i
        for i in range(len(nums)):
            if target-nums[i] in m and i!=m[target-nums[i]]:
                return [i,m[target-nums[i]]]
        return []
        