class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        h={}
        res=set()
        # i=0
        if set(nums)==set([0]):return [[0,0,0]]
        # while nums.count(0)>1: 
        #     nums.remove(0)
        for i in range(len(nums)):
            # j=i+1
            for j in range(1,len(nums)):
                comp=(nums[i]+nums[j]) * -1 
                # print(comp)
                # print(h)
                if comp in h and (h[comp]!=j and h[comp]!=i and i!=j)  :
                    res.add(tuple(sorted([nums[i], nums[j], comp])) )
                h[nums[j]]=j
        return [list(t) for t in res]
        