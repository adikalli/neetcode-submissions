class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        print(nums)
        res=0
        for n in numset:
            if n-1 not in nums:
                length=0
                while n + length in numset:
                    length+=1
                res=max(res,length)
        return res
