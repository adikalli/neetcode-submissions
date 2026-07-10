class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h=defaultdict(int)
        o=o1=[]
        for i in nums:
            h[i]+=1
        
        for key,v in h.items():
            o.append([v,key])
        
        sort_num = sorted(o)
        for i in sort_num:
            o1.append(i[1])
        return o1[::-1][:k]
        
        