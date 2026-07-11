class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=defaultdict(int)
        res=[]
        for i in nums:
            a[i] +=1
        
        s=sorted(a.items(),key=lambda i:i[1],reverse=True)
        for i in s:
            res.append(i[0])
        return res[:k]



        
        