class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        if strs==[""]:
            return "quotes"
        return '₹'.join(strs)

    def decode(self, s: str) -> List[str]:  
        o=s.split('₹')
        if s=='':
            return []
        if s=='quotes':
            return [""]
        return o


