class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        mp = {
            "(":")",
            "[":"]",
            "{":"}",
        }
        st = []
        val = []
        for i in s:
            if i in mp:
                st.append(i)
                print("curr stack",st)
            elif st:
                x = st.pop()
                print(f"pop: {x} curr:{i}")
                val.append(mp[x]==i)
            else:
                return False
        if len(st)!=0:
            return False
        print(val)
        return all(val)

