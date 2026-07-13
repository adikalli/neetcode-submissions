class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx_ar=0
        l=0
        r=len(heights)-1
        while l<r:
            area = (r-l) * min(heights[l],heights[r])     
            mx_ar=max(area,mx_ar)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return mx_ar
        