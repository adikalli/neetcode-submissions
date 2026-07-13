class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        h={}
        res=set()
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                comp=(nums[i]+nums[j]) * -1 
                if comp in h and (h[comp]!=j and h[comp]!=i and i!=j)  :
                    res.add(tuple(sorted([nums[i], nums[j], comp])) )
                h[nums[j]]=j
        return [list(t) for t in res]
        