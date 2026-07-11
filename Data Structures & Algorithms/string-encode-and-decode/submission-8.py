class Solution:
    def encode(self, strs: List[str]) -> str:
        return str(strs)
    def decode(self, s: str) -> List[str]:
        return eval(s)

    # def encode(self, strs: List[str]) -> str:
    #     if strs:
    #         inp= f"{len(strs)}"+"".join([f"${len(s)}${s}" for s in strs])
    #         print(inp)
    #         return inp
    #     else: return ''
    # def decode(self, s: str) -> List[str]:
    #     if s:
    #         o=[]
    #         n=int(s[0])
    #         start=1
    #         end=int(s[1])

    #         s_cp = s[1:]
    #         for i in range(n):
    #             o.append(s_cp[start:end+1])
    #             print(o)
    #             try:
    #                 start=end+2
    #                 end=start+int(s_cp[end+1])-1
    #                 print(start,end)
    #             except IndexError as ex: #Last Pass
    #                 pass
    #         return o
    #     else: return []

