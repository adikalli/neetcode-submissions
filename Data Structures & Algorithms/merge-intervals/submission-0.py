class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda i:i[0])
        out = [intervals[0]]

        for start,end in intervals[1:]:
            last_end = out[-1][1]
            if start <= last_end:
                out[-1][1]=max(last_end,end) # max bcos[1,5] [2,4] -> [1,5]
            else:
                out.append([start,end])
        return out
        