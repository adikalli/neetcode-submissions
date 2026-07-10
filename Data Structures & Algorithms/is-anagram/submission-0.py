class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h={}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        h1={}
        for i in t:
            if i in h1:
                h1[i]+=1
            else:
                h1[i]=1
        
        if len(s)==len(t):
            m=[]
            for k,cnt in h.items():
                if k in h1:
                    if h1[k]==cnt:
                        m.append(True)
                    else:
                        m.append(False)
                else:
                    return False
            if all(m):
                return True
            else:
                return False
        else:
            return False
        
        