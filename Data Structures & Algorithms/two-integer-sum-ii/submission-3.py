class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        while i < len(numbers):
            c=target-numbers[i]
            
            if c in numbers :
                j=numbers.index(c)
                return [i+1,j+1]
            i+=1
