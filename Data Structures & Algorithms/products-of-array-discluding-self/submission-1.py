class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_p=left_p=1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i]=left_p
            left_p*=nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            res[i]*=right_p
            right_p*=nums[i]
        return res