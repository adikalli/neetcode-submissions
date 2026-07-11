class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_s=[]
        for s in strs:
            sorted_s.append(''.join([i for i in sorted(s)]))
        print(sorted_s)
        a={}
        for i,s in enumerate(sorted_s):
            print(i,s)
            if s not in a:
                a[s]=[strs[i]]
            else:
                a[s].append(strs[i])

        return list(a.values())