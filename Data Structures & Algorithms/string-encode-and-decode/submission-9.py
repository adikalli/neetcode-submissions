class Solution:
    def encode(self, strs: List[str]) -> str:
        inp= "".join([f"{len(s)}${s}" for s in strs])
        print(inp)
        return inp

    def decode(self, s: str) -> List[str]:
        res,start=[],0
        while start < len(s):
            end=start # initialise end starting with start 0->n
            while s[end]!="$":
                end+=1
            length = int(s[start:end])
            start = end+1
            end = start+length
            res.append(s[start:end])
            start=end
        return res

