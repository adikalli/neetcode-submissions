class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mx_cnt=0
        dedup_num=list(set(nums))

        for num in dedup_num:
            if num-1 not in dedup_num: #start of a sequence
                length=1
                while num+length in dedup_num: # check longest consecutive sequence
                    length+=1
                mx_cnt=max(mx_cnt,length)
        return mx_cnt
        