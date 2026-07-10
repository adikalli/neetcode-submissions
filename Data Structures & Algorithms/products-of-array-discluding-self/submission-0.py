class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        o=[]
        for i in range(len(nums)):
            p=1
            for j in range(len(nums)):
                if j==i:
                    pass
                else:
                    p=p*nums[j]
            o.append(p)
        return o

        