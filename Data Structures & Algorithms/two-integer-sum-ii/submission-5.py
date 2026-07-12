class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        for i,num in enumerate(numbers):
            if target-num in numbers and target-num !=numbers[i]:
                res.append(i+1)
        return res
        