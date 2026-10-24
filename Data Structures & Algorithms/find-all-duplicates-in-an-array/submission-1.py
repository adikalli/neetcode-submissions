class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            n = abs(n)
            if nums[n-1]<0:
                res.append(n)
            nums[n-1]= - nums[n-1]
        return res

# Notes:
"""
# 1. Iterate: Go through every number in the array .
# 2. Map to Index: Since each number is in the range (1 to n-1),you can map every number to an index by calculating n-1
# 3. Mark as Visited: To track that you've seen a number, go to the calculated index and multiply the value stored there by -1.
# 4. Detect Duplicates: Before marking, check the value at the mapped index. If the number there is already negative, it means you have encountered that number before, making it a duplicate.
# 5. Handle Signs: Always use the absolute value when checking the index so that negative numbers don't affect your calculations

Example:  [2, 3, 1, 2]
Step-by-Step Trace:

Index 0 (Value 2): Calculate index 2 - 1 = 1. Mark nums[1] as negative. The array becomes [2, -3, 1, 2].
Index 1 (Value -3): Use the absolute value 3. Calculate index 3 - 1 = 2. Mark nums[2] as negative. The array becomes [2, -3, -1, 2].
Index 2 (Value -1): Use the absolute value 1. Calculate index 1 - 1 = 0. Mark nums[0] as negative. The array becomes [-2, -3, -1, 2].
Index 3 (Value 2): Use the absolute value 2. Calculate index 2 - 1 = 1. Check nums[1]. Since it is already negative, we found a duplicate: 2.
Result: [2]
"""
